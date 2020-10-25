### objective ### 
Reserving a character device in the kernel with a given major number using register_chrdev() function.
Create nodes for this device manually

### cmd ###
1- See if the device is registred after inserting the module.
	dmesg
2- See the device and the major number in the device list. 
	cat /proc/devices | grep Telnet_Device
3- Create a node for this module manually if the major number setted is accepted
	mknod /dev/node_name c 17 0
	note: 
	c: character device
 	17: major number
  	0: minor number
4- Remove a node
	rm /dev/node_name

