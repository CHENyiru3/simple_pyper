# This file is for reading the inputs (also parameters) and outputs

import re

class pyReader(object):
    def __init__(self, file_path):
        self.file = open(file_path, "r")

    def print_file(self):
        print(self.file.read())

    def count_pattern_in_def(self, pattern):
        self.file.seek(0)
        content = self.file.read()
        defs = re.findall(r'def.*\)', content)
        count = 0
        detailed_list = []
        for parameter in defs:
            matches = re.findall(pattern, parameter)
            count += len(matches)
            detailed_list = detailed_list + (matches)

        return (len(defs), count, detailed_list)




