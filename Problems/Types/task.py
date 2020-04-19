args = ["script.py", "1", "2", "3", "4"],
my_list = []  # your code here
for i in range(1, len(args)):
    my_list.append(int(args[i]))

print(str(my_list))