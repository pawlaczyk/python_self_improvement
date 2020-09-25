class HashFunction:

    def __init__(self, size):
        self.list_size = size
        self.the_list = ["-1" for i in range(size)]

    def hash_str(selfself, str_to_hash):
        hash_val = 0
        hash_sum = 0
        for i in range(len(str_to_hash)):
            # liczba liter
            char_code = ord(str_to_hash[i]) - 96 # ord("a") == 96
            hkv_tmp = hash_val # hash key value
            hash_sum += (hash_val * 27 + char_code) # 27 liter w alfabecie
        return hash_sum

    def hash_str_list(self, str_list):
        for str_to_hash in str_list:
            hash_sum = self.hash_str(str_to_hash)
            step_distance = 7 - (hash_sum % 7)
            while self.the_list[hash_sum] != "-1":
                hash_sum += step_distance #kolejny indeks gdy sa konflikty
                hash_sum %= self.list_size
            self.the_list[hash_sum] = str_to_hash

    def find(self, value):
        value_index = self.hash_str(value)
        step_distance = 7 - (value_index % 7)
        while self.the_list[value_index] != "-1":
            if self.the_list[value_index] == value:
                print(f"{value} in index: {value_index}")
                return self.the_list[value_index]
            value_index += step_distance
            value_index %= self.list_size # jeśli wyjdziemy po za elemnty listy
        return False

    def print_list(self):
        # Used to print each row of columns 10 at a time
        increment = 0
        # I want to allow for 10 columns per row
        num_of_rows = int((self.list_size / 10) + 1)
        for j in range(num_of_rows):
            self.print_line(78)
            # Get the next row of columns to print
            increment += 10
            # Print a row of indexes and then a row of data
            self.print_row(increment, False)
            self.print_line(78)
            self.print_row(increment, True)
        self.print_line(78)

    # Print a horizontal line for the table
    def print_line(self, num_of_lines):
        for l in range(num_of_lines):
            print("-", end="")
        print()

    # Used to print indexes and data for the table
    # Receives the row of data to print and whether it is data
    # or indexes
    def print_row(self, increment, is_data):
        k = increment - 10
        while k <= increment:
            # If past the end of the array print blank spaces
            if k > self.list_size - 1:
                print("|     ", end=" ")
            else:
                if not is_data:
                    # Print value with 3 spaces and right justify
                    # Print index numbers
                    print("| {:>3} ".format(k), end=" ")
                else:
                    # Print list data values or nothing if -1
                    if self.the_list[k] == "-1":
                        print("| {:>3} ".format(" "), end=" ")
                    else:
                        print("| {:>3} ".format(self.the_list[k]), end=" ")
            k += 1
        print("|")

if __name__ == "__main__":
    words_to_add = ["ace", "act", "add", "age", "ago", "aid", "aim", "air", "all", "amp", "and", "ant", "any", "ape",
                    "apt", "arc", "are", "ark", "arm", "art", "ash", "ask", "asp", "ate", "atm", "awe", "axe", "aye"]

    hash_func = HashFunction(61) #prime number
    hash_func.hash_str_list(words_to_add)
    hash_func.print_list()
    hash_func.find("ask")