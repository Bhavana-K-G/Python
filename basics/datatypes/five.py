#bytes and bytearray?
#represents group of elements inbetweeen o to 255
size = [38,40,0,255]
b = bytes(size)

print(size)
print(b)

for value in b:
    print(value)

print(type(size))
print(type(b))


ba=bytearray(size)
print(ba)
#print byte array values 
for value in ba:
    print(value)
print(type(ba))