import os
import os.path
from os import path

bold = "\033[1m"
close_bold = "\033[0m"

print(f'''
{bold}--------------------------------
|                              |
|    Linux Fonts Installer     |
|  https://github.com/ujaRHR   |
|                              |
--------------------------------{close_bold}''')

print("\nChecking if all tools are installed...")

# Check if wget installed, if not, then install
if path.exists("/usr/bin/wget") == False:
    print("✗ wget not found, installing wget...")
    if path.exists("/usr/bin/apt") == True:
        os.system("sudo apt install wget -y")
        print("✓ Successfully installed wget!")
    elif path.exists("/usr/bin/yum") == True:
        os.system("sudo yum -y install wget")
        print("✓ Successfully installed wget!")
    else:
        print("✗ wget not found, and neither apt nor yum are installed!")
        print("✗ Please install wget manually!")
else:
    print("✓ Already Installed. Woah!")

user = os.getenv("USER")

fetchFonts="https://raw.githubusercontent.com/ujarhr/linux-font-installer/main/root/fonts.tar.xz"
fontsDir=f"/home/{user}/.fonts"

# Check if the directory exists, if not, then create it.
if path.exists(fontsDir) == False:
    os.system(f"mkdir -p {fontsDir}")
    print("✓ Successfully created fonts directory!")
else:
    print("✓ Fonts Directory already exists. Superb!")

print("↻ Downloading file...\n")

os.system(f"cd {fontsDir} ; /usr/bin/wget -q --show-progress -O fonts.tar.xz {fetchFonts}")

# Check if the file exists and extract it
if path.exists(f"{fontsDir}/fonts.tar.xz") == True:
    print("↻ Installing !\n")
    os.system(f"cd {fontsDir} ; tar -xf fonts.tar.xz ; rm fonts.tar.xz")
else:
    print("✗ Something went wrong! Try again...✗\n")
    os.system("exit")

print(f'''✓ {bold}Download and Installation Complete !!!
✓ Please restart your computer to see the changes.{close_bold}\n
❤ Thank you for using Linux Fonts Installer!
❤ Created by Reajul Hasan Raju
❤ https://github.com/ujaRHR''')