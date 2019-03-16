#____________________________________________MODULES____________________________________________________
import pandas as pd
#_______________________________________________________________________________________________________

#___________________________________________FUNCTIONS____________________________________________________
def BuildResults(totalMonth,profitLossSum,averageChange,maxIncrease,maxDecrease):
    m1 = maxIncrease.iloc[0,0]
    v1 = maxIncrease.iloc[0,1]
    m2 = maxDecrease.iloc[0,0]
    v2 = maxDecrease.iloc[0,1]
    myString = "Finincial Analysis\r\n------------------\r\n" + \
               "Total months: " + str(totalMonth) + "\r\n" + \
               "Total: $" + str(profitLossSum) + "\r\n" + \
               "Average change: $" + str(averageChange) + "\r\n" + \
               "Greatest Increase in Profits: " + str(m1) + " $(" + str(v1) +")\r\n" + \
               "Greatest Decrease in Profits: " + str(m2) + " $(" + str(v2) +")\r\n"
    return myString
#________________________________________________________________________________________________________

#Read CSV file
path = "budget_data.csv"
df = pd.read_csv(path)

#Get total months
months = df["Date"].count()

#Get total of profit/losses over entire period
total_pl = df["Profit/Losses"].sum()

#Iterate over dataframe to find average change in profit/losses over entire period
li = [] # list to house each change in profit
avgSum = 0 # contains the sum total of changes in profits and losses
for i in range (0,months):
    if i > 0:
        val = df.iloc[i,1] - df.iloc[i-1,1] #solve for monthly change in profit and losses
        avgSum = avgSum + val #update running sum of changes in profits and losses
        li.append(val)#update list of changes in profits/losses

#Solve for average change in profit and losses over entire period
avgChange = avgSum / len(li)

#Max and min
aCopy = df.copy()
aCopy["Changes"] = [0] + li
myMax = aCopy.loc[aCopy["Changes"] == aCopy["Changes"].max(),["Date","Changes"]]
myMin = aCopy.loc[aCopy["Changes"] == aCopy["Changes"].min(),["Date","Changes"]]

#Build report string
report = BuildResults(months,total_pl,avgChange,myMax,myMin)

#Print Results
print(report)

#Export to text file
myFile = open("HW3_PyBankResults.txt","w+")
myFile.write(report)