import random
lot =(int(input("Введите колличество элементов первого множества:")))
lot2 =(int(input("Введите колличество элементов второго множества:")))
variety=set([random.randint(1, 10) for _ in range(lot)])
variety2=set([random.randint(1, 10) for _ in range(lot2)])
print(variety)
print(variety2)
res= sorted(variety.intersection(variety2))
print(res)