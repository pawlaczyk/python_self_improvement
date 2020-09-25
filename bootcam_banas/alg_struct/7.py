class HashFunction:
    """ Modulo przez liczbę pierwszą np 31 dramatycznie zmniejsza lcizbe kolizji"""
    def __init__(self, size):
        self.list_size = size
        self.the_list = []
        for i in range(size): #wypelnianie poczatkowe listy
            self.the_list.append("-1") # na pewno tego nie mam w liscie

    def hash_func_1(self, str_list):
        # słaba funkja hashująca
        for j in str_list:
            index = int(j)
            self.the_list[index] = j

    def hash_func_2(self, str_list):
        for k in str_list:
            str_int = int(k)
            index = str_int % 31
            print(f"Mod Index: {index} Value: {str_int}")

            while self.the_list[index] != "-1": #szukanie kolizji
                index+= 1
                print(f"Collision Try: {index} Instead")
                index %= self.list_size
            # jak nie ma kolizji to zapisuję
            self.the_list[index] = k

    def find_key(self, key):
        list_index_hash = int(key) % 29
        while self.the_list[list_index_hash] != "-1":
            if self.the_list[list_index_hash] == key:
                print(f"{key} in Index {list_index_hash}")
                return self.the_list[list_index_hash]
            list_index_hash += 1
            list_index_hash %= self.list_size
        return False

    def is_prime(self, num):
        # Własnosci liczb pierwszych
        # 6k =/- 1 prawdą po za liczbami 2 i 3
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False

        # 6k =/- 1 prawdą po za liczbami 2 i 3
        j= 5
        while j * j <= num:
            if num % j == 0 or num % (j+2) == 0:
                return False
            j = j + 6
        return True

    def get_next_prime(self, min_size):
        while True:
            if self.is_prime(min_size):
                return min_size
            else:
                min_size +=1 # min_size = +1 uzna wartosić jako (+1) dodanie a nie inkrementacje

    def increase_list_size(self, min_size):
        new_list_size = self.get_next_prime(min_size)
        print(new_list_size)
        self.move_old_list(new_list_size)

    def fill_list_with_none(self):
        for k in range(self.list_size):
            self.the_list.append(None)

    def remove_empty_spaces_in_list(self):
        temp_list = []
        for j in self.the_list:
            if j is not None:
                temp_list.append(j)
        return temp_list

    def move_old_list(self, new_list_size):
        self.list_size = new_list_size
        clean_list = self.remove_empty_spaces_in_list()
        self.fill_list_with_none()
        self.hash_func_2(clean_list)




hash_table = HashFunction(30)
str_list = ["1", "5", "17", "21", "26"]
hash_table.hash_func_1(str_list)
for i in range(hash_table.list_size):
    print(i, end=" ")
    print(hash_table.the_list[i])

print("*"*79)
print()

hash_table_2 = HashFunction(31)
#spec janlnie tyle danych by mieć kolizję
str_list_2 =  ["100", "510", "170", "214", "268", "398",
              "235", "802", "900", "723", "699", "1", "16",
              "999", "890", "725", "998", "990", "989", "984",
              "320", "321", "400", "415", "450", "50", "660", "624"]
hash_table_2.hash_func_2(str_list_2)
for i in range(hash_table_2.list_size):
    print(i, end=" ")
    print(hash_table_2.the_list[i])

hash_table_2.find_key("660")

print("*"*79)
print("Find Primes")
for i in range(500):
    if hash_table.is_prime(i):
        print(i)


print("*"*79)
print("Zmiana rozmiaru")
hash_table.increase_list_size(60)
for i in range(hash_table_2.list_size):
    print(i, end=" ")
    print(hash_table_2.the_list[i])
