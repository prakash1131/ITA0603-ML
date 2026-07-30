
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High',   'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High',   'Strong', 'Cool', 'Same', 'Yes'],
    ['Rainy', 'Warm', 'Normal', 'Weak',   'Warm', 'Same', 'No'],
    ['Sunny', 'Warm', 'Normal', 'Weak',   'Warm', 'Same', 'Yes']
]

hypothesis = ['0'] * (len(data[0]) - 1)

print("Initial Hypothesis:")
print(hypothesis)
for sample in data:
    if sample[-1] == "Yes":      
        for i in range(len(hypothesis)):
            if hypothesis[i] == '0':
                hypothesis[i] = sample[i]
            elif hypothesis[i] != sample[i]:
                hypothesis[i] = '?'

        print("\nPositive Example:", sample[:-1])
        print("Updated Hypothesis:", hypothesis)

print("\nFinal Hypothesis:")
print(hypothesis)
