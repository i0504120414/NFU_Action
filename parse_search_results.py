#!/usr/bin/env python3
import json, sys

results = []
try:
    with open('/tmp/search_results.json', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    video = json.loads(line)
                    video_id = video.get('id')
                    results.append({
                        'id': video_id,
                        'title': video.get('title'),
                        'channel': video.get('channel') or video.get('uploader'),
                        'duration': video.get('duration'),
                        'view_count': video.get('view_count'),
                        'thumbnail': f"https://i.ytimg.com/vi/{video_id}/mqdefault.jpg",
                        'url': f"https://youtube.com/watch?v={video_id}"
                    })
                except:
                    pass
except:
    pass

output = {'ok': True, 'query': sys.argv[1] if len(sys.argv) > 1 else '', 'count': len(results), 'results': results}

print('===SEARCH_RESULTS_START===')
print(json.dumps(output, ensure_ascii=False, indent=2))
print('===SEARCH_RESULTS_END===')

with open('search_results.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
