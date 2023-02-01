import PyPDF2
import os

folder = 'Data/'
for filename in os.listdir(folder):
    # Open the PDF file in binary mode, "rb" is read-binary
    file = open(folder+filename, "rb")
    # Read binary into PDF system,
    pdf = PyPDF2.PdfReader(file)

    # Iterate over every page in the PDF
    with open('Output/' + filename + '.txt', "w") as text_file:
        for page_number in range(len(pdf.pages)):
            TextInPage = pdf.pages[page_number].extract_text()
            text_file.write(TextInPage)
