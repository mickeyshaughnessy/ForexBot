
# This script implements a Naive Bayes classifier and 
# a simple buy low sell high strategy for forex trading in two currencies.
# It implements an automated test suite, using the yearly training data.
# It is restricted to a single trade per day and will always cease trading

from make_train_test import *
import sys


def generate_test(year):
    pass    

if __name__ == '__main__':
    EX = sys.argv[1]
    with open(EX) as EX_data:
        raw_data = EX_data.readlines()
    (first, last) = (raw_data[0].split(','), raw_data[-1].split(','))
    (first, last) = (convert_date(first[0]), convert_date(last[0]))
    

threshold = 0.6
risk_prcnt = 0.1

'''    
    for (test, train) in data:
        train(train)
        test(test)

    def train(train):
        p(A | B) = p(B | A) * p(A) / p(B)
        p(rise | last_n) = p(last_n | rise) * p(rise) / p(last_n)
        
        compute_tables()

    def test(test):
        A = 1000
        B = 1000
        for day in test:
            rise = compute_table(day, rise) 
            drop = 1 - rise 
        
        if rise > threshold:
            # trade risk_prcnt of currency A into currency B
             
        elif drop > threshold:
            # trade risk_prcnt of currency B into currency A
'''


#raw_data = raw_data.split(',')
#        print raw_data
#        first = raw_data
#    for year in range(data):
#        with open('test.csv') as test_file:
#            test_data = test_file.readlines()
#        with open('train.csv') as train_file:
#            train_data = train_file.readlines()
    
    # train classifier
      


    tests = []  # percent profit in year x
    
    # for day in test_data:
    #   test() 
