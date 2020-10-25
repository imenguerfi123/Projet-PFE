#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h> 
#include <linux/moduleparam.h>

/* Description of project */
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Rami Ben Abdallah");
MODULE_DESCRIPTION("kernel module with array parameter");
MODULE_VERSION("0.0.1");

/* Creation of module array parameter */

static int array[2];
static int arraySize;
module_param_array(array, int, &arraySize,  0660);
MODULE_PARM_DESC(array, "An array of integers");

static int kernel_module_init(void) {
	int i;
 	for (i = 0; i < arraySize ; i++)
  	{
 		printk(KERN_INFO "array[%d] = %d\n", i, array[i]);
 	}
 	return 0;
}
static void kernel_module_exit(void) {
 	printk(KERN_INFO "Goodbye! \n");
}
module_init(kernel_module_init);
module_exit(kernel_module_exit);
