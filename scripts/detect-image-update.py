#!/usr/bin/env python3
import importlib
import os
import requests
import shutil
import sys

docker_repo_info_dir = os.path.join(os.path.dirname(__file__), "docker_repo_info")
docker_image = "adminer"
cache_dir = os.path.join(os.path.abspath("../"), ".cache")
actions_name_update = "update"
actions_set_output_update = f"::set-output name={actions_name_update}::"
actions_name_tags = "additional_tags"
actions_set_output_tags = f"::set-output name={actions_name_tags}::"
actions_image = sys.argv[1]

shutil.move(os.path.join(docker_repo_info_dir, "0.parse_repo.py"), os.path.join(docker_repo_info_dir, "parse_repo.py"))
importlib.invalidate_caches()
from docker_repo_info.parse_repo import parse

latest_tag = requests.get(
    f"https://raw.githubusercontent.com/docker-library/repo-info/master/repos/{docker_image}/remote/latest.md")
if latest_tag.status_code == 200:
    # linux; amd64
    image = parse(latest_tag.text)[0]
    if os.path.isfile(os.path.join(cache_dir, "latest-tag.digest")):
        with open(os.path.join(cache_dir, "latest-tag.digest"), "r") as file:
            last_digest = file.read()
    else:
        last_digest = None

    if last_digest != image.digest:
        print(actions_set_output_update + "true")
        with open(os.path.join(cache_dir, "latest-tag.digest"), "w") as file:
            file.write(image.digest)
        tags_request = requests.get(
            f"https://raw.githubusercontent.com/docker-library/official-images/master/library/{docker_image}")
        if tags_request.status_code == 200:
            import re
            tags = re.search(r'Tags\: .*, latest', tags_request.text).group().split(" ")[1:]
            tags = [f"{actions_image}:" + x.replace(",", "") for x in tags]
            print(actions_set_output_tags + ",".join(tags))
        else:
            print(f"[ERROR] Could not find tags in docker-library for image '{docker_image}'")
    else:
        print(actions_set_output_update + "false")
else:
    print(actions_set_output_update + "false")
    print(f"[ERROR] Could not get latest tag info for docker image '{docker_image}'.")
    exit(1)
