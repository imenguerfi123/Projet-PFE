#include <stdio.h>
#include <sys/types.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/ioctl.h>
 
#include "chardev.h"
 
void get_vars(int fd)
{
    device_arg q;
 
    if (ioctl(fd, DEVICE_GET_VARIABLES, &q) == -1)
    {
        perror("DEVICE GET");
    }
    else
    {
        printf("x : %d\n", q.x);
        printf("y: %d\n", q.y);
        printf("z: %d\n", q.z);
    }
}
void clr_vars(int fd)
{
    if (ioctl(fd, DEVICE_CLR_VARIABLES) == -1)
    {
        perror("DEVICE CLR");
    }
}
void set_vars(int fd)
{
    int v;
    device_arg q;
 
    printf("Enter x: ");
    scanf("%d", &v);
    getchar();
    q.x = v;
    printf("Enter y: ");
    scanf("%d", &v);
    getchar();
    q.y = v;
    printf("Enter z: ");
    scanf("%d", &v);
    getchar();
    q.z = v;
 
    if (ioctl(fd, DEVICE_SET_VARIABLES, &q) == -1)
    {
        perror("DEVICE SET");
    }
}
 
int main(int argc, char *argv[])
{
    char *file_name = "/dev/Telnet_Device_Node";
    int fd;
    enum
    {
        e_get,
        e_clr,
        e_set
    } option;
 
    if (argc == 1)
    {
        option = e_get;
    }
    else if (argc == 2)
    {
        if (strcmp(argv[1], "-g") == 0)
        {
            option = e_get;
        }
        else if (strcmp(argv[1], "-c") == 0)
        {
            option = e_clr;
        }
        else if (strcmp(argv[1], "-s") == 0)
        {
            option = e_set;
        }
        else
        {
            fprintf(stderr, "Usage: %s [-g | -c | -s]\n", argv[0]);
            return 1;
        }
    }
    else
    {
        fprintf(stderr, "Usage: %s [-g | -c | -s]\n", argv[0]);
        return 1;
    }
    fd = open(file_name, O_RDWR);
    if (fd == -1)
    {
        perror("APP OPEN");
        return 2;
    }
 
    switch (option)
    {
        case e_get:
            get_vars(fd);
            break;
        case e_clr:
            clr_vars(fd);
            break;
        case e_set:
            set_vars(fd);
            break;
        default:
            break;
    }
 
    close (fd);
 
    return 0;
}
