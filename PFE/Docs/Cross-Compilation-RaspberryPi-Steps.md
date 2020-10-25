
<center><h1 style="color: #ff0000">Cross Compiling for Raspberry Pi</h1></center>


   1- Create a directory for the demo.

                                   mkdir rpi

  2- Get the specific build toolchain in this directory

                         git clone https://github.com/raspberrypi/tools

  3- Cloning / Downloading the Raspbian image from Raspberry PI Github repository

      https://github.com/raspberrypi/linux/releases/tag/raspberrypi-kernel_1.20200212-1

<h3>Note</h3>

 >By default the one coming right now is version 4.19.y. This doesn’t exactly match with the one we need i.e. 4.19.97-v7+.However,So we look into the Releases tab. we find the one we want 4.19.97 This exactly matches with the one in NOOBS.
       
  4- Extract the tarball with the below command


                   tar -xvf linux-raspberrypi-kernel_1.20200212-1.tar.gz

  5- Adding the tool chain to your system PATH by entering the command line:

    PATH=$PATH:/home/imengurefi/rpi/tools/arm-bcm2708/arm-rpi-4.9.3-linux-gnueabihf/bin

  6- check if the tool chain has been added to your system PATH
 
                                      echo $PATH
 
  7-  build the sources and Device Tree files to Generate the .config File(default configuration):

For Pi 2, Pi 3, Pi 3+, or Compute Module 3:

	       cd rpi/linux-raspberrypi-kernel_1.20200212-1
	       KERNEL=kernel7
	       make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcm2709_defconfig

 Change the default configuration
 
           make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig
   
We activate ‘’FPGA configuration framework’’ 

For Raspberry Pi 4:
  	      
          cd linux-raspberrypi-kernel_1.20200212-1
	      KERNEL=kernel7l
          make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- bcm2711_defconfig
          make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig

8- Then, for all: compile the raspbian kernel

          make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- zImage modules dtbs


<h2>Sources</h2>


[linux-kernel-programming](https://techfortalk.co.uk/category/linux-kernel-programming/)