import pandas as pd
import model

# importing dataset....
bowler_t20 = pd.read_csv('./datasets/bowler data t20i.csv')

# features considered.
features = ['Player Name', 'Wickets', 'Bowling Average', 'Economy Rate']
# cleaning the data
bowler_t20 = bowler_t20.dropna(subset=features)
bowler_t20 = bowler_t20[features].copy()

features.remove('Player Name')

# scaling the data.
scaled = model.scale_data(bowler_t20, features)
# using kmeans to form clusters.
data = model.kmeansCluster(scaled[0], scaled[1])

# print(data['Cluster'].value_counts())

# spliting the dataframe into diffrent clusters.
# grp0 = data.loc[data['Cluster'] == 0]
# grp1 = data.loc[data['Cluster'] == 1]
# grp2 = data.loc[data['Cluster'] == 2]

# print(len(grp0), len(grp1), len(grp2))

# finding the best cluster
best_bowler = model.find_best_cluster(data, 3)
print(best_bowler)
