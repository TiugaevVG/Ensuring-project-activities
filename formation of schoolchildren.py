print('Введите рост учащихся - 10 человек')
i=0
schoolmateHieght = [ ]
while i < 10:
    a = int(input())
    if a < 200:
        schoolmateHieght.insert(0, a)
        i=i+1
    
print('Список группы по росту')
schoolmateHieght.sort(reverse = True)
print(schoolmateHieght)
print('Введите рост Пети')

hieght = int(input())

for element in schoolmateHieght:
    if element < hieght:
        schoolmateHieght.insert(schoolmateHieght.index(element), hieght)
        print('место пети')
        print(schoolmateHieght.index(element))
        break
    else:
        continue
print(schoolmateHieght)