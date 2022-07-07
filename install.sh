#!/bin/bash
bold=$(tput bold)
normal=$(tput sgr0)

echo "${bold}--------------------------------"
echo "|                              |"
echo "|    Linux Fonts Installer     |"
echo "|  https://github.com/ujaRHR   |"
echo "|                              |"
echo "--------------------------------${normal}"

echo ""
echo "Checking if all tools are installed..."

# Check if wget installed, if not, then install
if ! command -v wget &> /dev/null
then
    echo "wget not found, installing wget..."
    sudo apt-get install wget
    yum install wget
else
  echo "✓ Woah! Already Installed!"
fi


fetchFonts="https://github.com/ujaRHR/linux-font-installer/raw/master/fonts.tar.xz"
fontsDir="/home/$USER/.fonts/Linux-Fonts"

# Check if the directory exists, if not, then create it.
if [ ! -d "$fontsDir" ]; then
  mkdir -p $fontsDir;
else
  rm -r $fontsDir;
  mkdir -p $fontsDir;
fi

echo -e "↻ Downloading file...\n"

cd $fontsDir;
/usr/bin/wget $fetchFonts

# Check if the file exists and extract it
cd $fontsDir"/"
if [ -f fonts.tar.xz ];
then
    echo -e "↻ Installing  !\n";
    tar -zxvf fonts.tar.xz;
    rm fonts.tar.xz;
else
    echo -e "✗ Something went wrong! Try again...✗\n";
    exit;
fi

echo -e "\n✓ ${bold}Download and Installation Complete !!!"
echo -e "✓ Please restart your computer to see the changes.\n"
echo -e "❤ ${normal}Thank you for using Linux Fonts Installer!"
echo -e "❤ Created by Reajul Hasan Raju"
echo -e "❤ https://github.com/ujaRHR"