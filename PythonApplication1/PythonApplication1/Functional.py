# ������

# 1. ������
# ������������ ������ ����� K - ���������� �������. ����� �� ������ K ������� � �������: �������� ������ � ��� ����������. 
# �������� ��� ������ � �������, ��� �������� ������ - ��� ����, � ���������� - ��������.

def fruit ():
	k = int(input('number of fruit: '))
	dictionary = {}


	for i in range(k):
		key = input('fruit: ')
		value = int(input('number of: '))
		dictionary [key] = value

	return print(dictionary)


# 2. ������� � �������
# ������������ ������ ����� N. ����� �� ������ ������ ������ (��� � �������) ����� N ������. �������� ������ friends � �������� � ���� N �������� � ������� name � age. 
# ������� ������ �������� �� ������ � �������� ��� ���.

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
		


	 