import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix, accuracy_score

data = pd.read_csv('dataset.csv')
x = pd.DataFrame(data.iloc[:,1:4].values)
y = data.iloc[:,4].values
lblen = LabelEncoder()
x.loc[:,0] = lblen.fit_transform(x.loc[:,0])
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=0)
sc = StandardScaler()
xtrain = sc.fit_transform(xtrain)
xtest = sc.transform(xtest)

classi = Sequential()
classi.add(Dense(6, activation = 'relu',input_dim = 3))
classi.add(Dense(6, activation = 'relu'))
classi.add(Dense(1, activation = 'sigmoid'))
classi.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
classi.fit(xtrain, ytrain, batch_size = 2, epochs = 5)
ypred = classi.predict(xtest)
ypred = (ypred > 0.5)
cmatrix = confusion_matrix(ytest, ypred)
print(cmatrix)
accuracy_score(ytest,ypred)