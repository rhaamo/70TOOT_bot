#!/usr/bin/env python3

import os, random
from mastodon import Mastodon
import config
import glob
import pathlib

masto = Mastodon(access_token='bot.usercred.secret', api_base_url=config.url)
masto.log_in()
files = glob.glob(f"{config.src_dir}/*.txt")

selected = random.choice(files)

base_filename = os.path.basename(os.path.splitext(selected)[0])

if os.path.exists(f"{config.src_dir}/{base_filename}.jpg"):
    picture = masto.media_post(f"{config.src_dir}/{base_filename}.jpg")
else:
    picture = None

try:
    if picture:
        masto.status_post(status=pathlib.Path(selected).read_text(), \
                media_ids=[picture], \
                visibility='unlisted',
                sensitive=None)
    else:
        masto.status_post(status=pathlib.Path(selected).read_text(), \
                visibility='unlisted',
                sensitive=None)
except:
    print("Failed to post to mastodon")
    exit()

os.rename(f"{config.src_dir}/{base_filename}.txt", f"{config.dst_dir}/{base_filename}.txt")
if picture:
    os.rename(f"{config.src_dir}/{base_filename}.jpg", f"{config.dst_dir}/{base_filename}.jpg")
