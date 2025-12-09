num1 = 11
num2 = num1

print(f"the value of num1 = {num1}")
print(f"the value of num2 = {num2}")

print(f"the num1 point to = {id(num1)}")
print(f"the num2 point to = {id(num2)}")

num2 = 22
print("\nAfter num2 value updated:")
print(f"the value of num1 = {num1}")
print(f"the value of num2 = {num2}")

print(f"the num1 point to = {id(num1)}")
print(f"the num2 point to = {id(num2)}")

print("\n############")
dict1 = {"value": 11}
dict2 = dict1

print("\nBefore dict1 value updated:")
print(f"the value of dict1 = {dict1}")
print(f"the value of dict2 = {dict2}")

print(f"the dict1 point to = {id(dict1)}")
print(f"the dict2 point to = {id(dict2)}")

dict2["value"] = 22
print("\nAfter dict1 value updated:")
print(f"the value of dict1 = {dict1}")
print(f"the value of dict2 = {dict2}")

print(f"the dict1 point to = {id(dict1)}")
print(f"the dict2 point to = {id(dict2)}")

dict2["aaa"] = 1
print(f"the dict2 point to = {len(dict2)}")
print(f"the dict2 point to = {id(dict2)}")
