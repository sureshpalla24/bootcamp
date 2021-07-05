import hashlib
m = hashlib.sha256()
m.update(b"Hello this is jayraj")
m.update(b" good morning")
print(m.digest())

h = hashlib.new('sha512')
h.update(b"what is your name")
print(h.hexdigest())

m = hashlib.md5()
text = input("enter a string")
m.update(text.encode('utf-8'))   
print(m.hexdigest())
