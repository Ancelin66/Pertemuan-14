#konversi List menjadi Set
print("=== Konversi List → Set ===")
list_data = [1, 2, 2, 3, 4, 4, 5]
print("Sebelum (List):", list_data)
set_from_list = set(list_data)
print("Sesudah (Set):", set_from_list)

#konversi Set menjadi List
print("\n=== Konversi Set → List ===")
set_data = {10, 20, 30, 40, 50}
print("Sebelum (Set):", set_data)
list_from_set = list(set_data)
print("Sesudah (List):", list_from_set)

#konversi Tuple menjadi Set
print("\n=== Konversi Tuple → Set ===")
tuple_data = ('a', 'b', 'a', 'c', 'd', 'c')
print("Sebelum (Tuple):", tuple_data)
set_from_tuple = set(tuple_data)
print("Sesudah (Set):", set_from_tuple)

#konversi Set menjadi Tuple
print("\n=== Konversi Set → Tuple ===")
set_data_2 = {'x', 'y', 'z'}
print("Sebelum (Set):", set_data_2)
tuple_from_set = tuple(set_data_2)
print("Sesudah (Tuple):", tuple_from_set)
