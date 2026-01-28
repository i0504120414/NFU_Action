#!/usr/bin/env python3
import sys, os, time, requests, json, mimetypes, base64
from urllib.parse import quote
from pathlib import Path

def upload_to_release(token, owner, repo, tag_name, file_paths):
    url = f'https://api.github.com/repos/{owner}/{repo}/releases/tags/{tag_name}'
    headers = {'Authorization': f'token {token}', 'Accept': 'application/vnd.github.v3+json'}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f'Failed to get release: {response.status_code}')
        return []
    
    release = response.json()
    upload_url_base = release['upload_url'].split('{')[0]
    
    time.sleep(5)
    
    results = []
    for idx, fp in enumerate(file_paths):
        try:
            file_path = Path(fp)
            filename = file_path.name
            encoded_filename = quote(filename, safe='')
            content_type = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
            
            upload_url = f'{upload_url_base}?name={encoded_filename}'
            
            with open(file_path, 'rb') as f:
                resp = requests.post(upload_url, headers={'Authorization': f'token {token}', 'Content-Type': content_type}, data=f, timeout=300)
            
            if resp.status_code in (200, 201):
                results.append({'index': idx, 'original_name': filename, 'asset_id': resp.json().get('id')})
                print(f'Uploaded: {filename}')
            else:
                print(f'Failed: {filename} - {resp.status_code}')
        except Exception as e:
            print(f'Error: {fp} - {e}')
    
    return results

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage: upload_to_release.py <token> <owner> <repo> <tag> <files...>')
        sys.exit(1)
    
    results = upload_to_release(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], [f for f in sys.argv[5:] if os.path.exists(f)])
    
    if results:
        print('===FILENAME_MAPPING_START===')
        print(base64.b64encode(json.dumps(results).encode()).decode())
        print('===FILENAME_MAPPING_END===')
