# Double Hashing Clustering
# TODO: Collision attack
# https://en.bitcoinwiki.org/wiki/Collision_attack
# print("|{:>3}".format(" "), end=" ")
class HashFunctions:
    def __init__(self, size):
        self.list_size = size
        self.the_list = ["-1" for i in range(size)]

    def dbl_hash_func(self, str_list):
        for k in str_list:
            str_int = int(k)
            index = str_int % 61 # modulo prime number
            # różnica w odległościach w stosunku do poprzedniej wersji
            step_distance = 7 - (int(self.the_list[index]) % 7)
            while self.the_list[index] != "-1":
                index += step_distance #posuzkiwanie kolejnego wolnego indeksu
                index %= self.list_size
            self.the_list[index] = k
            self.print_list()
            print()

    def print_list(self):
        # Rows of data
        # Print bunch of lines
        # Print indexes
        # Print data  separated with |

        increment = 0
        num_of_rows = int((self.list_size / 10) + 1)
        for j in range(num_of_rows):
            self.print_line(80)
            increment += 10
            self.print_row(increment, False) #indeksy
            self.print_line(80)
            self.print_row(increment, True)
        self.print_line(80)

    def print_line(self, num_of_lines):
        for l in range(num_of_lines):
            print("-", end="")
        print()

    def print_row(self, increment, is_data):
        k = increment - 10
        while k <= increment:
            if k > self.list_size - 1:
                print("|     ", end="")
            else:
                if not is_data:
                    print("| {:>3} ".format(k), end="")
                else:
                    if self.the_list[k] == "-1":
                        print("| {:>3} ".format(" "), end=" ")
                    else:
                        print("| {:>3} ".format(self.the_list[k]), end="")
            k += 1
        print("|")

    def find_key(self, key):
        list_index_hash = int(key) % 61
        step_distance = 7 - (int(self.the_list[list_index_hash]) % 7)
        while self.the_list[list_index_hash] != "-1":
            if self.the_list[list_index_hash] == key:
                print(f"{key} in index {list_index_hash}")
                return self.the_list[list_index_hash]
            list_index_hash += step_distance
            list_index_hash %= self.list_size
        return False



if __name__ == "__main__":
    l_2 = ["100", "510", "170", "214", "268", "398",
           "235", "802", "900", "723", "699", "1", "16",
           "999", "890", "725", "998", "990", "989", "984",
           "320", "321", "400", "415", "450", "50", "660", "624"]

    hash_func = HashFunctions(61) #liczba peirwsza 61
    hash_func.dbl_hash_func(l_2)
    hash_func.find_key("170")