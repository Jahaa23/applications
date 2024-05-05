#string validators

import re
str1 = input()

for char in str1:
    a = char.isalnum()
    if(a == True):
        print('True')
        break
if a!=True:
    print('False')
for char in str1:
    b = char.isalpha()
    if(b == True):
        print('True')
        break
if b!=True:
    print('False')
m = re.search('[0-9]', str1)
if(m is None):
    print('False')
else:
    print('True')
k = re.search('[a-z]', str1)
if(k is None):
    print('False')
else:
    print('True')

l = re.search('[A-Z]', str1)
if(l is None):
    print('False')
else:
    print('True')
