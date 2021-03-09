#tao ban sao cho list 
my_list = [1,2,4,'anh', '9']
my_duplicate_list = [item for item in my_list]
print ("original list", my_list)
print ("The first way to create duplicate list", my_duplicate_list)


#cach thu 2 
my_duplicate_list_2= list(my_list) 
print ("Second way to create duplicate list", my_duplicate_list_2)