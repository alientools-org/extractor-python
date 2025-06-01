import os
import shutil
import tarfile
import py7zr
import zipfile
import tempfile
import pycdlib

def extract_archive(file_path, dest_dir):
    ext = file_path.lower().split('.')[-1]

    if ext == 'zip':
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(dest_dir)
    elif ext in ['tar', 'gz', 'tgz', 'bz2', 'xz']:
        with tarfile.open(file_path, 'r:*') as tar_ref:
            tar_ref.extractall(dest_dir)
    elif ext == '7z':
        with py7zr.SevenZipFile(file_path, mode='r') as sz:
            sz.extractall(path=dest_dir)
    elif ext == 'iso':
        # Beispiel: ISO mit pycdlib lesen
        extract_iso(file_path, dest_dir)
    else:
        print(f"Dateityp .{ext} wird nicht unterstützt.")
        return False
    return True

def extract_iso(iso_path, dest_dir):
    iso = pycdlib.PyCdlib()
    iso.open(iso_path)
    # ISO-Dateisystem rekursiv auslesen und speichern
    for root, dirs, files in iso.list_children(iso_path='/'):
        print(f"{root=}, {dirs=}, {files=}")
        # Hier kannst du Dateien extrahieren (pycdlib hat auch extract_file)
    iso.close()
