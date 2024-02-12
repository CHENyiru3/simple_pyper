import os
from PyPDF4 import PdfFileMerger

def merge_pdfs_in_folder(folder_path, output_pdf_path):
    pdf_merger = PdfFileMerger()

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_merger.append(os.path.join(folder_path, filename))

    pdf_merger.write(output_pdf_path)

def main(folder_path:str, output_pdf_path:str):
    merge_pdfs_in_folder(folder_path, output_pdf_path)

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])