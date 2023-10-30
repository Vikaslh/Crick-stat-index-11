import pandas as pd
from sklearn.ensemble import RandomForestRegressor

'''
all = int(input(" enter the number of all rounder to display:"))
bat = int(input(" enter the number of all rounder to display:"))
ball = int(input(" enter the number of all rounder to display:"))
'''
batting_data = pd.read_csv('ODIBatting.csv')
bowling_data = pd.read_csv('ODIBowling.csv')
batting_data.drop_duplicates(subset ="Player", keep = 'first', inplace = True)
bowling_data.drop_duplicates(subset ="Player", keep = 'first', inplace = True)

def preprocess_value(value):
    if value == 'NA' or value == '-':
        return 0
    else:
        return float(value)

batting_data["Runs Scored"] = batting_data["Runs Scored"].apply(preprocess_value)
batting_data["Highest Innings Score Num"] = batting_data["Highest Innings Score Num"].apply(preprocess_value)
batting_data["Batting Avg"] = batting_data["Batting Avg"].apply(preprocess_value)

bowling_data["Innings Bowled In"] = bowling_data["Innings Bowled In"].apply(preprocess_value)
bowling_data["Bowling Strike Rate"] = bowling_data["Bowling Strike Rate"].apply(preprocess_value)
bowling_data["Four Wickets In An Innings"] = bowling_data["Four Wickets In An Innings"].apply(preprocess_value)
bowling_data["200+ Wickets Taken"] = bowling_data["200+ Wickets Taken"].apply(preprocess_value)

batting_data['batsman_Score'] = (batting_data["Runs Scored"] * 0.4) + (batting_data["Highest Innings Score Num"] * 0.3) + (batting_data["Batting Avg"] * 0.3)
bowling_data['bowler_Score'] = (bowling_data["Innings Bowled In"] * 0.3) + (bowling_data["Bowling Strike Rate"] * 0.2) + (bowling_data["Four Wickets In An Innings"] * 0.3)+(bowling_data["200+ Wickets Taken"] * 0.2)
allRounder_data=pd.merge(batting_data , bowling_data ,on ="Player")
allRounder_data['allRounder_Score'] = (allRounder_data['batsman_Score']*0.5) + (allRounder_data['bowler_Score']*0.5)
selectedBatsman_features = ["Runs Scored", "Highest Innings Score Num", "Batting Avg", "batsman_Score"]
selected_bowling_features =["Innings Bowled In","Bowling Strike Rate","Four Wickets In An Innings","200+ Wickets Taken"]
#selected_allRounder_features = ["Runs Scored", "Highest Innings Score Num", "Batting Avg", "batsman_Score","Innings Bowled In","Bowling Strike Rate","Four Wickets In An Innings","200+ Wickets Taken"]
X = batting_data[selectedBatsman_features]
y = batting_data['batsman_Score']
a = bowling_data[selected_bowling_features]
b = bowling_data['bowler_Score']
model = RandomForestRegressor()
model.fit(X, y)
model.fit(a,b)
#model.fit(p,q)
top_allRounder = allRounder_data.sort_values('allRounder_Score',ascending=False).head(7)
top_batsmen = batting_data.sort_values('batsman_Score', ascending=False).head(4)
top_bowler = bowling_data.sort_values('bowler_Score', ascending=False).head(4)
print("the top allRounders based rf model:")
print(top_allRounder[['Player','allRounder_Score']])
print("Top 3 batsman based on the Random Forest model:")
print(top_batsmen[['Player', 'batsman_Score']])
print("the top  bowlers based rf model:")
print(top_bowler[['Player','bowler_Score']])
    


 
    


    
    
