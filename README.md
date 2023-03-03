# RFID-micropython-mfrc522
Simplified (Micro)Python class to access the MFRC522 RFID reader

You are watching a fork from the [original code](https://github.com/danjperron/micropython-mfrc522). 

In this fork I added a class which simplifies access with automated general processes.

## Usage

Put the modules ``mfrc522.py``, ``rfidAccess.py``, ``rfid.py`` to the root of the flash FS on your board. 

I used the following pins for my setup:

| Signal | GPIO ESP8266 | GPIO ESP32 | GPIO WiPy | GPIO Pico | Note                          |
| ------ | ------------ | ---------- | --------- | --------- | ----------------------------- |
| sck    | 0            | 18         | "GP14"    | "GP2"     |                               |
| mosi   | 2            | 23         | "GP16"    | "GP3"     |                               |
| miso   | 4            | 19         | "GP15"    | "GP4"     |                               |
| rst    | 5            | 22         | "GP22"    | "GP0"     |                               |
| cs     | 14           | 21         | "GP14"    | "GP1"     | SDA on most RFID-RC522 boards |
 
Import the file "rfid.py" into your "main.py" file

Then, import from it the class "RFID".

When using it, if you use the same pins as in the table, there is no need to pass any method to the constructor, otherwise set properly all the arguments to match your connections.

The class RFID provides few methods: 

- ``readUid()`` which returns a tuple containing the uid of the red card in three forms (list of integers, integer number, hexadecimal number)

- ``read()`` returns the content of the card, litterally each block

- ``printcontent()`` which prints the content of the cards, both in hexadecimal and ascii form

- ``erase()`` erases the card or tag, returns True if success, otherwise False

- ``write(content: str)`` writes string content into the card in ascii form, returns True if success otherwise False

- ``rewrite(content: str)`` erases the card and writes content, returns True if success otherwise False
