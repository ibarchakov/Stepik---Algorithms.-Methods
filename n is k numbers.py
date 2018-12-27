"""For a given number 1≤n≤10**9 find the maximum number k
 for which n may be presented as a sum of various k natural components.
 In the first line you should output the k number and all the k components in the second line.

Sample Input 1:
4

Sample Output 1:
2
1 3

Sample Input 2:
6

Sample Output 2:
3
1 2 3

"""


n = int(input())

num_list = []
start = 1
sum_num_list = 0

while sum_num_list < n:
    num_list.append(start)
    sum_num_list += start
    start += 1

if sum_num_list == n:
    print(len(num_list))
    for i in num_list:
        print(i, end=' ')
else:
    elem_del = sum_num_list - n
    num_list.remove(elem_del)
    print(len(num_list))
    for i in num_list:
        print(i, end=' ')
