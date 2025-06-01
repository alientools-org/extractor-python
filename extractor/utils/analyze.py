import os
import shutil
import tarfile
import py7zr
import zipfile
import tempfile
import pycdlib




def analyze_bios_iso(extract_path):
    info = {}
    for root, _, files in os.walk(extract_path):
        for f in files:
            if 'readme' in f.lower():
                with open(os.path.join(root, f), 'r', errors='ignore') as file:
                    content = file.read()
                    info['readme'] = content[:500]  # Erstes 500 Zeichen
            elif f.endswith('.bin'):
                info.setdefault('firmware_files', []).append(f)
    return info
