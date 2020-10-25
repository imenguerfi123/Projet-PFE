### objective ### 
Reserving a character device in the kernel with a dynamically allocated major number (First way) using alloc_chrdev_region () function.

### cmd ###
1- See if the device is registred after inserting the module.
	dmesg
2- See the device and the major number in the device list. 
	cat /proc/devices | grep Telnet_Device
