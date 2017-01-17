""" Author: Rick Sam
    Purpose: Practice
    Book: Bye Code
    Program: Exception_Raise"""
class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = raw_input('Enter Something-->')
    if len(text) <3:
        raise ShortInputException(len(text),3)
except EOFError:
    print 'Why did you do a EOF on me?'
except ShortInputException as ex:
    print ('ShortInputException: The input was' + \
            '{0} long, excepted at least {1}') \
            .format(ex.length, ex.atleast)
else:
    print 'No exception was added.'
