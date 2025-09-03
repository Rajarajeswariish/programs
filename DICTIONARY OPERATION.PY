
print("\n\t\t DICTIONARY OPERATION")
print("\n\t\t~~~~~~~~~~~~~~~~~~~~~~")
my_dict={"name":"Rajarajeswari","age":"city"}
my_dict=dict(name="Rajarajeswari",age="18",city="tiruchirapalli")
print("\nmy_dict",my_dict)
print("\nmy_dict[name]",my_dict)
print("\nUpdate age as 18 ",my_dict)
my_dict["age"]=18

print("\nnow my_dict", my_dict)
print("\nDelete city in my_dict",my_dict)

del my_dict["city"]
print("\nmy_dict",my_dict)
print("\nname" in my_dict)

print("\nAddress in my_dict",my_dict)
print("\nAddress" in my_dict)

print("\nKeys" in my_dict)
print("\nname" in my_dict)
for keys in my_dict:
   print(keys)
   
print("\nKey value pairs in my_dict")
for key,values in my_dict.items():
  print(key,values)

print("\nnumber of values in my_dict",len(my_dict))

