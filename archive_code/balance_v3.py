import time
import serial
import matplotlib.pyplot as plt
import time

# 與設備通訊
ser = serial.Serial(
    port='COM3',
    baudrate=1200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
    )

# 確認是否連上設備
if (ser.isOpen() == 0):
    ser.open()

state = ser.isOpen()
print('state: ' + str(state))
print('connection succeeded.') 


# 倒數時間/模組
t = int(input("Enter time in second: "))
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


# 數據讀取/作圖/儲存
points = 0
data = []
filename = 'single_' + str(t) + '_sec.txt'
with open(filename,'w') as f:
    while points < 20:
        countdown(t)
        ser.write('D05\r'.encode('utf-8'))
        out = ser.read(12).decode('utf-8')
        f.write(out)
        print(out)

        data.append(float(out.replace(' ','').replace('g',''))) #移除空格與文字g

        plt.plot(data, 'b-o')
        plt.draw()
        plt.pause(0.0001)
        plt.savefig(filename.replace('txt', 'png'))
        plt.clf()
        points += 1

f.close()



# Backup
# while True:
#     command = input('Enter your commands below.\r\nInsert "exit" to leave the application: ')

#     if command == 'exit':
#         ser.close()
#         exit()
#     else:
#         ser.write((command+'C/R').encode('utf-8'))
