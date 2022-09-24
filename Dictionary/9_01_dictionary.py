#dictionary

# dictionary can be created by {} or dict() function .
# dict() will return an empty dictionary

# 1. programming_dict=dict() 
# 2 .programming_dict={}

# dictionary look like this
# programming_dict={ "key1":"value1","key2":"value2","key3":"value3"}

programming_dict={}

# key - value can be directly entered in curly
programming_dict={"loop":"Help to run code mulyiple time"}  # but if we insertion by this method it will first empty the dictionary

# Key-Value pair in dictionary can be added using slice operator

programming_dict["Bug"]="A error in program"
programming_dict["Function"]="A piece of code that you ca easily call over and over again"


print(programming_dict)

# to access the item use key and square brackets
print(programming_dict["loop"])

# to empty a dictionary
# programming_dict={}

# print(programming_dict)

programming_dict["Bug"]="A error in program"
programming_dict["Function"]="A piece of code that you ca easily call over and over again"


# to update value in dictionary just use square braket
programming_dict["Bug"]="A moth in a computer"
print(programming_dict)

# Looping through dictionary
for thing in programming_dict: 
    print(thing)  # just print key in dictionary
    print(programming_dict[thing])


x=programming_dict.values()
print(type(x))
# print(programming_dict.keys())
# print(programming_dict.values())

# print(programming_dict.items())
