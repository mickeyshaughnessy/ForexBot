
# This script implements a Naive Bayes classifier and 
# a simple buy low sell high strategy for forex trading in two currencies.
# It implements an automated test suite, using the yearly training data.
# It is restricted to a single trade per day and will always cease trading

from make_train_test import *
import sys
from random import choice

threshold = 0.6
risk_prcnt = 0.05
N_tests = 10

def generate_test(year, first, last):
    (start_year, start_month, start_day) = ( 
        choice(range(int(first[0])+1, int(last[0])-1)),
        choice(range(1,13)),
        choice(range(1,29))
        )
    #print ('%s, %s, %s', start_year, start_month, start_day) 
    
    pass    

if __name__ == '__main__':
    EX = sys.argv[1]
    with open(EX) as EX_data:
        raw_data = EX_data.readlines()
    
    (first, last) = (raw_data[0].split(','), raw_data[-1].split(','))
    dt_range = (convert_date(first[0]), convert_date(last[0]))

#    print choice(range(int(first[0].split('-')), last[0].split['-']))

    data = []
    for year in range(0, N_tests):
        data.append(generate_test(year, first[0].split('-'), last[0].split('-')))
    # generate 10 1-year intervals (starting at a random date) for testing
    # use the rest of the data for training.

    # The general strategy is to decide whether to buy or sell USD_to_X on a given day. 
    # The total volume to buy or sell is a fixed percentage of the total portfolio.
    # Because there is a fixed commision in terms of percent of transaction (0.01% of transaction)
    # This is also accounted for. 

    # At time t, the feature vector is the last n exchange rate changes, binned according to size.


    
                    #    for (test, train) in data:
                    #        train(train)
                    #        test(test)
                    #
                    #    def train(train):
                    #        p(A | B) = p(B | A) * p(A) / p(B)
                    #        p(rise | last_n) = p(last_n | rise) * p(rise) / p(last_n)
                    #        
                    #        compute_tables()
                    #
                    #    def test(test):
                    #        A = 1000
                    #        B = 1000
                    #        for day in test:
                    #            rise = compute_table(day, rise) 
                    #            drop = 1 - rise 
                    #        
                    #        if rise > threshold:
                    #            # trade risk_prcnt of currency A into currency B
                    #             
                    #        elif drop > threshold:
            # trade risk_prcnt of currency B into currency A


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
