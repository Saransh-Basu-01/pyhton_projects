import qrcode as qr
from PIL import Image
pic=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=4)
pic.add_data("https://github.com/Saransh-Basu-01")
pic.make(fit=True)
img=pic.make_image(fill_color="red")
img.save("github_qrcode.png")