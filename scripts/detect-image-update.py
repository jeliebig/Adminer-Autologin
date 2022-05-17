#!/usr/bin/env python3
import importlib
import os
import requests
import shutil
import sys

docker_image = "adminer"
docker_repo_info_dir = os.path.join(os.path.dirname(__file__), "docker_repo_info")
cache_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".cache")

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
        print("true")
        with open(os.path.join(cache_dir, "latest-tag.digest"), "w") as file:
            file.write(image.digest)
    else:
        print("false")
else:
    exit(1)
