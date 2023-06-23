# import all libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('./data/winequality-red.csv', header=0)
# construct a dataframe using pandas

df = pd.DataFrame(data)
y = df['quality']
X = df.drop(columns=['quality'])

# Set the n_components=3
principal = PCA(n_components=3)
principal.fit(X)
x = principal.transform(X)

# Check the dimensions of data after PCA
print(x.shape)

plt.scatter(x[:, 1], x[:, 2], c=data['quality'], cmap='plasma', s=10)
plt.show()
