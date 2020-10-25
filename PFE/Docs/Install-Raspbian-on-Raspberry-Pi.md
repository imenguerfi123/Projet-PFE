<center><h1 style="color: #ff0000">Install Raspbian on the Raspberry PI and connecting it to computer</h1></center>


<h2> Definition</h2>
Raspberry Pi is the name of a series of single-board computers made by the Raspberry Pi Foundation, a UK charity that aims to educate people in computing and create easier access to computing education.
<h3>Raspberrry Pi 4  </h3>

![](https://www.robot-advance.com/userfiles/www.robot-advance.com/images/raspberry-4-modele-b-4go.jpg)



 **- USB ports** — these are used to connect a mouse and keyboard. You can also connect other components, such as a USB drive.

 **- SD card slot** — you can slot the SD card in here. This is where the operating system software and your files are stored.

 **- Ethernet port** — this is used to connect Raspberry Pi to a network with a cable. Raspberry Pi can also connect to a network via wireless LAN.

 **- Audio jack** — you can connect headphones or speakers here.

  **- HDMI port** — this is where you connect the monitor (or projector) that you are using to display the output from the Raspberry Pi. If your monitor has speakers, you can also use them to hear sound.

 **- Micro USB power connector** — this is where you connect a power supply. You should always do this last, after you have connected all your other components.

 **- GPIO ports** — these allow you to connect electronic components such as LEDs and buttons to Raspberry Pi.
<h2>What you will need</h2>
<h3>Hardware</h3>
A Raspberry Pi computer with an SD card or micro SD card

A monitor with a cable (and, if needed, an HDMI adaptor)

A USB keyboard and mouse

A power supply

Headphones or speakers (optional)

An ethernet cable (optional)

<h3>Software</h3>
Raspbian, installed via NOOBS


<h2>Install Raspbian On Your Raspberry Pi</h2>
<h2>Install Noobs on a blank SD card</h2>

**Step 1: Download Noobs** 


You can download Noobs from the Raspberry Pi foundation website:                              
  [   https://www.raspberrypi.org/downloads/noobs/](   https://www.raspberrypi.org/downloads/noobs/)

**Step 2: Format your SD card in FAT 32 format**

**Step 3: Extract the files from the Noobs .zip archive**

Open the Noobs .zip file that you downloaded in step 1.

**Step 4: Copy the contents of the Noobs archive to the formatted SD card**

Your SD card is now ready, you just have to insert it into your Raspberry Pi.
Install Raspbian using Noobs
Insert the SD card containing Noobs in your Raspberry Pi and start it. To start a Raspberry Pi, just plug in the power.

Also consider connecting a keyboard, mouse and screen via HDMI to your Raspberry Pi for installation.

>Your Raspberry Pi should boot on the NOOBS utility and you have a list of available OSes.

![](https://www.raspberrypi-france.fr/wp-content/uploads/2019/05/install.png)

If you connect your RPi to Ethernet or configure the wifi, you will have access to new OS but by default, without internet connection, you can only install Raspbian or LibreELEC.
Choose **Raspbian** and click on “Install” or press the shortcut “i”.
Wait for Raspbian to install on your SD card, then your Raspberry Pi should restart and display the message **"OS installed successfully".**

<h2>Install Raspbian from a blank SD card</h2>

If you do not want to use the Noobs utility, it is possible to install Raspbian directly on the SD card but it takes a little longer.

 **Step 1:** Download the latest version of Raspbian

You can find the Raspbian disk image on the Raspberry Pi foundation website: [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/)

 **Step 2:** Unzip the archive

 **Step 3:** Download Etcher
Etcher is software that will install Raspbian (or any operating system) on the SD card and make it bootable directly.
There are other software but Etcher has the advantage of being compatible with Mac, Windows, Linux and is recommended by the Raspberry Pi foundation.

 **Step 4:** Insert your SD card into your computer and launch Etcher

 **Step 5:** Flash the SD card with Raspbian

Choose the Raspbian disk image in Etcher, select your SD card and start writing by clicking on "Flash"

![](https://pic.clubic.com/v1/images/1515912/raw)

You can then insert your SD card, connect the power supply to the Raspberry Pi to start it and it will boot on Raspbian.

<h2>Connect Raspberry PI to computer</h2>

After successfully booting Raspbian operating system on the chip, our mission now is making connection between the two computers. 

<h3>Finish the setup</h3>
When you start your Raspberry Pi for the first time, the Welcome to Raspberry Pi application will pop up and guide you through the initial setup.

![](https://projects-static.raspberrypi.org/projects/raspberry-pi-getting-started/395a8d858fe965db032b858601ca85e76ee22ba1/en/images/piwiz.gif)

  **Step 1: install ssh**

we have to install ssh for the two operating systems. The command line depends to the OS version in Linux.
For Raspbian and all Debian based operating systems the command is **"sudo apt-get install ssh".**

 **Step 2: Knowing the Raspberry PI's IP address**

we can get the IP address by passing **"ifconfig"** command in terminal.

 **Step 3: Connection step** 

Go to computer terminal and pass this command **"ssh  pi@ip_address "**, then we enter the login and the password.

<h2>Sources</h2>


[ Getting Started with Raspberry Pi]( https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started)