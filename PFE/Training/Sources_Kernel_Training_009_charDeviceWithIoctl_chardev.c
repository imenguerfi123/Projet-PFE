#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/version.h>
#include <linux/fs.h>
#include <linux/cdev.h>
#include <linux/device.h>
#include <linux/errno.h>
#include <linux/uaccess.h> 
#include "chardev.h"
 
#define DEVICE_NAME "Telnet_Device"
#define DEVICE_CLASS "Telnet_Device_Class"
#define DEVICE_NODE "Telnet_Device_Node"
#define FIRST_MINOR 0
#define MINOR_CNT 1
 
static dev_t dev;
static struct cdev c_dev;
static struct class *cl;
static int x = 1, y = 3, z = 5;
 
static int device_open(struct inode *i, struct file *f)
{
    return 0;
}
static int device_close(struct inode *i, struct file *f)
{
    return 0;
}
#if (LINUX_VERSION_CODE < KERNEL_VERSION(2,6,35))
static int device_ioctl(struct inode *i, struct file *f, unsigned int cmd, unsigned long arg)
#else
static long device_ioctl(struct file *f, unsigned int cmd, unsigned long arg)
#endif
{
    device_arg q;
 
    switch (cmd)
    {
        case DEVICE_GET_VARIABLES:
            q.x = x;
            q.y = y;
            q.z = z;
            if (copy_to_user((device_arg *)arg, &q, sizeof(device_arg)))
            {
                return -EACCES;
            }
            break;
        case DEVICE_CLR_VARIABLES:
            x = 0;
            y = 0;
            z = 0;
            break;
        case DEVICE_SET_VARIABLES:
            if (copy_from_user(&q, (device_arg *)arg, sizeof(device_arg)))
            {
                return -EACCES;
            }
            x = q.x;
            y = q.y;
            z = q.z;
            break;
        default:
            return -EINVAL;
    }
 
    return 0;
}
 
static struct file_operations fops =
{
    .owner = THIS_MODULE,
    .open = device_open,
    .release = device_close,
#if (LINUX_VERSION_CODE < KERNEL_VERSION(2,6,35))
    .ioctl = device_ioctl
#else
    .unlocked_ioctl = device_ioctl
#endif
};
 
static int __init module_Init(void)
{
    int ret;
    struct device *dev_ret;
 
 
    if ((ret = alloc_chrdev_region(&dev, FIRST_MINOR, MINOR_CNT, DEVICE_NAME)) < 0)
    {
        return ret;
    }
 
    cdev_init(&c_dev, &fops);
 
    if ((ret = cdev_add(&c_dev, dev, MINOR_CNT)) < 0)
    {
        return ret;
    }
     
    if (IS_ERR(cl = class_create(THIS_MODULE, DEVICE_CLASS)))
    {
        cdev_del(&c_dev);
        unregister_chrdev_region(dev, MINOR_CNT);
        return PTR_ERR(cl);
    }
    if (IS_ERR(dev_ret = device_create(cl, NULL, dev, NULL, DEVICE_NODE)))
    {
        class_destroy(cl);
        cdev_del(&c_dev);
        unregister_chrdev_region(dev, MINOR_CNT);
        return PTR_ERR(dev_ret);
    }
 
    return 0;
}
 
static void __exit module_Exit(void)
{
    device_destroy(cl, dev);
    class_destroy(cl);
    cdev_del(&c_dev);
    unregister_chrdev_region(dev, MINOR_CNT);
}
 
module_init(module_Init);
module_exit(module_Exit);
 
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Rami Ben Abdallah");
MODULE_DESCRIPTION("Char Device with ioctl call");

