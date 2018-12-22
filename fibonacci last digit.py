"""The number 1≤n≤10**7 is given, find the last digit of n-Fibonacci number.

Sample Input:
317457

Sample Output:
2

"""


def fib_digit(n):
    """If 0≤a,b≤9 are the last digits of Fibonacci numbers Fi и Fi+1,
    then(a+b)mod10 is the last digit of Fibonacci number Fi+2.

    """
    array = [0, 1]
    for i in range(2, n+1):
        array.append((int(str(array[i-1])[-1]) + int(str(array[i-2])[-1])) % 10)
    return array[n]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == '__main__':
    main()
