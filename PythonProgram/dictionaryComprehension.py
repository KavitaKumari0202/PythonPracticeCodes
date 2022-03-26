my_list=[18,15,13,4,6,5,31]
dct={i:('even' if (i%2==0) else 'odd') for i in my_list}
print(dct)
my_list=[18,15,13,4,6,5,31]
my_dict_even={i:'even' for i in my_list if (i%2==0)}
print(my_dict_even)
my_dict_odd={i:'odd' for i in my_list if (i%2!=0)}
print(my_dict_odd)