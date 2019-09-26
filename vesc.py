import pyvesc
# make a SetDutyCycle message
my_msg = pyvesc.SetDutyCycle(1e5)
print(my_msg.duty_cycle) # prints value of my_msg.duty_cycle
my_packet = pyvesc.encode(my_msg)
# my_packet (type: bytes) can now be sent over your UART connection
