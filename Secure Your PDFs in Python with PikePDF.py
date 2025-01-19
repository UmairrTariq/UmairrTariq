import pikepdf
input_pdf_path = r"C:\Users\ma\Downloads\PDF.pdf"
output_pdf_path = r'C:\Users\ma\Downloads\PDF1.pdf'

user_pass = input("Enter the password to encrypt PDF: ")
try:
    with pikepdf.Pdf.open(input_pdf_path) as pdf:
        pdf.save(output_pdf_path,encryption=pikepdf.Encryption(owner=user_pass,user=user_pass))
        print(f'The PDF has been encrypted successfully! Saves as {output_pdf_path}')
except FileNotFoundError:
    print('Error: The specified PDF file was not found')
except pikepdf._qpdf.PasswordError:
    print('Error: the file could not be encrypted due to an incorrect password.')
except Exception as e:
    print(f'An Error Occured : {e}')

