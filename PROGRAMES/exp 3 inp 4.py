import pandas as pd
from math import log2

# ---------------------------------
# Disease Diagnosis Dataset
# ---------------------------------

data = {
    'Fever': [
        'Yes', 'Yes', 'No', 'Yes', 'No',
        'Yes', 'No', 'Yes', 'Yes', 'No'
    ],

    'Cough': [
        'Yes', 'Yes', 'Yes', 'No', 'No',
        'Yes', 'Yes', 'No', 'Yes', 'No'
    ],

    'Headache': [
        'Yes', 'No', 'Yes', 'Yes', 'No',
        'Yes', 'No', 'No', 'Yes', 'Yes'
    ],

    'BodyPain': [
        'Yes', 'Yes', 'No', 'Yes', 'No',
        'No', 'Yes', 'Yes', 'Yes', 'No'
    ],

    'Disease': [
        'Positive', 'Positive', 'Negative', 'Positive', 'Negative',
        'Positive', 'Negative', 'Positive', 'Positive', 'Negative'
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

def information_gain(data, attribute, target='Disease'):

    total_entropy = entropy(data[target])

    weighted_entropy = 0

    for value in data[attribute].unique():

        subset = data[data[attribute] == value]

        weighted_entropy += (len(subset) / len(data)) * entropy(subset[target])

    return total_entropy - weighted_entropy


# ---------------------------------
# ID3 Algorithm
# ---------------------------------

def id3(data, original_data, features, target='Disease', parent=None):

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

print("\nDISEASE DIAGNOSIS DATASET\n")

print(df)

print("\nGenerated Decision Tree\n")

print(tree)


# ---------------------------------
# Classify New Patient
# ---------------------------------

new_patient = {

    'Fever': 'Yes',

    'Cough': 'Yes',

    'Headache': 'No',

    'BodyPain': 'Yes'

}

print("\nNew Patient Details")

print(new_patient)

prediction = predict(new_patient, tree)

print("\nDisease Prediction :", prediction)
