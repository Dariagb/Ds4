import random
bush=int(input("введите колиичество кустов:"))
variety=list([random.randint(1, 10) for _ in range(bush)])
print(variety)
crop=[] #cоздаем список, где каждому кусту будет соответствовать сумма ягод его и соседними
for i  in range(bush):
    prev_index=(i-1)%bush #ищем индексы кустов, которые находятся рядом
    next_index=(i+1)%bush
    final=variety[i]+variety[prev_index]+variety[next_index] #находим сумму ягод с двумя соседними кустами
    crop.append(final)
max_crop=max(crop) #максимальное количество ягод   
print(max_crop)
    
