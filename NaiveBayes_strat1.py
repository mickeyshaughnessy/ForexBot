
# This script implements a Naive Bayes classifier and 
# a simple buy low sell high strategy for forex trading in two currencies.
# It implements an automated test suite, using the yearly training data.
# It is restricted to a single trade per day and will always cease trading

from make_train_test import *
import sys
from random import choice
from make_train_test import *
from collections import deque
from datetime import datetime

threshold = 0.6 # Probability threshold for acting
risk_prcnt = 0.05 # How much of total account to risk on any one day
N_tests = 10 # testing years
N_lookback = 2 # time steps 
Lambda = 5 # days


def run_simulation():
    train = open('train.csv', 'r')
    train = train.readlines()
    test = open('train.csv', 'r')
    test = test.readlines()
 
#####  compute training results #####
    results = {}
    pattern = deque([])
    n = 0
    last = train[n][1]
    while last.rstrip() == '.':
        n += 1
        last = train[n][1]
    last = float(last.rstrip())
    
    for day in train[n+1:]:
        pair = day.split(',')
        if pair[1].rstrip() != '.':
            cur = float(pair[1].rstrip()) 
            change = cur - last
            if change != 0:
                last = cur
                pattern.appendleft(cmp(change,0))
        if len(pattern) > N_lookback:
            if tuple(pattern) in results.keys():
                results[tuple(pattern)] += 1
            else:
                results[tuple(pattern)] = 1
            pattern.pop()
    print results
#### run simulation ####

    USD = 100
    X = 0
    current = deque([])
    
    last = test[n][1]
    while last.rstrip() == '.':
        n += 1
        last = train[n][1]
    last = float(last.rstrip())
    
    for day in test[n+1:]:
        pair = day.split(',')
        if pair[1].rstrip() != '.':
            cur = float(pair[1].rstrip()) 
            USD += X * cur
            X = 0
            change = cur - last
            if change != 0:
                last = cur
                current.appendleft(cmp(change,0))
            if len(current) > N_lookback:
                print type((1,)+tuple(current))
                print type( tuple(current))
                n_rise = results.get((1,)+tuple(current[1:]))
                n_drop = results.get((-1,)+tuple(current[1:]))
                current.pop()    

#print tuple(current)    
                current.pop()
 #   compute_probs(results)

def compute_probs(results):
    # p(A | B) = p(B | A) * p(A) / p(B)
    table = {}
    for pattern in results:
        prev = pattern[1:]
        rise = results[(1,)+prev]
        drop = results[(-1,)+prev]
#print ('%s, p_rise: %s' % (pattern, float(rise)/(rise+drop)))
#print pattern
#        print results[pattern]

#p_rise 
    #p(rise | last_n) = p(last_n | rise) * p(rise) / p(last_n)
    


def analyze():
    pass
def generate_test_day(first, last, EX):
    (start_year, start_month, start_day) = ( 
        choice(range(int(first[0])+1, int(last[0])-1)),
        choice(range(1,13)),
        choice(range(1,29))
        )
    make_test(dt.date(start_year, start_month, start_day),
                    dt.date(start_year+1, start_month, start_day), EX)

def generate_test_min(first, last, EX):
    print first[0:4]
    print last[0:4]
    (start_year, start_month, start_day, start_hour, start_min) = ( 
        choice(range(int(first[0:4])+1, int(last[0:4])-1)),
        choice(range(1,13)),
        choice(range(1,29)),
        choice(range(1,23)),
        choice(range(1,59))
        )
    start = dt.datetime(start_year, start_month, start_day, start_hour, start_min) 
    end = dt.datetime(start_year+1, start_month, start_day, start_hour, start_min) 
    make_test(start, end, EX)

if __name__ == '__main__':
    EX = sys.argv[1]
    with open(EX) as EX_data:
        raw_data = EX_data.readlines()
        (first, last) = (raw_data[0].split(','), raw_data[-1].split(','))

    data = []
    for year in range(0, N_tests):
        #generate_test_day(first[0].split('-'), last[0].split('-'), EX)
        generate_test_min(first[1], last[1], EX)
        run_simulation()
        analyze() 

    # generate N_tests 1-year intervals (starting at a random date) for testing
    # use the rest of the data for training.

    # The general strategy is to decide whether to buy or sell USD_to_X on a given day. 
    # The total volume to buy or sell is a fixed percentage of the total portfolio.
    # Because there is a fixed commision in terms of percent of transaction (0.01% of transaction)
    # This is also accounted for. 

    # At time t, the feature vector is the last n exchange rate changes, binned according to size.

    # The output of the A predictor is a ranked list of currencies, ranked according to the probability
    # that the value of the currency will rise.

    # The output of the B predictor is a measure for each currency of the predicted change in value. 

    # Both A and B are combined to make a decision for the next day - all of the predicted least 
    # valuable currency is 

    
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
