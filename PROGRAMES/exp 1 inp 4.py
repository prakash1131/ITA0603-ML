
data = [
    ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Positive'],
    ['Yes', 'Yes', 'No',  'Yes', 'Yes', 'Positive'],
    ['No',  'Yes', 'Yes', 'No',  'No',  'Negative'],
    ['Yes', 'Yes', 'Yes', 'No',  'Yes', 'Positive'],
    ['No',  'No',  'Yes', 'Yes', 'No',  'Negative'],
    ['Yes', 'Yes', 'No',  'No',  'Yes', 'Positive']
]
hypothesis = ['0'] * (len(data[0]) - 1)

print("Initial Hypothesis:")
print(hypothesis)

for sample in data:
    if sample[-1] == 'Positive':      
        for i in range(len(hypothesis)):
            if hypothesis[i] == '0':
                hypothesis[i] = sample[i]
            elif hypothesis[i] != sample[i]:
                hypothesis[i] = '?'

        print("\nPositive Example:", sample[:-1])
        print("Updated Hypothesis:", hypothesis)

print("\nFinal Hypothesis:")
print(hypothesis)
