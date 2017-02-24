## This program will tell how many times Naive-Bayes approach will predicate correctly

## training file: Here is some pre calculated results

## Prediction: Guy will play or not?

## Assumption: Each attribute is independent of all other attributes

## testing file: Read each attribute from every line (separately) from this file .
##               make prediction whether the guy will play or not according to given attributes.
##               compare this result to the correct result

## finally see how many times prediction is correct


from collections import Counter, defaultdict
import re
import sys
import random

def laplacian_smoothing(favorableCases, totalCases, k, totalClass):
    """ 
    P(x) = (count(x) + k) / (N + k*|x|)
      
    where, count(x) is the number of occurrences of this value of the variable x

    |x| is the number of values that the variable x can take on

    k is a smoothing parameter

    N is the total number of occurrences of x in sample size
    """

    numer = favorableCases + k
    denom = totalCases + k*totalClass

    return float(numer / denom)

def classify_bayesian(line, priors, likelihood):
    """ 
    return 'yes' if player is supposed to play according to given attributes in testing file
    or return 'no' if player is not supposed to play.
    """

    # priors have two keywords i.e yes & no
    # conside first keyword as true case & second keyword as false case

    # total number of true cases
    no_ofTrueCases =  priors[priors.keys()[0]]

    # total number of false cases
    no_ofFalseCases = priors[priors.keys()[1]]

    noOfClasses = 0
    
    # count number of coloums in training file
    for x in line:
        noOfClasses += 1

    # extract the frequency of each word in form of dictionary in case of success
    SuccessAtrrFreq = likelihood[likelihood.keys()[0]]

    # extract the frequency of each word in case of failure
    failAttrFreq = likelihood[likelihood.keys()[1]]

    # initilize probalities with 1 
    probOfSuccess = 1
    probOfFail = 1

    # let's find actual probability of each attribute 
    # multiplying the conditional probabilities together for each attribute for a given class value
    for x in line:
        # implement laplacian smoothing for 'fail-safe'
        # let smoothing k = 2
        probOfFail = probOfFail * laplacian_smoothing(failAttrFreq[x], no_ofFalseCases, 2, noOfClasses)
        probOfSuccess = probOfSuccess * laplacian_smoothing(SuccessAtrrFreq[x], no_ofTrueCases, 2, noOfClasses)

    # return either "yes" or "no" on the behalf of above results
    if max(probOfFail, probOfSuccess) == probOfSuccess:
        return likelihood.keys()[0]
    else:
        return likelihood.keys()[1]

def tokenize(text):
    """ Break up text into words """
    return re.findall('[a-z0-9]+', text)

def read_testing_file(filename):
    listOfTests = []
    lines = open(filename).readlines()
    for line in lines:
        listOfTests.append(line.strip().split(','))
    return listOfTests

def read_training_file(filename):
    priors = Counter()

    likelihood = defaultdict(Counter)

    lines =  open(filename).read().splitlines()

    # skip header line
    lines = lines[1:]

    # calculate frequency of each word in training file
    for line in lines:
        parts = line.split(',')
        col_size = len(parts)-1;
        priors[parts[4]] += 1
        for i in range(col_size):
            for word in tokenize(parts[i]):
                # increment the frequency of word
                likelihood[parts[4].rstrip()][word] += 1

    return (priors, likelihood)

def make_testing_file(fileName):
    lines = open(fileName).read().splitlines()

    #Skip header line
    lines = lines[1:]

    target = open("testing.csv", "w")

    # Make test file of size of 1/3 of training file
    size = len(lines) / 3

    for i in range(size):
        myline = random.choice(lines)
        target.write(myline)
        target.write("\n")

    target.close()
    return "testing.csv"

def main():
    try:
        training_file = sys.argv[1]
        testing_file = make_testing_file(training_file)

        (priors, likelihood) = read_training_file(training_file)

        lines = read_testing_file(testing_file)

        num_correct = 0

        for line in lines:
            # lets make prediction by naive bayes approach 
            predicted_result = classify_bayesian(line, priors, likelihood)

            # actual result in testing file ('yes' or 'no')
            actual_result = line[4]

            # comparison of prediction & correct result
            if predicted_result == actual_result:
                num_correct += 1

        print "Classified %d correctly out of %d for an accuracy of %f %%" %(num_correct, len(lines), float(num_correct)/len(lines) * 100)

    except IndexError:
        print "ERROR: Pass training data"
    except IOError, e:
        print e

if __name__ == '__main__':
    main()
