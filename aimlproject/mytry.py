import pandas as pd
from sklearn.neighbors import NearestNeighbors

#loading the data from the csv file
data = pd.read_csv('C:/Users/Admin/Desktop/CricketScorePredictor-master/data/odi.csv')

#filter data for england batsman with at least 400 runs and the least number of wickets
filtered_data = data[(data['bat_team'] == 'England') & (data['runs'] >= 400)]
england_batsmen_data = filtered_data[filtered_data['wickets'] == filtered_data['wickets'].min()][['batsman', 'runs', 'wickets']]

#convertiung categorical data
processed_data = pd.get_dummies(england_batsmen_data)

#using runs and wickets as features
X = processed_data[['runs', 'wickets']].values

#initialize the k-nearest neighbor model
knn = NearestNeighbors(n_neighbors=5)  #adjust the value of k as needed

#fit the model with the data
knn.fit(X)

#Ffinding 5 nearest neighbors for the case where runs are at least 400 and wickets are the least
required_runs = 400
required_wickets = england_batsmen_data['wickets'].min()
distances, indices = knn.kneighbors(X[(X[:, 0] >= required_runs) & (X[:, 1] == required_wickets)])

#printing the selected England batsmen with at least 400 runs and the least wickets
print("England Batsmen with at least 400 runs and the least wickets:")
for i in indices:
    print(england_batsmen_data.iloc[i])
