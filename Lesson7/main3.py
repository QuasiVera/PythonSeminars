'''
[12,'sadf',5643] ---> ['sadf'] ,[12,5643]

'''
# list1 = [-12,'sadf',5643]
# list1 = [x for x in input().split()]
# res1 =list(filter(lambda el: el.isdigit(), list1))
# res2 = list(filter(lambda el: el.isdigit()==False, list1))
# # res1 =list(filter(lambda el: type(el)==int, list1))
# # res2 = list(filter(lambda el: type(el)== str, list1))

# print(res1, res2)

lst = [x for x in input().split()]
res1 = list(filter(lambda el: not el.isdigit(), lst))
res2 = list(map(int, filter(lambda el: el.isdigit(), lst)))
print (res1,res2)
