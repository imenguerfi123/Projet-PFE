<center>
<h1 style="color: #ff0000">Linux Kernel</h1>
</center>
<h2>Linux</h2> 

Linux is an operating system, resembles a UNIX OS – a stable multi-user multi-tasking operating system, and that has been assembled as a free and open-source software for development and distribution. 
<h3>Kernel </h3> 
A kernel is  <span style="color: #26B260">a central component of an operating system that acts as an interface between the user applications and the hardware</span> .The aim of the kernel is to manage the communication between the software (user level applications) and the hardware (CPU, disk memory etc).

<h2>The main tasks of the kernel</h2>  
<ul>
<li>Process management</li>
<li>Device management </li>
<li>Memory management</li>
<li>Interrupt handlingI/O communication</li>
<li>File system</li>
<li>System call control</li>
</ul>
 

<h3>Types of Kernels</h3> 

**Monolithic Kernel:** All operating system services run along the main kernel thread in a monolithic kernel, which also resides in the same memory area, thereby providing powerful and rich hardware access. The monolithic kernel includes not only the central processing unit, memory and IPC, but also device drivers, system server calls and file system management.

**Micro Kernel:** Define a simple abstraction over hardware that use primitives or system calls to implement minimum OS services such as multitasking, memory management and interprocess communication.

**Hybrid Kernel:** Run a few services in the kernel space to reduce the performance overhead of traditional microkernels where the kernel code is still run as a server in the user space.

**Nano Kernel:** Simplify the memory requirement by delegating services, including the basic ones like interrupt controllers or timers to device drivers.

**Exo Kernel:** Allocate physical hardware resources such as processor time and disk block to other programs, which can link to library operating systems that use the kernel to simulate operating system abstractions.

>**The Linux kernel is a monolithic computer operating system kernel that resembles the UNIX system.**

<h2>Linux Directory Tree</h2>

To understand Linux kernel, we can't escape the phase of understanding Linux Directory tree. 

![](https://nepalisupport.files.wordpress.com/2016/06/linux-filesystem.png)

- **/ – The Root Directory:** Everything on your Linux system is located under the / directory, known as the root directory.

- **/bin – Essential User Binaries:** important system programs and utilities such as the bash shell are located in /bin.
- **/sbin – System Administration Binaries:** The /sbin directory is similar to the /bin directory. It contains essential binaries that are generally intended to be run by the root user for system administration.
- **/boot – Static Boot Files:** The /boot directory contains the files needed to boot the system – for example, the GRUB boot loader’s files and Linux kernels are stored here. The boot loader’s configuration files aren’t located here, though – they’re in /etc with the other configuration files.
- **/etc – Configuration Files:** The /etc directory contains system-wide configuration files, which can generally be edited by hand in a text editor.
- **/dev – Device Files:** Linux exposes devices as files, and the /dev directory contains a number of special files that represent devices. This directory also contains pseudo-devices, which are virtual devices that don’t actually correspond to hardware, for example, /dev/random produces random numbers. /dev/null is a special device that produces no output and automatically discards all input.
- **/proc – Kernel & Process Files:** The /proc directory similar to the /dev directory because it doesn’t contain standard files. It contains special files that represent system and process information.
- **/sys – Kernel Interface:** It provides a filesystem-like view of information and configuration settings that the kernel provides, much like /proc but it interact with the whole system and kernel. Writing to these files may or may not write to the actual device, depending on the setting you're changing.
- **/home – Home Folders:** The /home directory contains a home folder for each user.
- **/root – Root Home Directory:** The /root directory is the home directory of the root user. Instead of being located at /home/root, it’s located at /root. This is distinct from /, which is the system root directory.
- **/lib – Essential Shared Libraries:** The /lib directory contains libraries needed by the essential binaries in the /bin and /sbin folder. Libraries needed by the binaries in the /usr/bin folder are located in /usr/lib.
- **/usr – User Binaries & Read-Only Data:** The /usr directory contains applications and files used by users, as opposed to applications and files used by the system. For example, non-essential applications are located inside the /usr/bin directory instead of the /bin directory and non-essential system administration binaries are located in the /usr/sbin directory instead of the /sbin directory. Libraries for each are located inside the /usr/lib directory. The /usr directory also contains other directories – for example, architecture-independent files like graphics are located in /usr/share.
- **/media – Removable Media:** The /media directory contains subdirectories where removable media devices inserted into the computer are mounted. For example, when you insert a CD into Linux system, a directory will automatically be created inside the /media directory.
- **/mnt – Temporary Mount Points:** The /mnt directory is where system administrators mounted temporary file systems while using them. For example, if you’re mounting a Windows partition to perform some file recovery operations, you might mount it at /mnt/windows.
- **/opt – Optional Packages:** The /opt directory contains subdirectories for optional software packages.
- **/run – Application State Files:** The /run directory is fairly new, and gives applications a standard place to store transient files they require like sockets and process IDs.
- **/srv – Service Data:** The /srv directory contains “data for services provided by the system.” If you were using the Apache HTTP server to serve a website, you’d likely store your website’s files in a directory inside the /srv directory.
- **/tmp – Temporary Files:** Applications store temporary files in the /tmp directory. These files are generally deleted whenever your system is restarted and may be deleted at any time by utilities such as tmpwatch.
- **/var – Variable Data Files:** The /var directory is the writable counterpart to the /usr directory, which must be read-only in normal operation. Log files and everything else that would normally be written to /usr during normal operation are written to the /var directory.
- **/lost+found – Recovered Files:** Each Linux file system has a lost+found directory. If the file system crashes, a file system check will be performed at next boot. Any corrupted files found will be placed in the lost+found directory, so you can attempt to recover as much data as possible.

>**By default the tree command is not installed. Type the following command to install  *''sudo apt-get install tree''***

<h2>Linux System Architecture </h2>

<h3>User Space</h3>

The User Space is the space in memory where user processes run. 

This Space is protected. The system prevents one process from interfering with another process. 

Only Kernel processes can access a user process

<h3>Kernel Space</h3>

The kernel Space is the space in memory where kernel processes run. 

The user has access to it only through the system call.

<h3>System Call</h3>

User Space and Kernel Space are in different spaces. 

When a System Call is executed, the arguments to the call are passed from User Space to Kernel Space.

A user process becomes a kernel process when it executes a system call.

![](https://tecadmin.net/tutorial/wp-content/uploads/2017/10/linux-architecture-image.png )

 
<h3>User Space and Kernel Space Relationship</h3>


![](https://images.slideplayer.com/17/5311154/slides/slide_1.jpg)

**The Linux kernel relationship with the Hardware**

The kernel can manage the system’s hardware through what is referred to as interrupts. When the hardware wants to interface with the system, an interrupt is issued that interrupts the processor that in turn does the same to the kernel. To provide synchronization, the kernel can disable interrupts, be it a single one or all of them. In Linux, however, the interrupt handlers do not run in a process context, they instead run in an interrupt context not associated with any process.This particular interrupt context exists solely to let an interrupt handler quickly respond to an individual interrupt and then finally exit.

<h2>Kernel Functional</h2>

- File System
- Process Management
- Device Driver
- Memory Management
- Networking

![](https://www.sharetechnote.com/image/Linux_DeviceDriver_Overview_01.png)


<h2>Functional & Architectural Layer</h2>

**File System :** It is responsible for storing information on disk and retrieving and updating this information.The File System is accessed through system calls such as : open, read, write,etc.


![](https://dev.monometric.io/img/articles/kernel-file-descriptors.svg)

**Type of Files**

The Unix system has the following types of files
 
 - **Ordinary Files :** Contain information entered into them by a user, an application, etc.

 - **Directory Files :** Manage the cataloging of the file system

 - **Special Files (devices) :** Used to access the peripheral devices
 
 - **FIFO Files for Pipes**

![](https://www.bottomupcs.com/chapter00/figures/pipe.png)


**File System Structure**

 - **Boot Block :** information needs to boot the system

 - **Super Block :** File System Specifications : Size, Max. number of files, Free blocks, Free inodes
 - **Inode List**

 - **Block List :** The files data

 - **Inode :** The inode represents all the information needed by the kernel to manipulate a file. Each file has an inode structure that is identified by an i-number. It doesn’t contain file name.

**Virtual File System :** It manages all the different file system. It is an abstraction layer between the application program and the file system implementations. It describes the system’s file in term of superblocks and 
inodes.


![](https://lh3.googleusercontent.com/proxy/8fjd8CrDokeSzfRi6pYtchE9aazmmwjCVr4YGQuM7DepNH_Bfb1hVe_aJhmO8x6sdASlbuQJ6Ek45P8sWaTaHhHYNqCh0Mimk_0kfI0RKjje1lGEQ8VBHg)


<h2>Process Management</h2>

The Unix OS is a time-sharing system.

Every process is scheduled to run for a period of time (time slice). 

Kernel creates, manages and deletes the processes

Every process (except init) in the system is create as the result of a fork system call. 

The fork system call splits a process into two processes (Parent and Child).

Each process has a unique identifier (Process ID).

<h3>Type of Processes</h3>
 
**Create (new) :** When a process is first created, it occupies the "created" or "new" state. In this state, the process awaits admission to the "ready" state.

**Ready and Waiting :** A "ready" or "waiting" process has been loaded into main memory and is awaiting execution on a CPU

**Running :** A process moves into the running state when it is chosen for execution.

**Terminated :** A process may be terminated, either from the "running" state by completing its execution or by explicitly being killed.

<h2>DeviceDriver</h2>

On of the purpose of an OS is to hide the system’s hardware from user. Instead of putting code to manage the HW controller into every application, the code is kept in the Linux kernel. It abstracts the handling of devices. All HW devices look like regular files.
First of all, we have to know that devices are divided into two types: character devices and block devices. 
 
- **Block devices :** have a buffer for requests, so they can choose the best order in which to respond to the requests. This is important in the case of storage devices. It can only accept input and return output in blocks (whose size can vary according to the device) 

- **Character devices :**  are allowed to use as many or as few bytes as they like. Most devices in the world are character, because they don't need this type of buffering, and they don't operate with a fixed block size. 

Now we will explain how the process of communication is implemented, in fact, every device has its own protocol and obviously this protocol must be supported by the kernel, which means the existence of a device driver integrated in the Kernel able to communicate with the device hardware for example USB protocol.

![](https://www.bottomupcs.com/chapter00/figures/file-descriptors.png)

Also the driver must create a special file in the **/dev** to represent the device and those files are used literally from user programs through a call system function.
In general every single device is represented with many files for specific reasons, for example, the whole Hard disk is represented by one file, but also every partition of the same disk has its own represented file. For that the Linux kernel represents devices as pairs of numbers : 

- **The major number :**  tells you which driver is used to access the hardware, each driver is assigned a unique major number and all device files with the same major number are controlled by the same driver.
-  **The minor number** is used by the driver to distinguish between the various hardware it controls.

To ensure the communication between those files and the user programs, the Linux kernel has introduced a control System Call operation called **ioctl () (Input/Output Control)**. Practical examples include volume control for an audio device, display configuration for a video device, reading device registers, and so on — basically, anything to do with device input/output, or device-specific operations.

![](https://olegkutkov.me/wp-content/uploads/2018/03/serail_driver_read.png)



<h2>Memory Management</h2>

<h3>Physical memory</h3> 

Is actually present in the machine and limited.

<h3>Virtual memory</h3>

 - **Large Address Spaces :** The operating system makes the system appear as if it has a larger amount of memory than it actually has. The virtual memory can be many times larger than the physical memory in the system.

 - **Protection :** Each process in the system has its own virtual address space. These virtual address spaces are completely separate from each other and so a process running one application cannot affect another. Also, the hardware virtual memory mechanisms allow areas of memory to be protected against writing. This protects code and data from being overwritten by rogue applications.

 - **Memory Mapping :** Memory mapping is used to map image and data files into a processes address space. In memory mapping, the contents of a file are linked directly into the virtual address space of a process.

 - **Shared Virtual Memory :** Although virtual memory allows processes to have separate (virtual) address spaces, there are times when you need processes to share memory. For example there could be several processes in the system running the bash command shell. Rather than have several copies of bash, one in each processes virtual address space, it is better to have only one copy in physical memory and all of the processes running bash share it. Dynamic libraries are another common example of executing code shared between several processes.

 - **Fair Physical Memory Allocation :** The memory management subsystem allows each running process in the system a fair share of the physical memory of the system
 

![](https://www.admin-magazine.com/var/ezflow_site/storage/images/archive/2014/21/memory-management-on-high-end-systems/figure-2/91088-1-eng-US/Figure-2_reference.png)


**BSD socket layer**

- It is a general interface (abstract layer).
- Used in networking and IPC.
- Socket address families:  UNIX, INET, AX25, IPX, APPLETALK, X25

**INET socket layer**

It supports the Internet address family. Its interface with BSD socket layer is through a set of operation which is registered with BSD socket layer.
Type of sockets

 - **Stream Socket :** Provide a reliable, sequenced, two-way connection (such as TCP).

 - **Datagram Socket :** A connection-less and unreliable connection (such as UDP).

 - **Raw Socket :**  Used for internal network protocols.

![](https://flylib.com/books/3/223/1/html/2/files/01fig04.gif)




<h2>Sources</h2>

[ Linux-kernel]( https://linuxhint.com/linux-kernel-tutorial-beginners/)

[ Kernel Architecture ]( https://slideplayer.com/slide/13907109/ "Kernel Architecture ")

[Linux-Device-Drivers-Series ](https://opensourceforu.com/tag/linux-device-drivers-series/page/2/)


