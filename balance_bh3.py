import time
import serial
import matplotlib.pyplot as plt
import datetime


# 與設備通訊
ser = serial.Serial(
    port='COM5',
    baudrate=600,
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


# # ---------test ------------------
# sample_name = input("Enter the sample name: ")
# filename = sample_name + '_sec.txt'

# with open(filename,'w') as f:
#     f.write("program created by Walter!\n")
#     f.close()

# while True:
#     recorder = open(filename,'a')
#     # ser.write('%RW\r'.encode('utf-8'))
#     out = ser.read(15).decode('utf-8')
#     data = out.replace(" ", "").replace("g","").replace("+","")
#     recorder.write(data)
#     print(data)
# # ---------test ------------------

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
    f.write("program created by Walter!\n")
    f.close()

while True:
    recorder = open(filename,'a')
    # countdown(t)
    # ser.write('D05\r'.encode('utf-8'))
    out = ser.read(15).decode('utf-8')
    # print(f"{datetime.datetime.now()} {out}")
    out_new = out.replace(" ", "").replace("g","").replace("+","") #移除+, 空格與文字g
    recorder.write(f"{datetime.datetime.now()} {out_new}")
    # recorder.write(out_new)
    recorder.close()

    # data.append(out_new)
    data.append(float(out_new))
    plt.plot(data, marker=".", linestyle="-")
    plt.draw()
    plt.pause(0.0001)
    plt.savefig(filename.replace('txt', 'png'))
    plt.clf()

# Reminder: restart the balance before taking any measurement in case the conflict from previous data