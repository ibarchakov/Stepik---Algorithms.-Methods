"""There is an integer given 1≤n≤105 and an array of different natural numbers
not exceeding 109 in ascending order A[1…n] in a first line,
-- an integer 1≤k≤105 and a k row of natural numbers not exceeding 109 in a second line.
For each i from 1 to k it is necessary to output the index 1≤j≤n that satisfies A[j]=bi,
or −1 if there is no such j.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1

"""


def search(elem, area):
    """Searches an element from a second line in a given ascending array
    by dividing a searching area into two halves according to a middle
    element check thus reducing a searching area in two times

    """
    start = 0
    end = len(area) - 1
    while start <= end:
        search_point = (start + end) // 2
        if area[search_point] == elem:
            return search_point + 1
        elif area[search_point] > elem:
            end = search_point - 1
        else:
            start = search_point + 1
    return -1


def main():
    array = []
    digits = []
    answer = []

    input1 = str(input()).split()
    n = int(input1[0])
    for _ in range(1, n + 1):
        array.append(int(input1[_]))

    input2 = str(input()).split()
    k = int(input2[0])
    for _ in range(1, k + 1):
        digits.append(int(input2[_]))

    for elem in digits:
        answer.append(search(elem, array))
    for _ in answer:
        print(_, end=' ')


if __name__ == '__main__':
    main()
