#три варианта строки


message = 'Hello World'   
print(message) 

text = 'I am student'
print(text)

numbers = 'Eleven'
print(numbers)


#три вариантта числа


num1 = 1          #созданеи int           
num2 = 1.10       # создание float
num3 = '1.10'     #создание строки

print(num1)
print(num2)
print(num3)


#три варианта списков


my_list = [1, 2, 3, 4]   #цифровой список
print(my_list)

my_list = ('One', 'Two', 'Three', 'Four')  #словесный список
print(my_list)

my_list = ('One', '2', 'Three', '4')  #смешаный список
print(my_list)




#три варианта словаря


dictionary = {'персона': 'человек',
              'марафон': 'гонка бегунов длиной около 26 миль',
              'противостоять': 'оставаться сильным, несмотря на давление',  #ключ-слово, значение-слово
              'бежать': 'двигаться со скоростью'}
print(dictionary)


gender_dict = {0: 'муж',     #ключ-цифра, значение-слово
               1: 'жен'}
print(gender_dict)


auto_dict = {"Company": "Toyota",     #смешаный словарь
  "model": "Premio",
  "year": 2012}
print(auto_dict)



#три варианта кортежей


a = ()        # пустой кортеж
print(a)

a = (5,'Hello', True)     # кортеж из 3-х элементов различных типов
print(a)

a = ('I am', (1.11, "Student")) # вложенный кортеж типов
print(a)



#три примера использования min()

s = 'abcC'
print(min(s))   #Min со строкой

tuple_numbers = (1, 2, 3, 4)  # Min с кортежем
print(min(tuple_numbers))
                                                
list_numbers = [1, 2, 3, -4]  # Min cосписком
print(min(list_numbers))


#три примера использования max(),
#аналогичны и противоположны min().



#Оператор IN


# Операция in - определение наличия элемента в списке
A = [ 'abc', 7, 8.5, -100 ]

# Использование операции in
item = 8.5 # искомый элемент
b = item in A # b = true
print("b = ",b)


# Генераторы списков
# сгенерировать список A из строки 'Hello', символ c дублируется 3 раза
A = [c*3 for c in 'Hello'] # A = ['HHH', 'eee', 'lll', 'lll', 'ooo']
print("A = ", A)


# Генераторы списков
# сгенерировать список A из строки 'Hello'
A = [i for i in 'Hello'] # A =   ['H', 'e', 'l', 'l', 'o']
print("A = ", A)



#Три примера условия if elif else.


a = int(10)
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')


age = int(21)
if age < 18:
    print('Close')
elif 17 <= age > 18:
    print('Open')
else:
    print('Next time')


car = str('BMW')
if str('BMW'):
    print('Helooo')
elif str('Mercedes'):
    print("It's not your website")
else:
    print('Not today')

































