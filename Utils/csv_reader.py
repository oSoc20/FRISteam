import csv
from Utils.fris_entities import Keyword

'''
 Read a csv file and returns a list of Keyword objects
 
 :parameter file_name the csv file to read
 :return list of Keyword objects
'''
def read(file_name):
    keywords = []
    with open(file_name, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                keywords.append(Keyword(row[0], row[1], row[2]))
                line_count += 1
        print(f'Processed {line_count} lines.')
    return keywords


def read(file_name, language):
    keywords = []
    with open(file_name, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[1] == language:
                    keywords.append(Keyword(row[0], row[1], row[2]))
                    line_count += 1
        print(f'Processed {line_count} lines.')
    return keywords


