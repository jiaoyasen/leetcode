import operator
data = [1,3,7,2,11,35,9,7,3,1,1,3,4,5,23]
result = {}
for i in data:
    tmp = result.get(i,0) + 1
    result[i] = tmp
print(result)
result_sorted = sorted(result.items(), key = operator.itemgetter(0))
print(result_sorted)
