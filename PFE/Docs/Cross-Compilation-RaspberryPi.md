<center><h1 style="color: #ff0000">Raspberry PI</h1></center>

<h2>Operating System</h2>
An operating system (OS) is system software that manages component hardware and software resources and provides common services for it. The component might be Desktop, Laptop, Phone, Tablet, etc.

The operating system consists of:

- **The bootloader:** software in charge of the boot process of the device. 
- **The kernel:** the core of the system and manages the CPU, memory and peripheral devices.
- **Daemons:** background services.
- **The shell:** comprises a command process that allows manipulation of the device through commands entered into a text interface.
- **Graphical Server:** the sub-system that shows the graphics on the screen.
- **Desktop Environment:** this is what the users usually interact with.
- **Applications:** are programs that perform the user’s tasks such as word processors.

An os is composed from two spaces:

  **- Kernel Space:**  
 Kernel space the core access to the hardware and system services are managed and provided as a service to the rest of the system.

  **- User Space:**  
 the user’s applications are carried out in the user-space, where they can reach a subset of the machine’s available resources via kernel system calls.

<h2>Operating System for Raspberry PI</h2> 

Since the Raspberry PI is a tiny computer, a tiny operating system should be installed to benefit from most of Raspberry's features.
A large number of operating system is available to be installed on Raspberry PI which the more powerful, efficient and popular one is the official Debain based OS announced by the Raspberrypi website is the Raspbian because it an official OS that has thousands of pre built libraries to perform many tasks and optimize the OS and support Python language.

There are NOOBS or NOOBS LITE Operating System for beginners announced by the Raspberrypi website but there are many other ones like Windows 10 For IOT, Ubuntu MATE, Pidora, Arch Linux ARM, FreeBSD, etc.

<h2>Kernel building</h2>

There are two main methods for building the kernel. You can build **locally on a Raspberry Pi**, which will take a long time; or you can **cross-compile**, which is much quicker, but requires more setup.
for us we will use the Cross-compilation.

<h2>Cross-compiling</h2>
Cross-compilation is the process of compiling code for one computer system (often known as the target) on a different system, called the host.
It's a very useful technique, for instance when the target system is too small to host the compiler and all relevant files.


![](https://3.bp.blogspot.com/-FKi3ypBSo_E/WP1Rs3YnsLI/AAAAAAAAB3g/G7cHCBklmf4e2RnPrzs_wz2x-OvF1yZUwCLcB/s640/cross001.png )

<h2>What is a Build Toolchain</h2>
Toolchain is a set of programming tools that is used to perform a complex software development task or to create a software product, which is typically another computer program or a set of related programs. 

<h3>Toolchain Examples</h3>
The most common toolchain is GNU toolchain produced by the GNU Project and used for developing software applications and operating systems including Linux, BSD, Windows, Solaris, macOS, etc.
 
Projects included in the GNU toolchain are:

**GNU make:** an automation tool for compilation and build

**GNU Compiler Collection (GCC):** a suite of compilers for several programming languages

**GNU C Library (glibc):** core C library including headers, libraries, and dynamic loader

**GNU Binutils:** a suite of tools including linker, assembler and other tools

**GNU Bison:** a parser generator, often used with the Flex lexical analyser

**GNU m4:** an m4 macro processor

**GNU Debugger (GDB):** a code debugging tool

**GNU build system (autotools):** Autoconf, Automake and Libtool


![](https://4.bp.blogspot.com/-s5a95TIc7ew/Vvkt7I5kC7I/AAAAAAAALRQ/1ER34SUMt9w46BVOaM7BNr7osotzpMRiQ/s1600/CrossCompile.png)


<h2>Why Kernel compilation</h2>
After kernel compilation, a file named **Module.symvers** will be generated that contains all exported symbols from vmlinux and all modules and other issues like **CRC (cyclic redundancy check)**. When we compile a new kernel module, this file and many other intermediates are needed.
After kernel compilation, an image file named **Image** and a compressed image named **zImage** will be created too in **arch/arm/boot/**, but they are not needed in our process.

<h3>What is the difference between the image generated and the final image</h3>
If you compile the same version without changing anything, you will get the same image just you have to convert this image to a **kernel.img** file using this command: **"python imagetool-uncompressed.py path/to/linux/arch/arm/boot/Image"**.
A boot image is a computer file containing the complete contents and structure of a Computer storage media. When it is transferred onto a boot device it allows the associated hardware to boot.

<h3>Why we can not use a compiled image directly</h3>

**Module.symvers** is not existed in Linux root directory and we must recompile the kernel to get it.  

Create a your module.c and your Makefile by adding compiler and source path, build it, send the .ko generated module to Raspberry PI to insert it using the command **insmod**


<h2>Sources</h2>

[ Getting Started with Raspberry Pi]( https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started)

[Steps of cross compilation of the raspberry pi](https://www.raspberrypi.org/documentation/linux/kernel/building.md)