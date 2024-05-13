## Fundamental Data Types
    #int : integer
    #float : decimal point
    #bool : True or False
    #str : string
    #list : ordered sequence of values
    #tuple
    #set
    #dict

print( 2 + 4 );
print(type( 2 + 4 ));
print(type( 2 / 4 ));
print(type( 2 // 4 ));

print(2 ** 3); #potencia
print(5 % 4); #modulo

print(round(3.1)); #redondear
print(abs(-20)); #absolute value

print(bin(5)) #binary
print(int('0b101', 2)) #binary to int

#variables

    #snake_case : my_variable
    #start with lowercase or underscore
    #case sensitive : my_variable != My_variable
    #don't overwrite keywords : keywords become blue in the editor

a = 69; #assignment
PI = 3.14 #constant
a,b,c = 1,2,3; #multiple assignment

#expressions vs statements
iq = 100; #statement
user_iq = iq / 5; #conté uma expression, mas no seu todo, é um statement

#augmented assignment operator
iq += 20;
print(iq);

print(type('hi ' + 'there')); #concatenation and type str

long_string = '''
WOW
O O
---
''';

print(long_string);

first_name = 'Davy';
last_name = 'Gatinho';

full_name = first_name + ' ' + last_name;

#Tipe conversion
print(type(str(100))); #int to str
print(type(int(str(100)))); #str to int

#Escape Sequence
weather = "It's \"kind of\" sunny";

print(weather);

# \t adds a tab ; \n adds a new line ; \\ adds a backslash

#Formatted Strings

name = 'Davy';
age = 18;

print ('hi' + name + '. You are ' + str(age) + ' years old');
    #or:
print(f'hi {name}. You are {age} years old');

#String Indexes

selfish = 'me me me';
print(selfish[0]); #m

# [start:stop:stepover]
print(selfish[0:8:3]); #me
print(selfish[::-1]); #reverse string

#Immutability
    #strings are immutable
    #selfish[1] = 'a' #error

#Built-in Functions

## Classes -> custom types


## Specialized Data Types

## None

############################################