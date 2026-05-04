a=(2,4,5,)
print(type(a))
b=(34,35,3555.45,'hello',True)
# b[1]=343353535
print(b) # we cannot change the tuple values as they are immutable
i=a.index(4)
print (i)
repeated = b * 3
print(repeated)

slice=b[1:4]
print(slice)