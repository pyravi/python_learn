#!/usr/bin/python3.7

# s='aaaaaaaaaaaaaaaaaaaaa'
# pos=-1
# while True:
#     pos=s.find('a',pos+1)
#     print('{} found at {} index'.format('a',pos))

print('''string writing type\n
    1.Single Quote
    2.Double Quote
    3.Three Single Quote
    4.Three Double Quote
''')
print('Python is \'scripting and programming\' langauge.' )
print('Python is "scripting and programming" langauge.' )
print('''Python is 'scripting and programming' langauge.''' )
print(r'C:\some\name') # convert in raw string

a,b=0,1
while a <10:
    print(a)
    a,b=b,b+a
