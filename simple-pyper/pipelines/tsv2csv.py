import csv
from typing import NewType
 
file_path = NewType('file_path', str)
def tsv_to_csv(inputas_tsv_file_path, outputas_csv_file_path):
    with open(inputas_tsv_file_path, 'r') as tsv_file, open(outputas_csv_file_path, 'w', newline='') as csv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        csv_writer = csv.writer(csv_file)
        for row in tsv_reader:
            csv_writer.writerow(row)

def main(inputas_tsv_file_path:file_path, outputas_csv_file_path:file_path):
    tsv_to_csv(inputas_tsv_file_path, outputas_csv_file_path)

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])