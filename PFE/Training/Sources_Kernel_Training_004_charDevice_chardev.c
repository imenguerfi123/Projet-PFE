#include <linux/module.h>
#include <linux/version.h>
#include <linux/kernel.h>
#include <linux/fs.h>

MODULE_LICENSE("GPL"); 
#define DEVICE_NAME "Telnet_Device"
 
static dev_t first; 
 
static int  new_char_driver_init(void) 
{
    if (alloc_chrdev_region(&first, 0, 3, DEVICE_NAME) < 0)
    {
        return -1;
    }
    printk(KERN_INFO "%s <Major, Minor>: <%d, %d>\n",DEVICE_NAME, MAJOR(first), MINOR(first)); 
    return 0;
}
 
static void  new_char_driver_exit(void) /* Destructor */
{
    unregister_chrdev_region(first, 3); 
    printk(KERN_INFO "%s is unregistered\n",DEVICE_NAME);
}
 
module_init(new_char_driver_init);
module_exit(new_char_driver_exit);
 
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Rami Ben Abdallah");
MODULE_DESCRIPTION("Character Driver using kdev_t library");
