import qrcode

# Function to create a QR code and save it as an image
def create_qr_code(content, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(content)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Name card information
name = "Supportive"
age = 18
occupation = "High school student"
location = "Jinju"

# Format the content as a string
content = f"Name: {name}\nAge: {age}\nOccupation: {occupation}\nLocation: {location}"

# File name for the QR code image
filename = "name_card_qr_code.png"

# Generate and save the QR code
create_qr_code(content, filename)
print(f"QR code has been created and saved as '{filename}'")
