__author__ = 'cap10'

tot = 0

for i in range(1, 10):
    tot += i

print(tot)

for s in ["some", "different", "words"]:
    print(s)

print(s)

first, last = 0, 1
print(last)

for i in range(0,20):
    temp = last
    last += first
    print(last,last/temp)
    first = temp