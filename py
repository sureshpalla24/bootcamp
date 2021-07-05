



import hashlib

m = hashlib.md5()
text = input("enter a string")
m.update(text.encode('utf-8'))   
print(m.hexdigest())
