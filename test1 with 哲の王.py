import operator
import datetime
import collections
import time
data = [1,3,7,2,11,35,9,7,3,1,1,3,4,5,23]
result = {}

time1 = time.clock()
for i in data:
    result[i] = result.get(i,0) + 1
time2 = time.clock()
print("The running time of 1 is ",(time2-time1))
print(result)

result = {}
time1 = time.clock()
a = set(data)
for i in a:
    result[i] = data.count(i)
time2 = time.clock()
print("The running time of 2 is ",(time2-time1))
print(result)

result = {}
time1 = time.clock()
result = collections.Counter(data)
time2 = time.clock()
print("The running time of 2 is ",(time2-time1))
print(result)


result = {}
time1 = time.clock()
for i in data:
    result[i] = result.setdefault(i,0) + 1
time2 = time.clock()
print("The running time of 2 is ",(time2-time1))
print(result)

# result_sorted = sorted(result.items(), key = operator.itemgetter(0))
# print(result_sorted)