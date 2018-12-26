"""The first line contains the number of items 1≤n≤10**3 and the knapsack capacity 0≤W≤2⋅10**6.
Each of the next lines specifies the cost 0≤ci≤2⋅10**6 and the volume 0<wi≤2⋅10**6 of the item
(n, W, ci, wi — integers). Output the maximum cost of item parts (each item can be divided
in any parts, its cost and volume proportionally decrease) can be put in a knapsack with an accuracy
at least three decimal places.

Sample Input:
3 50
60 20
100 50
120 30

Sample Output:
180.000

"""


items_list = []
knapsack_value = 0

number_of_items, capacity = map(int, input().split())
for i in range(number_of_items):
    price, weight = map(int, input().split())
    spec_cost = float(price / weight)
    items_list.append([price, weight, spec_cost])
    items_list.sort(key=lambda i: i[2])

while capacity > 0 and items_list:
    i = len(items_list) - 1
    if items_list[i][1] <= capacity:
        capacity -= items_list[i][1]
        knapsack_value += items_list[i][1] * items_list[i][2]
        items_list.remove(items_list[i])
    else:
        knapsack_value += capacity * items_list[i][2]
        capacity -= capacity

print(knapsack_value)
