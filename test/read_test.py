from python_reader import pyReader

reader = pyReader(file_path='./example_pipeline/tsv2csv.py')

# 调用print_file方法
reader.print_file()

count = reader.count_pattern_in_def('inputas_(.*?)\,')
print(f" {count} 次")


