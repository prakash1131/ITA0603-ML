data = [
    ['Sunny','Warm','Normal','Yes'],
    ['Sunny','Warm','High','Yes'],
    ['Rainy','Cold','High','No'],
    ['Sunny','Warm','High','Yes']
]
h = ['0'] * (len(data[0]) - 1)
for row in data:
    if row[-1] == 'Yes':
        if h[0] == '0':
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(h)
print("Final Hypothesis:", h)
