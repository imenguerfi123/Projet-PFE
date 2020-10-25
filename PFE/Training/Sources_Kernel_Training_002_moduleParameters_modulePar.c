#include <linux/init.h>

#include <linux/module.h>

#include <linux/kernel.h> 

#include <linux/moduleparam.h>


/* Description of project */

MODULE_LICENSE("GPL");

MODULE_AUTHOR("Imen Guerfi");

MODULE_DESCRIPTION("kernel module with parameter");

MODULE_VERSION("0.0.1");


/* Creation of module parameter */

static int parameter = 0;

module_param(parameter, int, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP);

MODULE_PARM_DESC(parameter, "An integer param");


static int kernel_module_init(void) {
 
printk(KERN_INFO "Hello, the module parameter is: %d\n", parameter);

 return 0;
}


static void kernel_module_exit(void) 
{//Exit module function
 printk(KERN_INFO "Goodbye, the module parameter is: %d\n", parameter);

}



module_init(kernel_module_init);

module_exit(kernel_module_exit);
