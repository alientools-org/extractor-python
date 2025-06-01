import os
import sys
import shutil
import tarfile
import py7zr
import zipfile
import tempfile
import pycdlib
import argparse

from utils import analyze, extract, mount



def main():
    parser = argparse.ArgumentParser(description="Archiv- und ISO-Extraktor mit BIOS-Analyse")
    parser.add_argument('archive', help="Pfad zur ISO oder Archivdatei")
    parser.add_argument('dest', help="Zielverzeichnis zum Entpacken")
    args = parser.parse_args()

    success = extract_archive(args.archive, args.dest)
    if success:
        print(f"Extraktion abgeschlossen nach: {args.dest}")
        info = analyze_bios_iso(args.dest)
        print("Gefundene BIOS-Infos:")
        for k, v in info.items():
            print(f"{k}: {v}")
    else:
        print("Extraktion fehlgeschlagen.")

if __name__ == "__main__":
    main()
