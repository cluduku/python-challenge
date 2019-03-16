#___________________________________MODULES______________________________________________________________
import pandas as pd
#________________________________________________________________________________________________________

#___________________________________FUNCTIONS____________________________________________________________
def BuildResult(voteTotal,aDataFrame):
    myString = myString = "Election Results\r\n-----------------\r\n" + \
               "Total Votes: " + str(voteTotal) + "\r\n-----------------\r\n" + \
               aDataFrame.to_string() + "\r\n-----------------\r\n" + \
               "Winner: " + aDataFrame.index[0]
    return myString
#________________________________________________________________________________________________________

path = 'election_data.csv' #specify file path
df = pd.read_csv(path) #read csv file into a data frame
numVotes = df["Voter ID"].count() #get total number of votes
p = df["Candidate"].value_counts()#get a series that totals vote for each candidate in descending order
g = p[:] /numVotes * 100 #get a series that reflects percentage value of votes obtained by each candidate
f = pd.concat([p,g], axis = 1) #create a dataframe that concisely shows candidates, votes & precent
f.columns = ["Total Votes","Percent (%)"] #rename columns for new data frame
summary = BuildResult(numVotes,f) #Build a string detailing results
print(summary) #print results to terminal

#Export to text file
myFile = open("HW3_PyPollResults.txt","w+")
myFile.write(summary)

