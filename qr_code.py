import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)
# data = input("Enter the url you want as a QR code: ")
qr.add_data("https://www.youtube.com/watch?v=AMTUrsaRzxY")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")