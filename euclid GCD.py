"""Find the GCD for a given two integers 1≤a,b≤2⋅109.

Sample Input 1:
18 35
Sample Output 1:
1

Sample Input 2:
14159572 63967072
Sample Output 2:
4

"""


def euclid_gcd(a, b):
    """Function uses a Euclid algorithm to find the GCD:
    1. Compares two numbers and changes the greater one with the the difference
    between the larger and the smaller numbers
    2. Repeats pos.1 until numbers are equal == GCD

    """
    if a == 0:
        return b
    elif b == 0:
        return a
    if a >= b:
        return euclid_gcd(a % b, b)
    else:
        return euclid_gcd(a, b % a)


def main():
    a, b = map(int, input().split())
    print(euclid_gcd(a, b))


if __name__ == '__main__':
    main()
