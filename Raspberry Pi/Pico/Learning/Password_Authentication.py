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
    
secret_key :list[str] = ['1','9','0','5','3','7']
entered_key :list[str] = []
key_count :int = 0
val = True
    
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

led = Pin(17,Pin.OUT,Pin.PULL_DOWN)
    
########################### Scan Keys ###########################
print("Enter the 6 digit passcode ")
def scan_keys():
    global key_count
    for row in range(4):
        row_pins[row].high()
        for col in range(3):   
            if column_pins[col].value() == 1:
                #print("You have pressed: ", matrix_keys[row][col])
                entered_key.append(matrix_keys[row][col])
                print(entered_key[key_count],end='')
                utime.sleep(0.3)
                key_count += 1
                    
        row_pins[row].low()                    
        if key_count == 6:
            verify_Password()
            break        
        
def verify_Password():
    secret_count :int = 0
    global entered_key
    global key_count
    global val
    for loop in range(0,6):
        if secret_key[loop] == entered_key[loop]:
            secret_count += 1
    if secret_count == 6:
        print("\nAuthorised Successfully")
        led.value(1)
        utime.sleep(3)
        led.value(0)
        entered_key.clear()
        secret_count = 0
        key_count = 0
        val = False
    else:
        print("\nWrong Password")
        key_count = 0
        secret_count = 0
        entered_key.clear()
                
def main():
    while val:
        scan_keys()
            
if __name__ == '__main__':
    main()
    
        


    