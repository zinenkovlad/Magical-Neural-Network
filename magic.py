import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

data_raw = pd.read_csv('zodiacs.csv', header=0, index_col=0)
data = pd.get_dummies(data_raw, prefix='is')

X = data.iloc[:, :2].values
y = data.iloc[:, 2:].values

model = Sequential()
model.add(Dense(5, input_dim=2, activation='relu'))
model.add(Dense(7, activation='relu'))
model.add(Dense(12, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=150, batch_size=10)

scores = model.evaluate(X, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))