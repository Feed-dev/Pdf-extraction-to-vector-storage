import os
from PyPDF2 import PdfMerger


def combine_pdfs(input_folder, output_name):
    # Create a PdfMerger object
    merger = PdfMerger()

    # Get all PDF files in the input folder
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]

    # Sort the PDF files alphabetically
    pdf_files.sort()

    # Loop through the sorted PDF files
    for filename in pdf_files:
        file_path = os.path.join(input_folder, filename)

        # Append the PDF to the merger
        merger.append(file_path)
        print(f"Added: {filename}")

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