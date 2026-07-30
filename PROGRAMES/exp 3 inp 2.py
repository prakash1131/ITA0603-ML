import pandas as pd
from math import log2

# ---------------------------------
# Student Placement Dataset
# ---------------------------------

data = {
    'CGPA': [
        'High', 'High', 'Medium', 'Medium', 'Low',
        'High', 'Low', 'Medium', 'High', 'Low'
    ],

    'Communication': [
        'Good', 'Excellent', 'Good', 'Average', 'Poor',
        'Good', 'Average', 'Good', 'Excellent', 'Poor'
    ],

    'Internship': [
        'Yes', 'Yes', 'Yes', 'No', 'No',
        'No', 'No', 'Yes', 'Yes', 'Yes'
    ],

    'Programming': [
        'Good', 'Excellent', 'Good', 'Average', 'Poor',
        'Good', 'Average', 'Excellent', 'Good', 'Average'
    ],

    'Placement': [
        'Yes', 'Yes', 'Yes', 'No', 'No',
        'Yes', 'No', 'Yes', 'Yes', 'No'
    ]
}

df = pd.DataFrame(data)

# ---------------------------------
# Entropy Function
# ---------------------------------

def entropy(target):

    values = target.value_counts()

    total = len(target)

    ent = 0

    for count in values:

        p = count / total

        ent -= p * log2(p)

    return ent

# ---------------------------------
# Information Gain
# ---------------------------------

def information_gain(data, attribute, target='Placement'):

    total_entropy = entropy(data[target])

    values = data[attribute].unique()

    weighted_entropy = 0

    for value in values:

        subset = data[data[attribute] == value]

        weighted_entropy += (len(subset) / len(data)) * entropy(subset[target])

    gain = total_entropy - weighted_entropy

    return gain

# ---------------------------------
# ID3 Algorithm
# ---------------------------------

def id3(data, original_data, features, target='Placement', parent=None):

    if len(data[target].unique()) == 1:

        return data[target].iloc[0]

    elif len(data) == 0:

        return original_data[target].mode()[0]

    elif len(features) == 0:

        return parent

    parent = data[target].mode()[0]

    gains = []

    for feature in features:

        gains.append(information_gain(data, feature, target))

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

# ---------------------------------
# Prediction Function
# ---------------------------------

def predict(sample, tree):

    if not isinstance(tree, dict):

        return tree

    root = next(iter(tree))

    value = sample[root]

    if value in tree[root]:

        return predict(sample, tree[root][value])

    else:

        return "Unknown"

# ---------------------------------
# Build Decision Tree
# ---------------------------------

features = list(df.columns[:-1])

tree = id3(df, df, features)

print("\nSTUDENT PLACEMENT DATASET\n")

print(df)

print("\nGenerated Decision Tree\n")

print(tree)

# ---------------------------------
# Classify New Sample
# ---------------------------------

new_student = {

    'CGPA': 'High',

    'Communication': 'Excellent',

    'Internship': 'Yes',

    'Programming': 'Excellent'

}

print("\nNew Student Details")

print(new_student)

prediction = predict(new_student, tree)

print("\nPlacement Prediction :", prediction)
