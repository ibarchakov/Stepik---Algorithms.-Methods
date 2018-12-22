"""For n given intervals find the set of points of a minimal size for which each interval
contains at least on of the points.
In a first line there is given a number of intervals 1≤n≤100.
Each of a next n lines consists of two numbers 0≤l≤r≤10**9 defining the start and the end of the interval.
Output the optimal number of m points and the points itself.
If there are many such sets then output any of them.

Sample Input 1:
3
1 3
2 5
3 6

Sample Output 1:
1
3

Sample Input 2:
4
4 7
1 3
2 5
5 6

Sample Output 2:
2
3 6

"""


base = []
answer = []


cuts = int(input())
for cut in range(cuts):
    start, end = map(int, input().split())
    cut_list = [start, end]
    base.append(cut_list)


while len(base) > 0:
    min = base[0]
    for i in range(len(base)):
        if base[i][1] < min[1]:
            min = base[i]
    answer.append(min)
    for i in reversed(range(len(base))):
        if min[1] in range(base[i][0], base[i][1] + 1):
            base.remove(base[i])

print(len(answer))
for elem in answer:
    print(elem[1], end=' ')
