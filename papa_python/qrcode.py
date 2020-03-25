# A Simple QRCode Using Python

import pyqrcode

url = pyqrcode.create("http://sigit-wasis.github.io/")
url.svg('uca-url.svg', scale=8)
print(url.terminal(quiet_zone=1))