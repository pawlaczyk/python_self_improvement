#function argument unpacking
#https://www.youtube.com/watch?time_continue=4&v=YWY4BZi_o28
# wypakowawywanie - operator gwiazdki
def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))
​
​
print_vector(0, 1, 0) 
​
​
tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]
​
print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])
print_vector(*tuple_vec) # wypakowanie elementów z typli
print_vector(*list_vec) # wypakowanie elementów z listy
​
gen_expr = ( x*x for x in range(3))
print_vector(*gen_expr) # wypakowanie elementów z generatora
​
​
dict_vec = {'x':1 , 'y': 0, 'z': 1}
# uwaga w przypadku słowników nie ma gwarancji co do kolejnosci wypakowaywania elementów
print_vector(**dict_vec) # wypakowanie elementów ze słownika - dwie **
Colla