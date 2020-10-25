### objective ###
Create a HelloWorld kernel module.

### link ###
https://www.geeksforgeeks.org/linux-kernel-module-programming-hello-world-program/

### cmd ###

# get the version of linux
uname -r
>4.13.0-38-generic

1- Preparing the system to run the code:
sudo apt-get install build-essential linux-headers-$(uname -r)

2- Create Makefile to compile source
3- Run the make command to compile the source code.
	make(default)/make all
	make clean
4- Loading/install the module
	sudo insmod hello.ko
5- Get information about the module using the modinfo command
	modinfo hello.ko
6- To see the messages, we need to read the kern.log in /var/log directory.
	tail /var/log/kern.log
7- To see messages we can also use the dmesg command
	dmesg
8- To see the loaded modules list we can use lsmod command
	lsmod 
9- To unload the module, we run rmmod
	sudo rmmod hello
