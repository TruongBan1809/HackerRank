import math

def simpleArraySum(arr):
    sum = 0
    for i in arr:
        sum = sum + int(i)
    return sum

if __name__ == '__main__':
    arr = input().split(' ')
    sum = simpleArraySum(arr)
    print(sum)