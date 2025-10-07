import qrcode

def generate_qrcode(text):
    qr_obj = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr_obj.add_data(text)
    qr_obj.make(fit=True)

    img = qr_obj.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

# Example: create a QR code for a website
generate_qrcode("https://www.google.com")


