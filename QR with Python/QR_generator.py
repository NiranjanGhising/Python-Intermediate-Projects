import pyqrcode

#input from user to generate QR of their Link.
text = input("enter the link, to generate the QR of it: ")

#calling create method, using text as argument.
QR_code = pyqrcode.create(text)

#calling svg method.
#create a file named QR_code.svg in svg format
#scale argument sets how large the pic should be.
QR_code.svg('QR_code.svg', scale=8)

