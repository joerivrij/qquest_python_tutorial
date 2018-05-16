num = 1
print(num, type(num))
num = num + num
print(num)
print('---------------------')

num = 2.5
print(num, type(num))
num = 1
print(num, type(num))
num = 2.5 + 1
print(num)
print('---------------------')

string = 'I am a string'
print(string, type(string))
string = "I am also a string"
print(string, type(string))
string_in_string = 'I am a string "in a string" in a string'
print(string_in_string, type(string_in_string))
print(f'I am printing a {string} in a string')
print('---------------------')

num = 'string'
print(num, type(num))
num = 9
print(num, type(num))
print(str(num), type(str(num)))