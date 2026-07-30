
data = [
    ['High', 'Good', 'Permanent', 'Yes', 'Young', 'Yes'],
    ['High', 'Good', 'Permanent', 'No', 'Middle', 'Yes'],
    ['Low', 'Poor', 'Temporary', 'No', 'Young', 'No'],
    ['Medium', 'Good', 'Permanent', 'Yes', 'Middle', 'Yes'],
    ['High', 'Average', 'Temporary', 'Yes', 'Old', 'No'],
    ['High', 'Good', 'Permanent', 'Yes', 'Middle', 'Yes']
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
