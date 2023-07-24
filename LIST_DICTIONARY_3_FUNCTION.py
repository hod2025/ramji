#for Dictionary and list function
my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict)

my_dict['Second'] = 'C++' #changing element
print(my_dict)

my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
a = my_dict.pop('Second') #pop element
print('Value:', a)
print('Dictionary:', my_dict)

b = my_dict.popitem() #pop the key-value pair
print('Key, value pair:', b)
print('Dictionary', my_dict)

print(my_dict.keys()) #get keys
print(my_dict.values()) #get values
print(my_dict.items()) #get key-value pairs

my_dict.clear() #empty dictionary
print(my_dict)

#for List Function 

my_list = [1, 2, 3, 'example', 3.132] #creating list with data
print(my_list)

my_list.append([555, 12]) #add as a single element
print(my_list)

my_list.extend([234, 'more_example']) #add as different elements
print(my_list)

my_list.insert(1, 'insert_example') #add element 
print(my_list)

del my_list[5] #delete element at index 5
print(my_list)

my_list.remove('example') #remove element with value
print(my_list)

