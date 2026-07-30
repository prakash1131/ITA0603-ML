from sklearn.tree import DecisionTreeClassifier

# Training data
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Target labels
y = ['No', 'No', 'Yes', 'Yes']

# Create Decision Tree using ID3 (Entropy)
clf = DecisionTreeClassifier(criterion='entropy')

# Train the model
clf.fit(X, y)

# Predict a new sample
prediction = clf.predict([[1, 0]])

print("Prediction:", prediction[0])
