import math

def compareTriplets(a, b):
    score = [0,0]
    for i in range(len(a)):
        if a[i] > b[i]:
            score[0] = score[0] + 1
        elif a[i] < b[i]:
            score[1] = score[1] + 1
        else:
            pass
    return score

if __name__ == "__main__":
    a = input().split(' ')
    b = input().split(' ')

    print(compareTriplets(a, b))
