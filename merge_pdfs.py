from PyPDF2 import PdfReader, PdfWriter
import os

def merge_pdfs(input_paths, output_path, order):
    """
    Merge PDFs in input_paths into a single PDF and save to output_path
    """
    writer = PdfWriter()
    # Create a list of input PDFs based on the desired order
    pdfs = []
    for num in order:
        pdfs.append(input_paths[num - 1])
    for path in pdfs:
        with open(path, 'rb') as pdf_file:
            reader = PdfReader(pdf_file)
            # Merge all pages of the current PDF into the output PDF
            for page_num in range(len(reader.pages)):
                writer.add_page(reader.pages[page_num])
    with open(output_path, 'wb') as output:
        writer.write(output)

input_dir = "PDFS"

# Get PDF files from input directory
pdf_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.pdf')]

# Print list of PDF files found with numbers
print("PDF files found:")
for i, f in enumerate(pdf_files, start=1):
    print(f"{i} -> {f}")

# Get desired order from user
order_input = input("Enter the desired order (e.g., 1-5, 5-1, 1,2,3,4,5, 5,4,3,2,1, 1,3,2,4,5).\nEnter: ")
order_parts = order_input.split(',')
order = []
for part in order_parts:
    if '-' in part:
        start, end = map(int, part.split('-'))
        order.extend(range(start, end + 1))
    else:
        order.append(int(part))

# Get output file name from user
output_name = input("Enter output file name (without .pdf): ") + '.pdf'
output_path = os.path.join(input_dir, output_name)

# Merge PDF files and save to output path
merge_pdfs(pdf_files, output_path, order)

print(f"PDF files merged and saved to {output_path}")
