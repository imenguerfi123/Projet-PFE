<center><h1 style="color: #ff0000">Design and Development of a Smart Card Hub with Raspberry PI</h1></center>


<h2>General description of the subject</h2>

The main goal is to design and develop a python server that offers REST web services to control a smart card hub connected to the raspberry pi via a HAT (Hardware Attached on Top) expansion card.

The server must offer REST APIs which ensure the multiplexing of smart cards connected to payment terminals..

This server must be integrated into an automatic test environment to launch the execution of test suites with the card hub. Hence the possibility of launching several automatic tests at the same time on several smart cards will be feasible.

<h2> block diagram</h2>

<img src="schema-bloc1.PNG">

<h2>Detailed Description of The Subject</h2>

The block diagram of our project includes a raspberry pi card (RPI) and a HAT extension card (hardware Attached on Top) which is equipped with an EEPROM memory, and it is connected with RPI via GPIOs.

In order to ensure multiplexing of smart cards with payment terminals, we will use a multiplexer and an FPGIA card.

Our FPGA is connected to the multiplexer selection pins. The multiplexer is the one that will do the multiplexing between the cards and the terminals.

First we will load the firmware into the FPGA card from the RPI, i.e. there is a binary that will be compiled and transferred to FPGA and it was done from the configuration pins ((SPI) Serial Peripheral Interface), it's at the linux kernel level.

Secondly at the application level we will develop a web server which must offer REST APIs which ensure the multiplexing of cards through the sending of commands via the serial link using UART (Universal Asynchronous Receiver / Transmitter).