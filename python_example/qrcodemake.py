import qrcode

# Function to create a QR code and save it as an image
def create_qr_code(content, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(content)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Replace 'ADDRESS_HERE' with the actual address of Jinjuseong
address = "ADDRESS_HERE"

# File name for the QR code image
filename = "jinjuseong_address_qr_code.png"

# Generate and save the QR code
create_qr_code(address, filename)
print(f"QR code for Jinjuseong address has been created and saved as '{filename}'")

