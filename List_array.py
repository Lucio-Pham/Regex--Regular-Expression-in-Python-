#tao ban sao cho list 
my_list = [1,2,4,'anh', '9']
my_duplicate_list = [item for item in my_list]
print ("original list", my_list)
print ("The first way to create duplicate list", my_duplicate_list)


#cach thu 2 
my_duplicate_list_2= list(my_list) 
print ("Second way to create duplicate list", my_duplicate_list_2)

#Cộng các element của 2 list 
#Lưu ý: không thể cộng các element khác kiểu
list_1= [1,2,4,5,6,7]
list_2= [4,5,7,11]
combine_list= [x+y for x, y in zip(list_1, list_2)] 
print (combine_list) #Kết quả trả về là 1 list mới, có số phần tử bằng số phần tử nhỏ hơn của 2 list thành phần

#cách khác để gộp các list
import operator
all_list= list(map(operator.add, list_1, list_2))
print(all_list)

#Dùng Numpy để cộng gộp 
#Gộp với numpy thì số phần tử trong 2 list phải bằng nhau (hai mảng cùng cấp) 
import numpy as np 
list_a= [1,2,4,5,6,7]
list_b= [4,6,8,9,3,8]

all_list_np= np.add(list_a, list_b) 
print(all_list_np)

#Kiểm tra 1 list là list rỗng hay không (empty) 
if len(list_a) ==0: 
    pass
#Hoặc cách khác: 
if list_a == []:
    pass
#Hoặc cách khác: 
if not list_a: 
    print('list rong')
else: 
    print ('list day')

#Tạo bản sao cho list (cloning) 
my_duplicate_list= [item for item in list_a]
print (my_duplicate_list)

#Hoặc cách khác
my_duplicate_list_2= list_a[:]
print(my_duplicate_list_2)

#Cách khác nữa 
my_duplicate_list_3= list(list_a)
print (my_duplicate_list_3) 

#Hoặc dùng hàm copy() 
my_duplicate_list_4= list_a.copy()
print (my_duplicate_list_4)

#import module copy 
import copy 
my_duplicate_list_5= copy.copy(list_a) 
print (my_duplicate_list_5) 

my_duplicate_list_6= copy.deepcopy(list_a) 
print (my_duplicate_list_6) 

#Hoặc chỉ đơn giản là multiplication với list 
my_duplicate_list_7= list_a*1
print(my_duplicate_list_7)


#Khôi phục phần tử sau cùng của list 
last_item= list_a[len(list_a)-1] 
#Đùng hàm pop()
last_item_1= list_a.pop()
#Dùng index lấy phần tử cuối cùng
last_item_2= list_a[-1]
#Hoặc dùng operator
*_, last_item_3= list_a

#Sắp xếp 1 list các string
my_list= ['anti-mage', 'Shadow Fiend', 'Injoker', 'Slitherine']
ls= sorted(my_list)

#Hoặc dùng casefold
ls_sorted= sorted(my_list, key=str.casefold) 

#dùng module locale
import locale
from functools import cmp_to_key
my_list_1=sorted(my_list, key=cmp_to_key(locale.strcoll))

#Hoặc cách khác
my_list_2= sorted(my_list, key=str.casefold, reverse=True) 

#Tìm giá trị thường gặp trong list 
print(max(set(my_list), key=my_list.count))

#Hoặc dùng module collections
from collections import Counter
cnt= Counter(my_list)
print(cnt.most_common(4)) 
#giá trị value trong hàm most_common(value) thể hiện số các giá trị phổ biến nhất trong list 
#list in ra màn hình thể hiện phần tử phổ biến nhất và số lần xuất hiện (đặt trong một set) 
#[('anti-mage', 1), ('Shadow Fiend', 1), ('Injoker', 1)]

list_n= [1,2,3,3,4,4,5,5,5,5,5,6,6,6,7,]
cmt= Counter(list_n) 
print(cmt.most_common(2)) #[(5, 5), (6, 3)]

#Đảo ngược vị trí string trong list 
list_rev= my_list[::-1]
print(list_rev) 

#phân tách thành phần của list bằng dấu phẩy
items= ['Kamehameda', 'Konoha', 'Kurama', 'Songoku']
print (','.join(items)) #in ra màn hình một chuỗi các string phân tách bởi dấu phẩy

#hoặc có thể dùng cho 1 list các chữ số
print(','.join(map(str, list_n))) #các số in ra màn hình định dạng là str

#mix data cũng tương tự 
mix_data= [('set', 'tuple'), (2,4), ('Wraith King', '9'), [2,2]]
print(','.join(map(str, mix_data)))
#Kết quả in ra màn hình: ('set', 'tuple'),(2, 4),('Wraith King', '9'),[2, 2]

#Sắp xếp list thành một chuỗi giảm dần
print(sorted(list_n, reverse=True))
#giá trị in ra màn hình: [7, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 3, 3, 2, 1]

#chuyển đổi chuỗi các từ trong list: dùng shuffle
from random import shuffle
noun_list= ['Kamehameda', 'Konoha', 'Kurama', 'Songoku']
shuffle(noun_list)
print (noun_list)
#giá trị in ra màn hình: ['Konoha', 'Songoku', 'Kamehameda', 'Kurama']

#Chương trình chuyển đổi list of character thành một chuỗi string 
character_a= ['Calculation', 'Jovahen', 'Kalos', 'Monohan', 'Dahan']
new_string= ''.join(character_a)
print(new_string) #giá trị in ra màn hình: CalculationJovahenKalosMonohanDahan

#Truy cập index của list 
#Dùng enumerate
noun_list= ['Kamehameda', 'Konoha', 'Kurama', 'Songoku']
for noun_list_index, noun_list_val in enumerate(noun_list): 
    print(noun_list_index, noun_list_val) 
    #Giá trị in ra màn hình: 
    #0 Kamehameda
    #1 Konoha
    #2 Kurama
    #3 Songoku

#Hoán vị các phần tử trong list (permutation) 
import itertools
print (list(itertools.permutations(['Kamehameda', 'Konoha', 'Kurama', 'Songoku']))

