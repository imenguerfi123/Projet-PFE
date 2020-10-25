<center><h1 style="color: #ff0000">Device Tree</h1></center>


<h2>Definition</h2>
A device tree is a tree data structure with nodes that describe the physical devices on the board. While using device tree, kernel no longer contains the description of the hardware, it is located in a separate binary blob called the device tree blob. 

The device tree is passed to the kernel at boot time. Kernel reads through it to learn about what kind of system it is and what drivers to be loaded. So on the change of board only developer needs to change device tree blob and that it new port of kernel is ready.


![](https://raw.githubusercontent.com/robbie-cao/repo-diagrams/master/linux/Linux-Device-Tree-Workflow.png)


<h2>Device tree basics</h2>
Each driver or a module in the device tree is defined by the node and all its properties are defined under that node. Based on the driver it can have child nodes or parent node.

For example a device connected by SPI bus will have SPI bus controller as its parent node and that device will be one of the child node of spi node. Root node is the parent for all the nodes.

Under the root node typically consists of

1) CPUs node information

2) Memory information

3) Chosen can have configuration data like the kernel parameters string and the location of an initrd image

4) Aliases

5) Nodes which define the buses information

![](https://octavosystems.com/octavosystems.com/wp-content/uploads/2018/05/Figure-1-Block-diagram-of-a-simple-device-tree-structure.png)



![](https://images.slideplayer.com/25/8097490/slides/slide_53.jpg)


Device Tree files are not monolithic, they can be split in
several files, including each other.

 - **.dtsi files** are included files, while .dts files are final Device
Trees Typically, .dtsi will contain definition of SoC-level
information (or sometimes definitions common to several
almost identical boards).

 -  **The .dts file** contains the board-level information.

 - The compiled binary format is referred to as Flattened Device Tree (FDT) or Device Tree Blob (DTB), and is stored in **.dtb files.**

<h2>Device Tree Objective</h2>

Traditionally, the specific hardware configurations are described in so called board-description files and permanently embedded into the kernel during compilation. Kernel sources are then expanded according to the number of files needed. Furthermore modern ARM architectures use pins for multiple purposes. With multiplexing, a pin may e.g- work as GPIO or as part of a I2C or a SPI interface. Thus board files have to be added at compilation time and cannot be modified afterwards. For changing the pin assignment it is necessary to re-compile the kernel.

The Device Tree is supposed to revolutionize this. Its idea is to read the hardware configuration from a data structure stored in RAM at startup. So it is possible to run one kernel on multiple development boards, just by swapping the data structure

<h2>Device Tree overlays</h2>
A modern SoC (System on a Chip) is a very complicated device; a complete Device Tree could be hundreds of lines long. Taking that one step further and placing the SoC on a board with other components only makes matters worse. To keep that manageable, particularly if there are related devices that share components, it makes sense to put the common elements in .dtsi files, to be included from possibly multiple .dts files.

To solve this problem, the device tree overlay (DTO) enables a central device tree blob (DTB) to be overlaid on the device tree. A bootloader using DTO can maintain the SOC DT and dynamically overlay a device-specific DT, adding nodes to the tree and making changes to properties in the existing tree.

<h2>FPGA programming using Device Tree Overlay (DTO)</h2>

The Device Tree Overlay (DTO) is used to reprogram an FPGA while Linux is running. The DTO overlay will add the child node and the fragments from the **.dtbo file** to the base device tree,

The newly added device node/drivers will be probed after bitstream programming

DTO contains:
<h3>Target FPGA Region</h3>

- "target-path" or "target" : The insertion point where the contents of the overlay will go into the live tree.

- target-path is a full path, while target is a phandle.

<h3>FPGA Image firmware file name</h3>

- "firmware-name" : Specifies the name of the FPGA image file on the firmware search path.
The search path is described in the firmware class documentation.

<h3>Image specific information</h3>

- external-fpga-config : boolean, set if the FPGA has already been configured prior to Linux boot up.

<h3>Child devices</h3>
- Child nodes corresponding to hardware that will be loaded in this region of the FPGA.


<h2>DT overlays process</h2>
In this paragraph we will talk about Device tree creations steps and all commands needed to know.

Create a device tree source file
This a sample Device tree source for a specific device that use SPI bus with dtsi extension:  

The device contains many nodes, and each node is interfacing with specifics bus.

<h2>Device Tree Compilation</h2>

After Creating our Device tree source (human readable format), we have to compilate it into a dtbo blob device tree file (binary file understandable by kernel).
So initially, we have to install dtc compiler by entering this command line :

                     sudo apt-get install device-tree-compiler

After that, we can compile our source file by this command : 

                     sudo dtc -@ -O dtb -o file.dtbo -b O file.dts
The inverse compilation way is also permitted by recovering the source file from binary.

                      sudo -I dtb -O dts -o file.dts file.dtbo  

Allowing device tree overlay to be loaded from boot process
Allowing device tree overlay to be loaded from boot process steps are simply moving the dtbo file into **/boot/overlays** and adding dtoverlay **dt_file_name.** 

<h3>Manually adding device tree</h3>

To add your device tree manually without booting the Raspberry PI you can simply use the command  

                         sudo dtoverlay file.dtbo

dtoverlay have many other functionalities like removing an overlay, listing loaded ones, getting the overlay information, etc.

You can read the help to find these functionalities 

                              dtoverlay -h
 
This picture explains the Device Tree Process :

![](https://source.android.com/devices/architecture/images/treble_dto_bootloader.png)


<h2>Sources</h2>

[Device Trees, overlays, and parameters](https://www.raspberrypi.org/documentation/configuration/device-tree.md)

[Documentation-devicetree-bindings](https://elixir.bootlin.com/linux/latest/source/Documentation/devicetree/bindings)