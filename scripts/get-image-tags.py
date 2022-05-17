#!/usr/bin/env python3
import requests
import sys

docker_image = "adminer"
actions_image = sys.argv[1].lower()

tags_request = requests.get(
    f"https://raw.githubusercontent.com/docker-library/official-images/master/library/{docker_image}")
if tags_request.status_code == 200:
    import re
    tags = re.search(r'Tags\: .*, latest', tags_request.text).group().split(" ")[1:]
    tags = [f"{actions_image}:" + x.replace(",", "") for x in tags]
    print(",".join(tags))
else:
    exit(1)
