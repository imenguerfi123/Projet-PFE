#ifndef CHARDEV_H
#define CHARDEV_H
#include <linux/ioctl.h>
 
typedef struct
{
    int x, y, z;
} device_arg;
 
#define DEVICE_GET_VARIABLES _IOR('q', 1, device_arg *)
#define DEVICE_CLR_VARIABLES _IO('q', 2)
#define DEVICE_SET_VARIABLES _IOW('q', 3, device_arg *)
 
#endif

