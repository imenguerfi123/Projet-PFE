#include <linux/module.h>
#include <linux/version.h>
#include <linux/kernel.h>
#include <linux/types.h>
#include <linux/kdev_t.h>
#include <linux/fs.h>
#include <linux/device.h>
#include <linux/cdev.h>
#include <linux/uaccess.h>

#define DEVICE "TELNET_DEVICE"
#define CLASS "TELNET_CLASS"
#define NODE "TELNET_NODE"

static char str[100]; 
static dev_t first; 
static struct cdev c_dev;
static struct class *cl; 
static int my_open(struct inode *i, struct file *f)
{
  printk(KERN_INFO "Rami Driver: open()\n");
  return 0;
}
  static int my_close(struct inode *i, struct file *f)
{
  printk(KERN_INFO "Rami Driver: close()\n");
  return 0;
}
 
static ssize_t my_read(struct file *f, char __user *buf, size_t len, loff_t *off)
{
   int i=0;
   str[99]='\n';
   printk(KERN_INFO "Driver: read()\n");
   for( i=0; i<100; i++){
      if (*off <100){
         if (copy_to_user(buf+i , str+i, 1) != 0){
             printk(KERN_ALERT "%lld\n",*off);
             return -EFAULT;}
         else{  (*off)++; }
       }else{  return 0;}
    }
    if(*off ==100) {  return 100;}
    return 0;
}
static ssize_t my_write(struct file *f, const char __user *buf, size_t len, loff_t *off)
{
    int i =0;
    printk(KERN_INFO "Driver: write()\n");
    for( i=0; i<len; i++)
        if (copy_from_user(str + i, buf+i , 1) != 0)
            return -EFAULT;
     return len;
}
  static struct file_operations pugs_fops =
{
  .owner = THIS_MODULE,
  .open = my_open,
  .release = my_close,
  .read = my_read,
  .write = my_write
};
 
static int mod_init(void) /* Constructor */
{
  if (alloc_chrdev_region(&first, 0, 1, DEVICE) < 0)
  {
    return -1;
  }
    if ((cl = class_create(THIS_MODULE, CLASS)) == NULL)
  {
    unregister_chrdev_region(first, 1);
    return -1;
  }
    if (device_create(cl, NULL, first, NULL, NODE) == NULL)
  {
    class_destroy(cl);
    unregister_chrdev_region(first, 1);
    return -1;
  }
    cdev_init(&c_dev, &pugs_fops);
    if (cdev_add(&c_dev, first, 1) == -1)
  {
    device_destroy(cl, first);
    class_destroy(cl);
    unregister_chrdev_region(first, 1);
    return -1;
  }
  return 0;
}
 
void mod_exit(void) /* Destructor */
{
  cdev_del(&c_dev);
  device_destroy(cl, first);
  class_destroy(cl);
  unregister_chrdev_region(first, 1);
  printk(KERN_INFO "Rami Driver is unregistered\n");
}
 
module_init(mod_init);
module_exit(mod_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Rami Ben Abdallah");
MODULE_DESCRIPTION("Character Driver With buffer");

