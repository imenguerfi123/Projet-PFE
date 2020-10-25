/*
 * start.c 
 */

#include <linux/kernel.h> 

#include <linux/module.h> 

int init_module(void)

{
 printk(KERN_EMERG "EMERG Hello world!\n");

printk(KERN_ALERT "ALERT Hello world!\n");

printk(KERN_CRIT "CRIT Hello world!\n");

printk(KERN_ERR "ERR Hello world!\n");

printk(KERN_WARNING "WARNING Hello world!\n");

printk(KERN_NOTICE "NOTICE Hello world!\n");

printk(KERN_INFO "INFO Hello world!\n");

printk(KERN_DEBUG "DEBUG Hello world!\n");
 
return 0;
}
