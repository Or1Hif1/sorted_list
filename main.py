import sys


def replacer(old_string, char, index):
    if index == len(old_string):
        return old_string[:-1]+char
    if index == 0:
        return char+old_string[1:]
    return old_string[:index]+char+old_string[index+1:]


def sinon(old_string: str):
    for x in old_string:
        if not x.isalpha() and x != " ":
            old_string = replacer(old_string, "", old_string.index(x))
    return old_string


f = open("Text.txt", "r")
my_list = str(f.read()).split()
my_dict = {}
w = "hello, world!"
print(sinon(w))
print(my_list)
for x in my_list:
    x = sinon(x)
    my_dict[x] = my_list.count(x)
print(my_list)
new_list = sorted(my_dict, key=lambda y: my_dict[y], reverse=True)
n = sys.argv[1]
if int(n) > len(new_list):
    print("Not Good")
else:
    try:
        for x in range(int(n)):
            print(new_list[x])
    except ValueError:
        print("Value Error")
