



list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
list1.append(11)
print(list1)
print(list1)
print(list1[0], list1[8])
print(list1[1:5])
print(list1[1:])
print(list1[:5])
print('---------------------')

list2 = [1, 1, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 7,8, 2, 1, 1, 1, 2, 7, 4, 5, 6, 7, 8, 9, 10]
print(list2)
set_list2 = list(set(list2))
print(set_list2)
print('---------------------')

list3 = [1, 3, 2, 10, 9, 6, 7, 8, 5, 4]
print(list3)
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)
print('---------------------')


list4 = []
for x in range(15):
    list4.append(x**3)

print(list4)


list4 = list(map(lambda x: x**3, range(15)))
print(list4)

print('---------------------')

#list Comprehensions
list5 = [x**3 for x in range(15)]
print(list5)



list6 = [23524356346, 23598235092835, 235874587135, 2039851,
         656545451, 5166546465435, 35656514684, 2115456846845212, 65465465465121, 100351510]
max_value = max(list6)
min_value = min(list6)
avg_value = sum(list6)/len(list6)
print(max_value)
print(min_value)
print(avg_value)