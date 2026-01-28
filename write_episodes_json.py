#!/usr/bin/env python3
import os, sys

def main():
    episodes_json = os.environ.get('EPISODES_JSON', '')
    if not episodes_json:
        print("Error: EPISODES_JSON is empty", file=sys.stderr)
        sys.exit(1)
    
    with open('/tmp/episodes.json', 'w', encoding='utf-8') as f:
        f.write(episodes_json)
    print(f"Wrote {len(episodes_json)} chars")

if __name__ == '__main__':
    main()
