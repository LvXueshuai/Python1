import hashlib

obj = hashlib.md5()

obj.update("hello".encode("utf8"))

print(obj.hexdigest())
