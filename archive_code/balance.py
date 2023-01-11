import time
import serial

ser = serial.Serial(
    port='COM3',
    baudrate=1200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
    )

if (ser.isOpen() == 0):
    ser.open()

print('connection succeeded.')



with open('test.txt', 'w') as f:
    i=0
    while i <10:
        out = ser.read(12).decode()
        f.write(out)
        print(out)
        time.sleep(5)
        i+=1
    f.close()




# backup code
# ------------------------------------------
# command = b'D01\r\n'
# ser.write(command)
# out = ser.read(12).decode()
# print(out)
# -------------------------------------------

# Using while loop to set how many point of data to acquire
# with open('test.txt', 'w') as f:
#     i=0
#     while i < 10:
#         out = ser.read(12).decode()
#         f.write(out)
#         print(out)
#         i+=1
#     f.close()

