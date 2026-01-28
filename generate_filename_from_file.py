#!/usr/bin/env python3
import sys

def safe_filename(title):
    if not title:
        return None
    replacements = {'/': '_', '\\': '_', ':': '_', '*': '_', '?': '_', '"': '_', '<': '_', '>': '_', '|': '_', '#': ''}
    for old, new in replacements.items():
        title = title.replace(old, new)
    return ' '.join(title.split()) + '.mp3'

if __name__ == '__main__':
    title_file = sys.argv[1] if len(sys.argv) > 1 else '/tmp/episode_title.txt'
    try:
        with open(title_file, 'r', encoding='utf-8') as f:
            title = f.read().strip()
        if title:
            print(safe_filename(title))
        else:
            print(f"episode_{__import__('datetime').datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3")
    except:
        print(f"episode_{__import__('datetime').datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3")
