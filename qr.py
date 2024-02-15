import qrcode

img = qrcode.make('your_site_url')

img.save('qrcode_image_name')
