# ������

# 1. Фрукты
# Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате: название фрукта и его количество. 
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.

def fruit ():
	k = int(input('number of fruit: '))
	dictionary = {}


	for i in range(k):
		key = input('fruit: ')
		value = int(input('number of: '))
		dictionary [key] = value

	return print(dictionary)


# 2. Старший и младший
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

def create_fiends():
    def input_name():
        return input("name: ")
    
    def input_age():
        return int(input("age: "))    
        
    
    N = int(input('numbers of friends: '))
    list_friend = [(input_name(), input_age()) for i in range(N)]
    
    return list_friend


    

def youngest_friend(list_friend):
    
    def get_key(dictionary, value):
        for k, v in dictionary.items():
            if v == value:
                return k
        else: 
            return "None"
            
    dictionary_friend = dict(list_friend)
    youngest_friend = min(dictionary_friend.values())
    
    print("youngest friend is", get_key(dictionary_friend, youngest_friend))



# 3. Еще немного о друзьях
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.

def avg_age(list_friend):
    
    N = len(list_friend)
    dictionary_friends = dict(list_friend)
    avarage_age = round(sum(dictionary_friends.values()) / N, 0)

    
    print("avarage age  is", avarage_age)

# find longest NAME in list
def longest_name(list_friend):
    
    dictionary_friends = dict(list_friend)

    ## get names your friends
    list_names = dictionary_friends.keys()
    
    longest_name = longest_string_func(list_names) 
        
    
    print("longest_name is", longest_name)
 
# find longest STRING in list
def longest_string_func(x):
    max = 0
    for i in x:
        if len(i) > max: 
            max = len(i)
            longest_string = i
        
    return longest_string


# 4. Английский словарь
# "Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка. 
# Программа получает на вход слово на английском языке и несколько его переводов на русском языке. 
# Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов. 

