# Regular Expressions

# Search : Returns a Match object if there is a match anywhere in the string
# findall : Returns a list containing all matches
# Split: Returns a list where the string has been split at each match
# sub : Replaces one or many matches with a string

'''
QUICK SNIPPET:
re.search('^a.*s$',letters)
re.search('\AThe',letters)
re.findall('[a-z]',letters) / re.findall('[a-zA-Z]',b) / re.findall('[0-9]',b)
re.findall("ai", txt)
re.findall("\d", txt)
re.findall('^D.*ai{2}',txt)
re.findall("Oiii|Daiii", txt)
re.findall(r"\bain", txt) ---> r'ain\b' --> r"\Bain"  --> r"ain\B"
\D - only strings
\s - only space
\S - without space
\W - special character
\w - words
re.findall("[0123]", txt) --> re.findall("[arn]", txt) -> re.findall("[^arn]", txt)
re.sub('\s','9',txt,2)
'''
import re
text='The value of creation is depends upon the action'
letters='absolute'
numerics = 'abkdkfdj5523226'
re.search('^a.*s$',letters)  ---> Will return True or false
re.search('^The.*action$',text)  ---> will return True or False
re.findall('^The.*action$',text) --> ['The value of creation is depends upon the action']
re.search('\AThe',letters)  --> If the letter starts with "The"
re.findall('^[a-zA-Z].*[0-9]',numerics) --> which helps to give alpha and numeric values
re.findall('[a-zA-Z][0-9]',numerics) --> will give 'j2' numeric next to alpha letter
-----------------------------------------------------

letters='absolute'

re.findall('[a-z]',letters)  --> ['a', 'b', 's', 'o', 'l', 'u', 't', 'e']
re.search('[a-z]',letters)   --> match object->Return True
re.findall('[a-z]',text)
['h', 'e', 'v', 'a', 'l', 'u', 'e', 'o', 'f', 'c', 'r', 'e', 'a', 't', 'i', 'o', 'n', 'i', 's', 'd', 'e', 'p', 'e', 'n', 'd', 's', 'u', 'p', 'o', 'n', 't', 'h', 'e', 'a', 'c', 't', 'i', 'o', 'n']
re.search('[A-Z]',letters)   --> match object - Return false

b='section under 142'

int(''.join(re.findall('\d',b))) - Can get the output values in int type itself

re.findall('[0-9]',b) 

b= 'Value are between 55 25 746'
re.findall('[0-5][0-9]',b) - #Check if the string has any two-digit numbers, from 00 to 59:

re.findall('[a-zA-Z]',b) - Any character between lower and upper case


------------------------------------------------------------

import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)  --> ['ai', 'ai']



------------------------------------------------------------


txt = "That will be 59 dollars"
a='Hello world'

#Find all digit characters:

x = re.findall("\d", txt)  -->['5','9']

print re.findall('world$', a)  --> ['world']

print re.findall('He..o',a)

---------------------------------------------------------

import re

txt = 'Daiii welcomee' 

# #Check if the string contains "a" followed by exactly two "i" characters:

print re.findall('ai{2}',txt)
print re.findall('^D.*ai{2}',txt)

---------------------------------------------------

# | - either or
#Check if the string contains either "Daiii" or "Oiii":

import re

txt = 'Dai welcomee Oiiiiiiiii' 

print re.findall("Oiii|Daiii", txt)

if re.search("Oiii|Daiii", txt):
    print "Yesss"
else:
    print "Nooo"


-------------------------------------------------------

# r"\bxxx" or r"xxx\b"
import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)


print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

-------------------------------------------------

# r"\Bxxx" or r"xxx\B"  -- 'xxx' present but NOT at the beginning or ending

import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

#Check if "ain" is present, but NOT at the end of a word:

x = re.findall(r"ain\B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

----------------------------------------------------------------------------

re.findall('\D',b)  - Returns a match where the string DOES NOT contain digits	


re.findall('\s',b) -Returns a match where the string contains a white space character

re.findall('\S',b) - Returns a match where the string DOES NOT contain a white space character	


re.findall('\w',b)  - Any word except space

re.findall('\W',b) - Doesnt contain any character

-----------------------------------------------------------------------------

import re

txt = "The rain in Spain 2512"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)


#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)


#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

------------------------------------------------------------

import re

#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


#Replace the first two occurrences of a white-space character with the digit 9:

x = re.sub("\s", "9", txt, 2)

--------------------------------------------------------------

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
print(x.span())
print(x.group())

----------------------------------------------------------

# Capture the mail ID

maidID='ganesh92jai@gmail.com'

re.findall(r'\A\w+.*@\w+.\w+',maidID)  -- Best for all scenario
re.findall(r'\A\w+.*@gmail.com$',mailID)
re.findall(r'\A\w+.@gmail.com\b',mailID)

