#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <asm/uaccess.h> 

MODULE_LICENSE("GPL"); 

#define DEVICE_NAME "Telnet_Device"
#define Major 17

static int device_open(struct inode *inode, struct file *file)
{
 return 0;
}

static int device_release(struct inode *inode, struct file *file)
{
 return 0;
}

static ssize_t device_read(struct file *filp, char *buffer, size_t length, loff_t * offset)
{
 return 0;
}

static ssize_t device_write(struct file *filp, const char *buff, size_t len, loff_t * off)
{
 return 0;
}

static struct file_operations fops = {
 .read = device_read,
 .write = device_write, 
 .open = device_open, 
 .release = device_release
};


int init_module(void){
 	
 	if (!register_chrdev(Major, DEVICE_NAME, &fops)) {
 		printk(KERN_ALERT "The allocated major number is :  %d\n", Major);
 		return Major;
 	}
	else{
		printk(KERN_ALERT "NO WAY :%d is already reserved as a major number!\n",Major);	
	} 
 	return 0;
}

void cleanup_module(void){
	
 	unregister_chrdev(Major, DEVICE_NAME);
 	printk(KERN_INFO "Device clean");
}
