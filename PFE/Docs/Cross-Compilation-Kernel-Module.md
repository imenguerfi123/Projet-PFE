<center><h1 style="color: #ff0000">Cross Compilation of the helloRPI Kernel Module</h1></center>

1. Create helloRPI.c


         #include <linux/module.h>	 /* Needed by all modules */ 
         #include <linux/kernel.h>	 /* Needed for KERN_INFO */ 
         #include <linux/init.h>	 /* Needed for the macros */ 

         MODULE_LICENSE("GPL"); 
         MODULE_AUTHOR("Author's Name"); 
         MODULE_DESCRIPTION("A simple Hello world LKM!"); 
         MODULE_VERSION("0.1"); 

         static int __init hello_start(void) 
         { 
	         printk(KERN_INFO "Hello world\n"); 
	         return 0; 
         } 

         static void __exit hello_end(void) 
         { 
	        printk(KERN_INFO "Goodbye Mr.\n"); 
          } 

          module_init(hello_start); 
          module_exit(hello_end); 

2. Create Makefile to compile source


        COMPILER:=$(HOME)/rpi/tools/arm-bcm2708/arm-rpi-4.9.3-linux-gnueabihf/bin/arm-linux-gnueabihf-
        SOURCE:=$(HOME)/rpi/linux-raspberrypi-kernel_1.20200212-1/
        PWD:=$(shell pwd)
        obj-m += helloRPI.o
        default:
	           make ARCH=arm CROSS_COMPILE=${COMPILER} -C $(SOURCE) M=$(PWD) modules
        clean:
	          make ARCH=arm CROSS_COMPILE=${COMPILER} -C $(SOURCE) M=$(PWD) clean


3. Run the make command to compile the source code.
	   
           make(default)/make all
	       make clean

4. Send the created object file (helloRPI.ko) to your Raspberry via SSH using the command line 
           
             sudo scp helloRPI.ko pi@IPADDRESS:/home/pi

5. Make the file executable from the RaspberryPi  by passing the command line 
  
                            "chmod +x helloRPI.ko" 

6. Loading/install the module
	
                             sudo insmod hello.ko

7. Get information about the module using the modinfo command
	
                              modinfo hello.ko

8. To see messages we can also use the dmesg command
	
                                      dmesg

9. To see the loaded modules list we can use lsmod command
	
                                       lsmod 
10. To unload the module, we run rmmod
	
                                      sudo rmmod hello


<h2>Sources</h2>

[Linux kernel Module](https://linux.die.net/lkmpg/index.html)