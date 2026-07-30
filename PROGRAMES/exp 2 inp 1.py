data=[
    ['Sunny','Warm','Yes'],
    ['Sunny','Cold','Yes'],
    ['Rainy','Warm','No'],
    ['Sunny','Warm','Yes']
]
S=data[0][:-1]
G=['?']*len(S)
for x in data:
    if x[-1]=='Yes':
        for i in range(len(S)):
            if S[i]!=x[i]:
                S[i]='?'
    else:
        for i in range(len(S)):
            if S[i]!=x[i]:
                G[i]=S[i]
    print("S=",S,"G=",G)
print("Final S=",S)
print("Final G=",G)
