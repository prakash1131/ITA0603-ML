# Candidate Elimination Algorithm - Disease Diagnosis Dataset

import copy

# Training Dataset
data = [
    ['Yes', 'Yes', 'Yes', 'Yes', 'Positive'],
    ['Yes', 'Yes', 'No',  'Yes', 'Positive'],
    ['No',  'Yes', 'Yes', 'No',  'Negative'],
    ['Yes', 'No',  'Yes', 'Yes', 'Positive'],
    ['No',  'No',  'No',  'No',  'Negative'],
    ['Yes', 'Yes', 'Yes', 'No',  'Positive'],
    ['No',  'Yes', 'No',  'Yes', 'Negative'],
    ['Yes', 'No',  'No',  'Yes', 'Positive'],
    ['Yes', 'Yes', 'Yes', 'Yes', 'Positive'],
    ['No',  'No',  'Yes', 'No',  'Negative']
]

num_attr = len(data[0]) - 1

# Initialize Specific and General Hypotheses
S = ['0'] * num_attr
G = [['?'] * num_attr]

print("Initial Specific Hypothesis (S):", S)
print("Initial General Hypothesis (G):", G)

for sample in data:
    attributes = sample[:-1]
    target = sample[-1]

    if target == "Positive":
        G = [g for g in G if all(g[i] == '?' or g[i] == attributes[i]
                                 for i in range(num_attr))]

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

    print("\nTraining Example:", sample)
    print("S =", S)
    print("G =", G)

print("\nFinal Specific Hypothesis (S):")
print(S)

print("\nFinal General Hypotheses (G):")
for g in G:
    print(g)
