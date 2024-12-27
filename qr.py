import qrcode

def generate_qr_code(link, output_file="qrcode.png"):
    """Generates a QR code from a given link."""
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(output_file)
    print(f"QR code generated and saved as {output_file}")

def main():
    link = input("Enter the link to generate a QR code: ").strip()
    output_file = input("Enter the output file name (default: qrcode.png): ").strip() or "qrcode.png"
    generate_qr_code(link, output_file)

if __name__ == "__main__":
    main()
