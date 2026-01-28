#!/usr/bin/env python3
import json, subprocess, os, sys

def main():
    if len(sys.argv) < 3:
        print("Usage: download_multiple_episodes.py <json_file> <folder>")
        sys.exit(1)
    
    json_file = sys.argv[1]
    base_folder = sys.argv[2]
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, dict) and 'episodes' in data:
        episodes = data['episodes']
        podcast_title = data.get('podcast_title', 'Podcast')
    else:
        episodes = data
        podcast_title = 'Podcast'
    
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        podcast_title = podcast_title.replace(char, '')
    
    podcast_folder = os.path.join(base_folder, podcast_title.strip())
    os.makedirs(podcast_folder, exist_ok=True)
    
    for i, ep in enumerate(episodes, 1):
        url = ep.get('url')
        title = ep.get('title', f'episode_{i}')
        
        if not url:
            continue
        
        for char in invalid_chars:
            title = title.replace(char, '_')
        
        filename = f"{title}.mp3"
        target = os.path.join(podcast_folder, filename)
        
        print(f"Downloading {i}/{len(episodes)}: {title}")
        subprocess.run(['wget', '-O', target, url], check=False)

if __name__ == '__main__':
    main()
