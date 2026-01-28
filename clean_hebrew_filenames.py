#!/usr/bin/env python3
import os, re, glob, sys

def clean_filename(filename):
    clean = filename.replace('#', '').replace('<', '_').replace('>', '_')
    clean = clean.replace(':', '_').replace('"', '_').replace('|', '_')
    clean = clean.replace('?', '_').replace('*', '_')
    clean = re.sub(r'\s+', ' ', clean)
    return clean

def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.chdir(folder)
    
    for mp3_file in glob.glob('**/*.mp3', recursive=True):
        dir_name = os.path.dirname(mp3_file)
        filename = os.path.basename(mp3_file)
        clean = clean_filename(filename)
        
        if filename != clean:
            old_path = os.path.join(dir_name, filename) if dir_name else filename
            new_path = os.path.join(dir_name, clean) if dir_name else clean
            try:
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} -> {clean}')
            except Exception as e:
                print(f'Failed: {filename} - {e}')

if __name__ == '__main__':
    main()
