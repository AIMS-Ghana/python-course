__author__ = 'cap10'

def findFib(err):
    first, last = 1, 2
    phiEst = 1.0 # 1/1
    while (phiEst - last/first)**2 > err**2:
        phiEst = last/first
        temp = last
        last += first
        first = temp
    return (first, last, last/first)

if __name__ == "__main__":
    print(findFib(1e-6))
    print(findFib(1e-12))
