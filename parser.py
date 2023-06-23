import csv


class CSVParser:
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.column_labels = None
        self.data = []
    
    def parse(self):
        with open('data/' + self.file_name, 'r') as file:
            csv_reader = csv.reader(file)
            for reader_index, row in enumerate(csv_reader):
                if reader_index == 0:
                    self.column_labels = row
                else:
                    self.data.append([float(r) for r in row])
    
    def print_data(self):
        for label in self.column_labels:
            print(f'{label}', end='|')
        print()
        
        for j, row in enumerate(self.data):
            print(f'{j + 1}: {row}')
