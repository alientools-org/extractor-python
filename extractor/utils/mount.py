import subprocess

def mount_iso(iso_path, mount_point):
    subprocess.run(['sudo', 'mount', '-o', 'loop', iso_path, mount_point], check=True)

def umount_iso(mount_point):
    subprocess.run(['sudo', 'umount', mount_point], check=True)
