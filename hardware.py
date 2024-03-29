import serial.tools.list_ports
import time

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB Serial Device" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return "/dev/ttys005"
if getPort() != "None":
    ser = serial.Serial( port=getPort(), baudrate=115200)
    print(ser)

while True:
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        print(ser.read(bytesToRead).decode("UTF-8"))
    time.sleep(1)
