import random

"""The mean colour """
#total number of colour in a week is 91
#total number of colour shirt is  10

number_of_colour_dress_in_a_week = 91
number_of_colour_dress = 10

mean_color = number_of_colour_dress_in_a_week / number_of_colour_dress
print("The mean color is ", mean_color)
#the shirt mostly worn throughout the week is blue
def fibonacci(n):
    a,b =0, 1
    while a < n:
        yield a
        a, b = b, a+b
"""The first 50 fibonacci sequence"""
m = list(fibonacci(10000000000))
print(len(m))
print("the sum of the first 50 fibonacci sequence is ", sum(m))

def rand():
    """A function that generate 4 digit binary random number"""
    x = ''
    for i in range(4):
        x += str(random.randint(0,1))
    return x


# converting the num to decimal 
x = rand()
print(int(x, base=2))
