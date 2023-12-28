#!/usr/bin/env python
# coding: utf-8

# In[24]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.layers import Conv1D,MaxPooling1D
from tensorflow.keras.optimizers import Adam


print(tf.__version__)

import pandas as pd
import numpy as np
from sklearn import  metrics
from sklearn.model_selection import train_test_split

asthma=pd.read_csv("data.csv")
X=asthma.drop(columns=['PEFR'])
X.head()
y=asthma['PEFR']
X = np.array(X)
X = X.reshape(X.shape[0], X.shape[1], 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
model = Sequential()
model.add(Conv1D(filters=64, kernel_size=3, activation='relu' ))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(1, activation='linear'))


# Compile the model with mean squared error loss
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0,validation_data=(X_test, y_test))

# Evaluate the model on the test set and calculate the MSE percentage
mse = model.evaluate(X_test, y_test)
mse_percent =( mse / int(tf.reduce_mean(y_test))**2) * 100
x=np.sqrt(mse_percent)





# In[25]:


model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the model
model.fit(X_train, y_train, epochs=30, validation_data=(X_test, y_test))

# Evaluate the model
loss, mae = model.evaluate(X_test, y_test)
y_test_float = tf.cast(y_test, dtype=tf.float32)
mae_percentage = (int(mae) / tf.math.reduce_variance(y_test_float))*100
mae_percentage
# Make predictions
print(X_test.shape)

predictions = model.predict(X_test)


# In[26]:


mae_percentage.numpy()


# In[27]:





# In[28]:







