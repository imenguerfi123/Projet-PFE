#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>

#define PROC_NAME "Telnet_Proc"


static int proc_show(struct seq_file *m, void *v) {
  seq_printf(m, "Hello from Telnet proc!\n");
  return 0;
}

static int proc_open(struct inode *inode, struct  file *file) {
  printk(KERN_INFO "procfile_read (/proc/%s) called\n", PROC_NAME);
  return single_open(file, proc_show, NULL);
}

static const struct file_operations proc_fops = {
  .owner = THIS_MODULE,
  .open = proc_open,
  .read = seq_read,
  .llseek = seq_lseek,
  .release = single_release,
};

static int __init proc_init(void) {
  proc_create(PROC_NAME, 0, NULL, &proc_fops);
  printk(KERN_INFO "/proc/%s created\n", PROC_NAME);
  return 0;
}

static void __exit proc_exit(void) {
  remove_proc_entry(PROC_NAME, NULL);
  printk(KERN_INFO "/proc/%s removed\n", PROC_NAME);
}

MODULE_LICENSE("GPL");
module_init(proc_init);
module_exit(proc_exit);

