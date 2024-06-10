import sys


f = open("Text.txt", "r")
my_list = str(f.read()).split()
my_dict = {}
for x in my_list:
    my_dict[x] = my_list.count(x)
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
