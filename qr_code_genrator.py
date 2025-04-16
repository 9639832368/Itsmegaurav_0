import qrcode as qr
from PIL import Image



img = qr.make("https://github.com/9639832368/Itsmegaurav_0")
img.save("itsmegaurav_0_qr.png")