import serial
ser=serial.Serial('/dev/ttyAMA0')
while True:
  #  print('not 0')
    data=ser.readline()
    line=data
    print line
