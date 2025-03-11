import qrcode
import cv2
from pyzbar.pyzbar import decode

def generate_qr_code(link, output_file="qrcode.png"):
    """Generates a QR code from a given link."""
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(output_file)
    print(f"QR code generated and saved as {output_file}")

def decode_qr_code(image_path):
    """Decodes a QR code from an image file."""
    image = cv2.imread(image_path)
    decoded_objects = decode(image)
    
    if decoded_objects:
        for obj in decoded_objects:
            print(f"Decoded QR Code: {obj.data.decode('utf-8')}")
    else:
        print("No QR code found in the image.")

def main():
    choice = input("Do you want to generate (G) or decode (D) a QR code? ").strip().lower()
    if choice == "g":
        link = input("Enter the link to generate a QR code: ").strip()
        output_file = input("Enter the output file name (default: qrcode.png): ").strip() or "qrcode.png"
        generate_qr_code(link, output_file)
    elif choice == "d":
        image_path = input("Enter the path of the QR code image: ").strip()
        decode_qr_code(image_path)
    else:
        print("Invalid choice. Please enter 'G' to generate or 'D' to decode.")

if __name__ == "__main__":
    main()
