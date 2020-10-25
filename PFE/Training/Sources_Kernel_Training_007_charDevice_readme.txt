### objective ###
1- Create a device class. 
2- Create automatically a device node accessible to read and write by user using an automatically generated major number with  alloc_chrdev_region() function.

### cmd ###
1- See the new created class:
	ls /sys/class | grep Telnet
2- See the new created device node:
	ls /dev/ | grep Telnet
3- See the allocated major number of device:
	ls -a /proc/devices | grep Telnet
4- Write something in module buffer by user:
	echo "Some text">/dev/Telnet_Device_Node
5- Read the module buffer by user:
	cat /dev/Telnet_Device_Node

