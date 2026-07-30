import pandas as pd
from math import log2

# ----------------------------
# Play Tennis Dataset
# ----------------------------

data = {
    'Outlook': [
        'Sunny','Sunny','Overcast','Rain','Rain','Rain',
        'Overcast','Sunny','Sunny','Rain','Sunny',
        'Overcast','Overcast','Rain'
    ],

    'Temperature': [
        'Hot','Hot','Hot','Mild','Cool','Cool',
        'Cool','Mild','Cool','Mild','Mild',
        'Mild','Hot','Mild'
    ],

    'Humidity': [
        'High','High','High','High','Normal','Normal',
        'Normal','High','Normal','Normal','Normal',
        'High','Normal','High'
    ],

    'Wind': [
        'Weak','Strong','Weak','Weak','Weak','Strong',
        'Strong','Weak','Weak','Weak','Strong',
        'Strong','Weak','Strong'
    ],

    'PlayTennis': [
        'No','No','Yes','Yes','Yes','No',
        'Yes','No','Yes','Yes','Yes',
        'Yes','Yes','No'
    ]
}

df = pd.DataFrame(data)

# ----------------------------
# Entropy Function
# ----------------------------

def entropy(target):
    values = target.value_counts()
    total = len(target)

    ent = 0

    for count in values:
        p = count / total
        ent -= p * log2(p)

    return ent

# ----------------------------
# Information Gain
# ----------------------------

def information_gain(data, attribute, target='PlayTennis'):

    total_entropy = entropy(data[target])

    values = data[attribute].unique()

    weighted_entropy = 0

    for value in values:

        subset = data[data[attribute] == value]

        weighted_entropy += (len(subset) / len(data)) * entropy(subset[target])

    return total_entropy - weighted_entropy

# ----------------------------
# ID3 Algorithm
# ----------------------------

def id3(data, original_data, features, target='PlayTennis', parent=None):

    # All examples belong to one class
    if len(data[target].unique()) == 1:
        return data[target].iloc[0]

    # Empty dataset
    elif len(data) == 0:
        return original_data[target].mode()[0]

    # No features left
    elif len(features) == 0:
        return parent

    # Parent node
    parent = data[target].mode()[0]

    # Best feature
    gains = [information_gain(data, feature, target) for feature in features]

    best_feature = features[gains.index(max(gains))]

    tree = {best_feature: {}}

    remaining_features = [f for f in features if f != best_feature]

    for value in data[best_feature].unique():

        subset = data[data[best_feature] == value]

        subtree = id3(
            subset,
            original_data,
            remaining_features,
            target,
            parent
        )

        tree[best_feature][value] = subtree

    return tree

# ----------------------------
# Predict Function
# ----------------------------

def predict(sample, tree):

    if not isinstance(tree, dict):
        return tree

    root = next(iter(tree))

    value = sample[root]

    if value in tree[root]:
        return predict(sample, tree[root][value])

    return "Unknown"

# ----------------------------
# Build Decision Tree
# ----------------------------

features = list(df.columns[:-1])

tree = id3(df, df, features)

print("\nPLAY TENNIS DATASET\n")
print(df)

print("\nGenerated Decision Tree\n")
print(tree)

# ----------------------------
# New Sample Classification
# ----------------------------

new_sample = {
    'Outlook': 'Sunny',
    'Temperature': 'Cool',
    'Humidity': 'High',
    'Wind': 'Strong'
}

print("\nNew Sample")
print(new_sample)

result = predict(new_sample, tree)

print("\nPrediction :", result)
