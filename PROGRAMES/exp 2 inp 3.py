# Candidate Elimination Algorithm - Loan Approval Dataset

import copy

# Training Dataset
data = [
    ['High',   'Good',    'Permanent', 'Yes', 'Young',  'Yes'],
    ['High',   'Good',    'Permanent', 'No',  'Middle', 'Yes'],
    ['Low',    'Poor',    'Temporary', 'No',  'Young',  'No'],
    ['Medium', 'Good',    'Permanent', 'Yes', 'Middle', 'Yes'],
    ['High',   'Average', 'Temporary', 'Yes', 'Old',    'No'],
    ['Medium', 'Good',    'Permanent', 'No',  'Young',  'Yes'],
    ['Low',    'Good',    'Permanent', 'Yes', 'Middle', 'Yes'],
    ['Low',    'Poor',    'Temporary', 'Yes', 'Old',    'No']
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

    if target == "Yes":

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
