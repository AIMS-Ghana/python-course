__author__ = 'cap10'

something = input("enter something:")
while something != "stop":
    print(something)
    something = input("enter something, 'stop' to stop:")

anumber = None

while anumber != -1:
    try:
        anumber = int(input("enter an integer, -1 to stop:"))
    except (TypeError, ValueError) as err:
        print(err.args[0])
    else:
        print("success", anumber)
