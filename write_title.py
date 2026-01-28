#!/usr/bin/env python3
import os, sys

title = os.environ.get('EPISODE_TITLE', '')
if not title:
    print("ERROR: EPISODE_TITLE not set", file=sys.stderr)
    sys.exit(1)

with open('/tmp/episode_title.txt', 'wb') as f:
    f.write(title.encode('utf-8'))
print(f"Wrote title ({len(title)} chars)")
