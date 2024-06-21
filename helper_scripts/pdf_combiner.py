import os
from PyPDF2 import PdfMerger

def combine_pdfs(input_folder, output_name):
    # Create a PdfMerger object
    merger = PdfMerger()

    # Loop through the numbered PDF files from 01 to 17
    for i in range(1, 18):
        # Create the filename with zero-padded number
        filename = f"{i:02d}.pdf"
        file_path = os.path.join(input_folder, filename)

        # Check if the file exists
        if os.path.exists(file_path):
            # Append the PDF to the merger
            merger.append(file_path)
        else:
            print(f"Warning: File {filename} not found.")

    # Create the output folder if it doesn't exist
    output_folder = os.path.join(input_folder, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Create the full output file path
    output_file = os.path.join(output_folder, f"{output_name}.pdf")

    # Write the combined PDF to the output file
    with open(output_file, "wb") as output:
        merger.write(output)

    print(f"Combined PDF saved as {output_file}")

# Get user input
input_folder = input("Enter the path to the folder containing the PDF files: ")
output_name = input("Enter the name for the combined PDF file (without .pdf extension): ")

combine_pdfs(input_folder, output_name)