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
#define NUMBER 5

static dev_t first; 
static struct cdev c_dev;
static struct class *cl; 
static int my_open(struct inode *i, struct file *f)
{
  printk(KERN_INFO "Driver: open()\n");
  return 0;
}
  static int my_close(struct inode *i, struct file *f)
{
  printk(KERN_INFO "Driver: close()\n");
  return 0;
}
 
static ssize_t my_read(struct file *f, char __user *buf, size_t len, loff_t *off)
{
   printk(KERN_INFO "Driver: read()\n");
    return 0;
}
static ssize_t my_write(struct file *f, const char __user *buf, size_t len, loff_t *off)
{
    printk(KERN_INFO "Driver: write()\n");
    return 0;
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
  int i,j;
  if (alloc_chrdev_region(&first, 0, NUMBER, DEVICE) < 0)
  {
    return -1;
  }
    if ((cl = class_create(THIS_MODULE, CLASS)) == NULL)
  {
    unregister_chrdev_region(first, NUMBER);
    return -1;
  }

  for(i=0;i<NUMBER;i++) {
    if (device_create(cl, NULL, MKDEV(MAJOR(first) , MINOR(first)+i ), NULL, "TELNET_NODE_%d",i) == NULL)
    {
      for(j=0;j<i;j++)
          device_destroy(cl, MKDEV(MAJOR(first) , MINOR(first)+j ));
      class_destroy(cl);
      unregister_chrdev_region(first, 2);
      return -1;
    }
  }
    cdev_init(&c_dev, &pugs_fops);
    if (cdev_add(&c_dev, first, 1) == -1)
  {
    device_destroy(cl, MKDEV(MAJOR(first) , MINOR(first)+1 ));
    device_destroy(cl, first);
    class_destroy(cl);
    unregister_chrdev_region(first, NUMBER);
    return -1;
  }
  return 0;
}
 
void mod_exit(void) /* Destructor */
{
int j;
  cdev_del(&c_dev);
  for(j=0;j<NUMBER;j++)
       device_destroy(cl, MKDEV(MAJOR(first) , MINOR(first)+j ));
  device_destroy(cl, first);
  class_destroy(cl);
  unregister_chrdev_region(first, NUMBER);
  printk(KERN_INFO "Module is unregistered\n");
}
 
module_init(mod_init);
module_exit(mod_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Rami Ben Abdallah");
MODULE_DESCRIPTION("Character Driver With buffer");

