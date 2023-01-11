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


sample_name = input("Enter the sample name: ")
t = int(input("Enter time in second: "))

# 倒數時間/模組
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


# 數據讀取/作圖/儲存
data = []
filename = sample_name + '_' +str(t) + '_sec.txt'

with open(filename,'w') as f:
    f.write("Welcome!\n")
    f.close()

while True:
    recorder = open(filename,'a')
    countdown(t)
    ser.write('D05\r'.encode('utf-8'))
    out = ser.read(12).decode('utf-8')
    recorder.write(out)
    print(out)
    recorder.close()

    data.append(float(out.replace(' ','').replace('g',''))) #移除空格與文字g

    plt.plot(data, 'b-o')
    plt.draw()
    plt.pause(0.0001)
    plt.savefig(filename.replace('txt', 'png'))
    plt.clf()

