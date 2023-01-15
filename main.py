import qrcode

data = "https://t.me/nebulawalker_bot"
filename = "site.png"
img = qrcode.make(data)
img.save(filename)