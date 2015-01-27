

# This script reads a CSV (date, value) exchange rate file
# And prepares it into a pair of testing and training data 
# sets. 

import sys
from random import random
import datetime as dt

IS_RANDOM = False
TEST_FRACT = 0.1

def convert_date(date):
    date = date.split('-')
    date = [int(x) for x in date]
    return dt.date(date[0], date[1], date[2])

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception('Exactly 3 arguements required.')
    (START, END) = (convert_date(x) for x in [sys.argv[2], sys.argv[3]])
    train = open('train.csv', 'w')
    test = open('test.csv', 'w')
    
    with open(sys.argv[1], 'r') as infile:
        for line in infile.readlines():
            if IS_RANDOM:
                if random() < TEST_FRACT:
                    test.write(line)
                else:
                    train.write(line)
            
            else:
                (date, rate) = line.strip().split(',')
                date = date.split('-')
                date = [int(x) for x in date]
                date = dt.date(date[0], date[1], date[2])
                if date < START or date >= END:
                    train.write(line)
                else:
                    test.write(line)
                    

