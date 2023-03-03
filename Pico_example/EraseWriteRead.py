from rfid import RFID
import time

reader = RFID() # assuming to use same pins as in table

'''
Code below erases the content of the card/tag,
writes "This is just a test" into it and
prints its content
'''

while True:
  if reader.erase():
    
    reader.write('This is just a test')
    print(reader.read())
    
    reader.printContent()
    break
