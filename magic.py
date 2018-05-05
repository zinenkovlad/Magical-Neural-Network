import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import to_categorical
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# random seed for reproducibility
seed = 7


# function to create model, required for KerasClassifier
def create_model():
    model = Sequential()
    model.add(Dense(5, input_shape=(2,), activation='relu'))
    model.add(Dense(7, activation='relu'))
    model.add(Dense(9, activation='sigmoid'))         # add one more Dense
    model.add(Dense(12, activation='softmax'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# load dataset
data_raw = pd.read_csv('zodiacs.csv', header=0, index_col=0)
# prepare data
data = pd.get_dummies(data_raw, prefix='is')
# split into input (X) and output (Y) variables
X = data.iloc[:, :2].values
y = data.iloc[:, 2:].values

# create model
model = KerasClassifier(build_fn=create_model, epochs=150, batch_size=10, verbose=0)
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

# evaluate using 10-fold cross validation
results = cross_val_score(model, X, y, cv=kfold)
print(results.mean())
