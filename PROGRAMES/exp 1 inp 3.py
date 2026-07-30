
data = [
    ['High', 'Good', 'Yes', 'Good', 'High', 'Yes'],
    ['High', 'Excellent', 'Yes', 'Good', 'High', 'Yes'],
    ['Medium', 'Average', 'No', 'Average', 'Medium', 'No'],
    ['High', 'Good', 'Yes', 'Excellent', 'High', 'Yes'],
    ['Low', 'Poor', 'No', 'Average', 'Low', 'No'],
    ['High', 'Good', 'Yes', 'Good', 'Medium', 'Yes']
]

hypothesis = ['0'] * (len(data[0]) - 1)

print("Initial Hypothesis:")
print(hypothesis)
for sample in data:
    if sample[-1] == 'Yes':    
        for i in range(len(hypothesis)):
            if hypothesis[i] == '0':
                hypothesis[i] = sample[i]
            elif hypothesis[i] != sample[i]:
                hypothesis[i] = '?'

        print("\nPositive Example:", sample[:-1])
        print("Updated Hypothesis:", hypothesis)

print("\nFinal Hypothesis:")
print(hypothesis)
