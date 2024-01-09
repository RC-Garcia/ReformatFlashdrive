import subprocess

def format_usb_drive(drive_letter):
    try:
        # The 'format' command with the '/FS:FAT32' option formats the drive as FAT32
        subprocess.run(['format', drive_letter + ':', '/FS:FAT32', '/Q'], check=True)
        print(f"USB drive {drive_letter} formatted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'E' with the drive letter of your USB flash drive
    usb_drive_letter = 'E'
    format_usb_drive(usb_drive_letter)
