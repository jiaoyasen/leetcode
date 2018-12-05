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
time2 = time.clock()import operator
import datetime
import collections
import time
import random

data = [random.randint(-100,101) for i in range(10000)]

#get() method of dict
result = {}
time1 = time.clock()
for i in data:
    result[i] = result.get(i,0) + 1
time2 = time.clock()
print("The running time of 1 is ",(time2-time1))
print(result)

#get() method of dict ,time is 4.5e-6
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
print("The running time of 3 is ",(time2-time1))
print(result)


result = {}
time1 = time.clock()
for i in data:
    result[i] = collections.deque.append(i)
time2 = time.clock()
print("The running time of 4 is ",(time2-time1))
print(result)



result = {}
time1 = time.clock()
for i in data:
    result[i] = result.setdefault(i,0) + 1
time2 = time.clock()
print("The running time of 5 is ",(time2-time1))
print(result)



result = {}
time1 = time.clock()
for i in data:
    result[i] = result.setdefault(i,0) + len(set([i]).intersection(data))
time2 = time.clock()
print("The running time of 6 is ",(time2-time1))
print(result)
# result_sorted = sorted(result.items(), key = operator.itemgetter(0))
# print(result_sorted)


import random
data = []
for i in range(10000):
    data.append([random.randint(-100,101) for j in range(random.randint(10,1001))])


a = [1,2,1,1,3,4,5,1,2,4,6]
result = {}
for i in range(len(a)):
    result[a[i]] = result.setdefault(a[i],[]) + [i]
print(result)
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