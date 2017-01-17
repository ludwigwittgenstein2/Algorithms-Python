''' identifiers
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
. any character, except for a newline
\b the whitespace around words
\. a period

Modifiers:
{1,3} we're expecting 1-3 \d{1-3}
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ match the end of a string
^ matching beginning of a string
| either or \d{1-3} | \w{5-6}
[] range  or variance [A-Za-z][1-5a-qA-Z]
{x} expecting "x" amount

White Space characters:
\n - new line
\s - space
\t - tab
\e - escape
\f - form feed
\r - return carriage

DONT FORGET!:
. + * ? [] $ ^ () {} | \  - If you want to use them, you need to escape them


'''

import re

exampleString = ''' Jessica is 15 years old, And Daniel is 27 years old. Edwards is
97, And his grandfather, Oscar, is 102.'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print ages
print names 
