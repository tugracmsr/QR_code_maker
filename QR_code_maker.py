import pyqrcode
import os

while True:
    try:
        size = int(input("Size(Defult 8):"))
        if size<=0:
            print("Enter a number higher than zero.")
        else:
            break
    except ValueError:
        print("Enter a number.")
try:
    pyqrcode.create(input("Text to be QR code:")).svg("QR_code.svg",scale = size)
except ValueError:
    print("The data will not fit in any QR code version.")
os.system("QR_code.svg")
