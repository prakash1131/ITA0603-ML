# Candidate Elimination Algorithm

import copy

# Dataset
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Same', 'Yes'],
    ['Rainy', 'Warm', 'Normal', 'Weak', 'Warm', 'Same', 'No'],
    ['Sunny', 'Warm', 'Normal', 'Weak', 'Warm', 'Same', 'Yes'],
    ['Cloudy', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Cold', 'High', 'Weak', 'Cool', 'Change', 'No']
]

num_attr = len(data[0]) - 1

# Initialize S and G
S = ['0'] * num_attr
G = [['?'] * num_attr]

print("Initial S:", S)
print("Initial G:", G)

for sample in data:
    attributes = sample[:-1]
    target = sample[-1]

    if target == "Yes":
        G = [g for g in G if all(g[i] == '?' or g[i] == attributes[i] for i in range(num_attr))]

        # Update S
        for i in range(num_attr):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = '?'

    else:
        G_new = []
        for g in G:
            for i in range(num_attr):
                if g[i] == '?':
                    if S[i] != '?' and S[i] != '0':
                        new_g = copy.deepcopy(g)
                        new_g[i] = S[i]
                        if new_g not in G_new:
                            G_new.append(new_g)
        G = G_new

    print("\nExample:", sample)
    print("S =", S)
    print("G =", G)

print("\nFinal Specific Hypothesis (S):")
print(S)

print("\nFinal General Hypotheses (G):")
for g in G:
    print(g)
