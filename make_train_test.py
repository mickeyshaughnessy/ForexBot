

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
    if len(date) == 3:
        return dt.date(date[0], date[1], date[2])
    elif len(date) == 5:
        return dt.datetime(date[0], date[1], date[2], date[3], date[4])

def make_test(START, END, EX_file):
    # This function takes an exchange rate file
    # and start and end dt objects and generates
    # a test / train csv pair. 
    train = open('train.csv', 'w')
    test = open('test.csv', 'w')

    with open(EX_file, 'r') as infile:
        if 'day' in EX_file:
            for line in infile.readlines():
                (date, rate) = line.strip().split(',')
                date = date.split('-')
                date = [int(x) for x in date]
                date = dt.date(date[0], date[1], date[2])
                if rate != '.':
                    if date < START or date >= END:
                        train.write(line)
                    else:
                        test.write(line)
        else:
            for line in infile.readlines():
                words = line.strip().split(',')
                (date, time, rate) = (words[1], words[2], words[3])
                datetime = dt.datetime(
                    int(date[0:4]), 
                    int(date[4:6]),
                    int(date[6:8]),
                    int(time[0:2]),
                    int(time[2:4])
                )
                if datetime < START or datetime >= END:
                    train.write('%s,%s\n' % (date+time, rate))
                else:
                    test.write('%s,%s\n' % (date+time, rate))
                    


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception('Exactly 3 arguements required.')
    (START, END) = (convert_date(x) for x in [sys.argv[2], sys.argv[3]])
   
    make_test(START, END, sys.argv[1])

