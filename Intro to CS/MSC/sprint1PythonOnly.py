from keras.datasets import mnist
import matplotlib.pyplot as plt
from collections import Counter

(x_train, y_train), (x_test, y_test) = mnist.load_data()

def least_common_digit(x_set, y_set):
    '''
       Input: x_set, the x values of the dataset and y_set, the y values of the  dataset
       Expected Output: The image from the x set of the least common digit.
    '''
    for i,num in enumerate(y_set):
        if num == least_common:
            return x_set[i]

        
lc_train = least_common_digit(x_train, y_train)
lc_test = least_common_digit(x_test, y_test)

def most_common_digit(x_set, y_set):
    '''
       Input: x_set, the x values of the dataset and y_set, the y values of the  dataset
       Expected Output: The image from the x set of the most common digit.
    '''
    for i,num in enumerate(y_set):
        if num == most_common:
            return x_set[i]

    
mc_train = most_common_digit(x_train, y_train)
mc_test = most_common_digit(x_test, y_test)

def plot_two(im1, title1, im2, title2):
    '''
        Input: im1, a matrix representing a grayscale image and title1 a string,im2 a matrix representing 
        a grayscale image and title2 a string
        Expected Output: A tuple (fig, ax) representing a generated figure from matplotlib and two subplots 
        ready to display the inputed images with the given titles
    '''
    return (fig, ax)

plot_two(lc_train, 'Least Common Train', lc_test, 'Least Common Test'), plot_two(mc_train, 'Most Common Train', mc_test, 'Most Common Test')
plt.show()

def how_many_of_each_digit(y_set):
    '''
       Input: y_set, the y values of the training set
       Expected Output: A dict of the count of each digit in the set
    '''
    return vals_by_count

count_train = how_many_of_each_digit(y_train)
count_test = how_many_of_each_digit(y_test)

def bar_chart(train, test):
    '''
    Inputs: train, a dictionary of count of each digit of the training set and test, a dictionary of the count
    of each digit for the test set
    Expected Output: A tuple (fig, ax) ready to show using matplotlib
    '''
    return (fig, ax)

fig, chart = bar_chart(count_train, count_test)
plt.show()

def interesting_visualization():
    '''
        Fill in this code block with your interesting visualization if you want the extra credit
    '''
    pass

#remember to set the arguments for your visualization if you need to
interesting_visualization()
