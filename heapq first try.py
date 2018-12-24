"""The first line contains the number of operations 1≤n≤10**5.
Each of next n lines specifies the operations one of the next types:
Insert x, where 0≤x≤10**9 — integer;
ExtractMax.
The first operation adds x to a heap, the second — extracts the maximum number and outputs it.

Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

Sample Output:
200
500

"""


import heapq


h = []
max_elems = []


n = int(input())
for _ in range(n):
    command = input()
    if command.startswith('Insert'):
        command = command.split(' ')
        elem = int(command[1])
        heapq.heappush(h, -elem)
    else:
        max_elems.append(-h[0])
        heapq.heappop(h)


for _ in max_elems:
    print(_)