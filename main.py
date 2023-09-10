import qrcode


def create_qrcode(url):
    """
    Function to create qr code and save set of qr images (default and stylized image)
    :param url: URL for which qr code needs to be created
    :return:
    """
    img = qrcode.make("www.google.com")
    img.save("google.png")

    qr = qrcode.QRCode()
    qr.add_data("www.youtube.com")
    img2 = qr.make_image(fill_color="blue", back_color="black")
    img2.save("youtube.png")
