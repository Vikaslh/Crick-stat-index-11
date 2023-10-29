import pandas as pd
import model

# importing dataset....
keeper_t20 = pd.read_csv('./datasets/wicketkeeper data t20i.csv')

# features considered.
features = ['Player Name', 'Catches', 'Stumpings', 'Maximum Dismissals']
# cleaning the data
keeper_t20 = keeper_t20.dropna(subset=features)
keeper_t20 = keeper_t20[features].copy()

features.remove('Player Name')

# scaling the data.
scaled = model.scale_data(keeper_t20, features)
# using kmeans to form clusters.
data = model.kmeansCluster(scaled[0], scaled[1])

# print(data['Cluster'].value_counts())

# spliting the dataframe into diffrent clusters.
# grp0 = data.loc[data['Cluster'] == 0]
# grp1 = data.loc[data['Cluster'] == 1]
# grp2 = data.loc[data['Cluster'] == 2]

# print(len(grp0), len(grp1), len(grp2))

# finding the best cluster
best_keeper = model.find_best_cluster(data, 2)
print(best_keeper)
