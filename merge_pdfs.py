from PyPDF2 import PdfReader, PdfWriter
import os

def merge_pdfs(input_paths, output_path):
    """
    Merge PDFs in input_paths into a single PDF and save to output_path
    """
    writer = PdfWriter()
    # Get the list of input PDFs sorted by their creation time
    sorted_paths = sorted(input_paths, key=lambda path: os.path.getctime(path))
    for path in sorted_paths:
        with open(path, 'rb') as pdf_file:
            reader = PdfReader(pdf_file)
            # Merge all pages of the current PDF into the output PDF
            for page_num in range(len(reader.pages)):
                writer.add_page(reader.pages[page_num])
    with open(output_path, 'wb') as output:
        writer.write(output)

# Get input directory from user
input_dir = input("Enter input directory path: ")

# Get PDF files from input directory
pdf_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.pdf')]

# Print list of PDF files found
print("PDF files found:")
for f in pdf_files:
    print(f)

# Get output file name from user
output_name = input("Enter output file name: ")
output_path = os.path.join(input_dir, output_name)

# Merge PDF files and save to output path
merge_pdfs(pdf_files, output_path)

print(f"PDF files merged and saved to {output_path}")
