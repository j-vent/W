#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import time
from sklearn.preprocessing import PolynomialFeatures

test = []

class LinearRegressor:

    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        self.w = 0
        self.stepsize = 0
        self.g = 0

    def __str__(self):
        string = "w = "+str(self.w)
        return string

    def mb_update(self,batch_size,epochs):
        # uses mini-batch gradient descent to update param w

        # indexes is used to randomly choose values from dataset 
        # D = (x_i,y_i)
        indexes = [i for i in range(0,len(self.Y))]

        for p in range(epochs):
            epoch_start_time = time.time()
            random.shuffle(indexes)
            load_string = ""

            for k in range((((p+1)*batch_size)-batch_size),(p+1)*batch_size):
                self.g = ((self.X[k]*self.w) -self.Y[k])*self.X[k]
                self.stepsize = 1/(p+1)
                self.w = self.w - (self.stepsize*self.g)
                load_string = self.load_graphic(batch_size,epochs,p,k)
                print(load_string,end="\r")

            time_string = load_string+" time: "+str(round(time.time()-epoch_start_time,4))+" seconds"
            print(time_string)

    def load_graphic(self,batch_size,epochs,epoch,iteration):

        # function to show loading animation
        padding = ""
        extra_padding_amount = 1
        max_load = 30
        percent = ""
        load_string = "["
        end_string = "\r"
        
        # adds padding to make animations look better
        for i in range(len(str(epochs))-len(str(epoch+1))+extra_padding_amount):
            padding += " "
        string = "epoch "+str(epoch+1)+"/"+str(epochs)+":"+padding

        # loading animation
        for i in range((iteration*max_load)//batch_size):
            load_string += "\u2580"

        # unloaded part
        for i in range(20-((iteration*max_load)//batch_size)-1):
            load_string += " "
        load_string += "]"

        return string+load_string

def format_dates(data):
    # function to convert dates to numbers between 0-364
    # returns csv with formated numbers
    
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    fixed_dates = []
    
    for i in range(len(data[1])-1):

        date = data[1][i].split("/")
        fixed_dates.append(date)

    fixed_df = data
    fixed_df["Fixed Dates"] = fixed_dates

    return fixed_df

def main():

    # creating dataframe w/ pandas
    csv_name = "/home/ryans/Projects/HackedProject/edmonton_shelters.csv"
    dates = [31,28,31,30,31,30,31,31,30,31,30,31]
    shelters_df = pd.read_csv(csv_name,",").dropna()
    shelters_df["Ratio"] = shelters_df["Overnight"]/shelters_df["Capacity"]
    #jl = format_dates(shelters_df)
    #shelters_df["Day"] = sum(dates[0:int(shelters_df["Date"].str.split("/")[0])-1]) + int(shelters_df["Date"].str.split("/")[1])
    temp = shelters_df["Date"].str.split("/")
    print(temp[0])

    #X = shelters_df["Day"]
    #Y = shelters_df["Ratio"]

    #model = LinearRegressor(X,Y)
    #batch_size = len(X)
    #epochs = 20

    #model.mb_update(batch_size,epochs)
    #print(model)

    #plt.plot(X,Y,"o")
    #plt.show()

main()
