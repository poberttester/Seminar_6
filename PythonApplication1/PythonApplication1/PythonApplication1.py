import Functional



# 1. Фрукты
print('\n', '1. Фрукты')
Functional.fruit()


# 2. Старший и младший
print('\n', '2. Старший и младший')
Functional.youngest_friend(Functional.create_fiends())


# 3. Еще немного о друзьях
print('\n', '3. Еще немного о друзьях')
friends = Functional.create_fiends()

Functional.avg_age(friends)
Functional.longest_name(friends)

	
# 4. Английский словарь
print('\n', '4. Английский словарь')
Functional.create_language_dictionary()


# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.
print('\n', '4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.')
rand_list = Functional.create_random_numbers()
Functional.find_unique_values(rand_list)