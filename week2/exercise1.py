"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']
# I think it will print "word"
for word in some_words: 
    print(word)#Prints "What does this line do"
# I think it will print "x"
for x in some_words:#Prints "What does this line do"
    print(x)
# I think it will print "Word" and "x"
print(some_words)
# I think it will print the string if some words variable contains more tham 3 words
if len(some_words) > 3:# Printed the string
    print('some_words contains more than 3 words')
# this will show me system specs
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())# showed me the system specs!!! and name of pc 

usefulFunction()
