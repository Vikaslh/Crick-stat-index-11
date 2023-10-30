import pandas as pd
from sklearn.neighbors import NearestNeighbors
data = pd.read_csv('C:/Users/Admin/Desktop/CricketScorePredictor-master/data/odi.csv')
filtered_data = data[(data['bat_team'] == 'England') & (data['runs'] >= 400)]
england_batsmen_data = filtered_data[filtered_data['wickets'] == filtered_data['wickets'].min()][['batsman', 'runs', 'wickets']]
processed_data = pd.get_dummies(england_batsmen_data)
X = processed_data[['runs', 'wickets']].values
knn = NearestNeighbors(n_neighbors=5)  #adjust the value of k as needed
knn.fit(X)
required_runs = 400
required_wickets = england_batsmen_data['wickets'].min()
distances, indices = knn.kneighbors(X[(X[:, 0] >= required_runs) & (X[:, 1] == required_wickets)])
print("England Batsmen with at least 400 runs and the least wickets:")
for i in indices:
    print(england_batsmen_data.iloc[i])
