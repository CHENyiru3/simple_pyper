import csv
from typing import NewType

file_path = NewType('file_path', str)

def csv_to_tsv(input_csv_file_path: file_path, output_tsv_file_path: file_path):
    with open(input_csv_file_path, 'r') as csv_file, open(output_tsv_file_path, 'w', newline='') as tsv_file:
        csv_reader = csv.reader(csv_file)
        tsv_writer = csv.writer(tsv_file, delimiter='\t')
        for row in csv_reader:
            tsv_writer.writerow(row)

def main(input_csv_file_path: file_path, output_tsv_file_path: file_path):
    csv_to_tsv(input_csv_file_path, output_tsv_file_path)

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])