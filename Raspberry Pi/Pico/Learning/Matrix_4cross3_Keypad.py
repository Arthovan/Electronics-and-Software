"""--------------------- Modules Import --------------"""
from machine import Pin	# have to access everything like basic == 2 
import utime	# module to create a delay
        
#-------------- Matrix Keypad 4*3
"""	PICO IO		Keypad
    GPIO 2		1 - Row 1
    GPIO 3		2 - Row 2
    GPIO 4		3 - Row 3
    GPIO 5		4 - Row 4
    GPIO 6		5 - column 1
    GPIO 7		6 - column 2
    GPIO 8		7 - column 3	"""
    
# Create a map between keypad buttons and characters
matrix_keys :list[str] = [['1', '2', '3'],
                         ['4', '5', '6'],
                         ['7', '8', '9'],
                         ['*', '0', '#']]
    
# PINs according to schematic - change the pins to match with your connections
# Only used for setting the PINs as output or input
keypad_rows :list[int]		= [2,3,4,5]
keypad_columns :list[int]	= [6,7,8]
    
#create a empty lists to setup pins (Rows o/p and colum o/p)
row_pins :list[int] = []
column_pins :list[int] = []
    
# Loop to assign GPIO pins and setup I/O
for x in range(0,4):
    row_pins.append(Pin(keypad_rows[x], Pin.OUT))
        
for x in range(0,3):
    column_pins.append(Pin(keypad_columns[x], Pin.IN, Pin.PULL_DOWN))
    
########################### Scan Keys ###########################
print("Enter the 6 digit passcode ")
def scan_keys():
    for row in range(4):
        row_pins[row].high()
        for col in range(3):           
            if column_pins[col].value() == 1:
                print("You have pressed: ", matrix_keys[row][col])
                utime.sleep(0.3)
                    
        row_pins[row].low()                           
    
def main():
    while True:
        scan_keys()
            
if __name__ == '__main__':
    main()
    
        


    
