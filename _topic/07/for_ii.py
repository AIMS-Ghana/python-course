__author__ = 'cap10'

sumFor, sumWhile = 0, 0

start, end = 0, 10

for i in range(start, end):
    sumFor += i

while start < end:
    sumWhile += start
    start += 1

assert sumFor == sumWhile