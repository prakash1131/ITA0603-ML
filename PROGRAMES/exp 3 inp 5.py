import pandas as pd
from math import log2

# ---------------------------------
# Employee Promotion Dataset
# ---------------------------------

data = {
    'Experience': [
        'High', 'High', 'Medium', 'Low', 'Medium',
        'Low', 'High', 'Medium', 'High', 'Low'
    ],

    'Performance': [
        'Excellent', 'Good', 'Good', 'Average', 'Excellent',
        'Poor', 'Good', 'Average', 'Excellent', 'Poor'
    ],

    'Leadership': [
        'Yes', 'Yes', 'No', 'No', 'Yes',
        'No', 'Yes', 'No', 'Yes', 'No'
    ],

    'Training': [
        'Yes', 'Yes', 'Yes', 'No', 'Yes',
        'No', 'No', 'Yes', 'Yes', 'Yes'
    ],

    'Promotion': [
        'Yes', 'Yes', 'Yes', 'No', 'Yes',
        'No', 'Yes', 'No', 'Yes', 'No'
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

def information_gain(data, attribute, target='Promotion'):

    total_entropy = entropy(data[target])

    weighted_entropy = 0

    for value in data[attribute].unique():

        subset = data[data[attribute] == value]

        weighted_entropy += (len(subset) / len(data)) * entropy(subset[target])

    return total_entropy - weighted_entropy


# ---------------------------------
# ID3 Algorithm
# ---------------------------------

def id3(data, original_data, features, target='Promotion', parent=None):

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

print("\nEMPLOYEE PROMOTION DATASET\n")

print(df)

print("\nGenerated Decision Tree\n")

print(tree)


# ---------------------------------
# Classify New Employee
# ---------------------------------

new_employee = {

    'Experience': 'Medium',

    'Performance': 'Excellent',

    'Leadership': 'Yes',

    'Training': 'Yes'

}

print("\nNew Employee Details")

print(new_employee)

prediction = predict(new_employee, tree)

print("\nPromotion Prediction :", prediction)
