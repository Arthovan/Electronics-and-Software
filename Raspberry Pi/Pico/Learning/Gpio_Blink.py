import machine	# moudle to use the ports and pins
#-------------- GPIO
onboard_led = machine.Pin(25,machine.Pin.OUT)
while True:
    onboard_led.value(1)
    utime.sleep(2)
    onboard_led.value(0)
    utime.sleep(2)