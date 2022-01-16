#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from sklearn.linear_model import LinearRegression

class LinearRegressor:

    def __init__(self,X,Y,d):
        self.X = X
        self.Y = Y
        self.d = d+1
        self.w = [0.5 for i in range(self.d)]
        self.stepsize = 0
        self.g = [0 for i in range(self.d)]

    def __str__(self):
        string = "w = "+str(self.w)
        return string

    def epoch(self,batch_size,epoch):
        # uses mini-batch gradient descent to update param w

        # indexes is used to randomly choose values from dataset 
        # D = (x_i,y_i)
        indexes = [i for i in range(0,len(self.Y))]

        for p in range(batch_size//len(self.X)):
            random.shuffle(indexes)

            for k in range(p*batch_size,batch_size+(p*batch_size)-1):
                self.g = (([i*self.w for i in range(len([self.X[k]]))]) -self.Y)*self.X[k]
                self.stepsize = 1/(p+1)
                self.w = self.w - ([i*self.stepsize for i in range(len(self.g))])


    def update(self,batch_size,epochs):
        for i in range(epochs):
            self.epoch(batch_size,i)


def main():

    # creating dataframe w/ pandas
    csv_name = "fixed.csv"
    new_csv = "model_csv.csv"
    shelters_df = pd.read_csv(csv_name,",")
    shelters_df = shelters_df[shelters_df["Ratio"].notna()]
    shelters_df = shelters_df[shelters_df["Day"].notna()]
    
    i = pd.IndexSlice
    X = np.array(shelters_df["Day"].tolist()).reshape(1,-1)
    Y = np.array(shelters_df["Ratio"].tolist()).reshape(1,-1)
    d = 1 #linear reg

    regressor = LinearRegression()
    regressor.fit(X,Y)
    prediction = regressor.intercept_ + (regressor.coef_ * X)

    shelters_df = shelters_df.drop("Ratio",1)
    shelters_df["Rating"] = pd.Series(prediction[0])
    shelters_df = shelters_df.dropna()
    shelters_df.sort_values(by=["Rating"],inplace=True,ascending=False)
    shelters_df.to_csv(new_csv,",")

    #model = LinearRegressor(X,Y,d)

    #batch_size = len(X)
    #epochs = 5
    
    #model.update(batch_size,epochs)
    #print(model)

    #plt.plot(X,Y,"o")
    #plt.show()

main()
