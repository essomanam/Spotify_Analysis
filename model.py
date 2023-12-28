import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Dataset creation
X = pd.DataFrame(data =np.random.rand(10000,2),columns=['feat1','feat2'])
y = np.random.randint(0,2,10000)

cls = LogisticRegression()
# Training
cls.fit(X,y)

#Store the model
pickle.dump(cls, open('model.pkl','wb'))