a = ['this is my sentence', 'my word is good','good is bad','my sentence is bad']
b = ['my','sentence','good','bad']
c = [s for s in a if any(xs in s for xs in b)]
print(c)
