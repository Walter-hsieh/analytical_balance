import time
import serial
import matplotlib.pyplot as plt
import keyboard

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
    data = []
    plt.ion()
    # time.sleep(5)       # wait one second before requesting for next point
    while i <100:     # decide how many points you want to collect
        out = ser.read(12).decode()     # read data from balance
        f.write(out)
        print(out)

        out1 = out.replace(' ', '')     # remove space
        out2 = out1.replace('g', '')    # remove string
        data.append(float(out2))        # turn string into float

        plt.plot(data, 'r-o')
        plt.draw()
        plt.pause(0.0001)
        plt.clf()


        i+=1

    f.close()



# 參考程式
# plt.ion()
# for i in range(50):
#     y = np.random.random([10,1])
#     plt.plot(y)
#     plt.draw()
#     plt.pause(0.0001)
#     plt.clf()




# backup code
# ------------------------------------------
# command = b'D01\r\n'
# ser.write(command) 
# out = ser.read(12).decode()
# print(out)
# ------------------------------------------

# Using while loop to set how many point of data to acquire
# with open('test.txt', 'w') as f:
#     i=0
#     while i < 10:
#         out = ser.read(12).decode()
#         f.write(out)
#         print(out)
#         i+=1
#     f.close()
# ------------------------------------------
# keyboard.press('alt')
# keyboard.press('f4')
# keyboard.release('f4')
# keyboard.release('alt')
