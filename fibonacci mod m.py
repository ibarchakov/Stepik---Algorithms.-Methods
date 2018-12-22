"""There are integers given 1≤n≤10**18 and 2≤m≤10**5,
find the remainder of dividing of n-Fibonacci number by m.

"""


def fib_mod(n, m):
    """The task is solved using the definition of Pisano period.
    For any integer n, the sequence of Fibonacci numbers Fi taken modulo n is periodic.
    The Pisano period, denoted π(n), is the length of the period of this sequence.

    """
    if n <= 2:
        return 1
    else:
        pisano = [0, 1]
        for i in range(2, 6 * m):
            pisano.append((pisano[i - 2] + pisano[i - 1]) % m)
            if pisano[i-1] == 0 and pisano[i] == 1:
                break
        target_pisano_position = n % (len(pisano)-2)
        answer = pisano[target_pisano_position]
        return answer


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == '__main__':
    main()
