f=open("mytext.txt","r")
print(f.read(5))
print(f.readline())
for x in f:
  print(x)
