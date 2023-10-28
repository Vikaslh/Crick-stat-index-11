import pandas as pd
from sklearn.ensemble import RandomForestRegressor

'''
all = int(input(" enter the number of all rounder to display:"))
bat = int(input(" enter the number of all rounder to display:"))
ball = int(input(" enter the number of all rounder to display:"))
'''
#loading the data
batting_data = pd.read_csv('ODIBatting.csv')
bowling_data = pd.read_csv('ODIBowling.csv')

#dropping duplicates from batting data
batting_data.drop_duplicates(subset ="Player", keep = 'first', inplace = True)

#dropping duplicates from bowling data
bowling_data.drop_duplicates(subset ="Player", keep = 'first', inplace = True)








#function to remove NA values and convert '-' to 0
def preprocess_value(value):
    if value == 'NA' or value == '-':
        return 0
    else:
        return float(value)


#apply the preprocess value function to the specific columns
batting_data["Runs Scored"] = batting_data["Runs Scored"].apply(preprocess_value)
batting_data["Highest Innings Score Num"] = batting_data["Highest Innings Score Num"].apply(preprocess_value)
batting_data["Batting Avg"] = batting_data["Batting Avg"].apply(preprocess_value)

bowling_data["Innings Bowled In"] = bowling_data["Innings Bowled In"].apply(preprocess_value)
bowling_data["Bowling Strike Rate"] = bowling_data["Bowling Strike Rate"].apply(preprocess_value)
bowling_data["Four Wickets In An Innings"] = bowling_data["Four Wickets In An Innings"].apply(preprocess_value)
bowling_data["200+ Wickets Taken"] = bowling_data["200+ Wickets Taken"].apply(preprocess_value)


#generate score for each batsmen
batting_data['batsman_Score'] = (batting_data["Runs Scored"] * 0.4) + (batting_data["Highest Innings Score Num"] * 0.3) + (batting_data["Batting Avg"] * 0.3)
#generate score for each bowler
bowling_data['bowler_Score'] = (bowling_data["Innings Bowled In"] * 0.3) + (bowling_data["Bowling Strike Rate"] * 0.2) + (bowling_data["Four Wickets In An Innings"] * 0.3)+(bowling_data["200+ Wickets Taken"] * 0.2)


#merging the two dataframes(batsman and bowler) based on player column
allRounder_data=pd.merge(batting_data , bowling_data ,on ="Player")

#generate a score for all rounders
allRounder_data['allRounder_Score'] = (allRounder_data['batsman_Score']*0.5) + (allRounder_data['bowler_Score']*0.5)




#selecting the features for the model
selectedBatsman_features = ["Runs Scored", "Highest Innings Score Num", "Batting Avg", "batsman_Score"]
selected_bowling_features =["Innings Bowled In","Bowling Strike Rate","Four Wickets In An Innings","200+ Wickets Taken"]
#selected_allRounder_features = ["Runs Scored", "Highest Innings Score Num", "Batting Avg", "batsman_Score","Innings Bowled In","Bowling Strike Rate","Four Wickets In An Innings","200+ Wickets Taken"]
#prepare the data for the Random Forest model
X = batting_data[selectedBatsman_features]
y = batting_data['batsman_Score']
a = bowling_data[selected_bowling_features]
b = bowling_data['bowler_Score']

#p =allRounder_data['selected_allRounder_features']
#q = allRounder_data['allRounder_Score']

#building the Random Forest model
model = RandomForestRegressor()
model.fit(X, y)
model.fit(a,b)
#model.fit(p,q)















#save the top  allrounders on the rf model predictions to the below variable
top_allRounder = allRounder_data.sort_values('allRounder_Score',ascending=False).head(7)

    
    

#save the top batsmen based on the model predictions to this variable
top_batsmen = batting_data.sort_values('batsman_Score', ascending=False).head(4)
    

#save the top bowlers based on the model predictions to this variable
top_bowler = bowling_data.sort_values('bowler_Score', ascending=False).head(4)
    
#display the top n allrounders
print("the top allRounders based rf model:")
print(top_allRounder[['Player','allRounder_Score']])
    
#display the top n batsman
print("Top 3 batsman based on the Random Forest model:")
print(top_batsmen[['Player', 'batsman_Score']])

    
#display the top n bowlers
print("the top  bowlers based rf model:")
print(top_bowler[['Player','bowler_Score']])
    


 
    


    
    