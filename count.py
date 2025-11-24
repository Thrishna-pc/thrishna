text="this is a simple line this is a text "
word=text.split()
counts={}
for i in word:
    counts[i]=counts.get(i,0)+1
print(counts)
