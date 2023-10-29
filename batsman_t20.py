# importing necessary libraries.
import pandas as pd
import model

# importing dataset....
batsman_t20 = pd.read_csv('./datasets/batsman data t20i.csv')
batsman_t20 = batsman_t20.drop(38)  # removing incorrect data
batsman_t20 = batsman_t20.reset_index()

# features considered.
features = ['Player Name', 'Batting Average',
            'Strike Rate', 'Runs', 'Not Outs']
# cleaning the data
batsman_t20 = batsman_t20.dropna(subset=features)
batsman_t20 = batsman_t20[features].copy()

features.remove('Player Name')

# scaling the data.
scaled = model.scale_data(batsman_t20, features)
# using kmeans to form clusters.
data = model.kmeansCluster(scaled[0], scaled[1])

# print(data['Cluster'].value_counts())

# spliting the dataframe into diffrent clusters.
# grp0 = data.loc[data['Cluster'] == 0]
# grp1 = data.loc[scaled_data['Cluster'] == 1]
# grp2 = data.loc[scaled_data['Cluster'] == 2]

# print(len(grp0), len(grp1), len(grp2))

# finding the best cluster

best_batsmen = model.find_best_cluster(data, 3)
print(best_batsmen)
