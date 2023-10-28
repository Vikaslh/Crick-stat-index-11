# importing necessary libraries.
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# importing dataset....
bowler_t20 = pd.read_csv('./datasets/bowler data t20i.csv')

# features considered.
features = ['Player Name', 'Wickets', 'Bowling Average', 'Economy Rate']
# cleaning the data
bowler_t20 = bowler_t20.dropna(subset=features)
bowler_t20 = bowler_t20[features].copy()

# scaling the data.
scaler = StandardScaler()
features.remove('Player Name')
scaled_data = pd.DataFrame(
    scaler.fit_transform(bowler_t20[features]),
    columns=features)
pca = PCA(2)
reduced_data = pca.fit_transform(scaled_data)

''' To find how many clusers are to be formed '''


def elbow_plot(min_k, max_k, k_max_iter):
    sum_squared_distances = []
    k_range = range(min_k, max_k+1)
    for k in k_range:
        km = KMeans(n_clusters=k,
                    max_iter=k_max_iter,
                    init='k-means++',
                    n_init=50,
                    random_state=0)
        km.fit(reduced_data)
        sum_squared_distances.append(km.inertia_)

    # Plot the score for each value of k
    plt.plot(k_range, sum_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum of squared distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()


# elbow_plot(2, 5, 50)

# Clustering the players using k-means algorithm.
km = KMeans(n_clusters=3,
            n_init=50,
            init='k-means++',
            random_state=0)
label = km.fit_predict(reduced_data)
scaled_data['Cluster'] = km.labels_

''' Plot cluster on graph '''


def plot_clusters():
    centroids = km.cluster_centers_
    u_labels = np.unique(label)
    for i in u_labels:
        plt.scatter(reduced_data[label == i, 0],
                    reduced_data[label == i, 1], label=i)
    plt.scatter(centroids[:, 0], centroids[:, 1], s=80, color='k')
    plt.legend()
    plt.show()


# plot_clusters()


scaled_data.insert(0, 'Player Name', bowler_t20['Player Name'])

# print(scaled_data['Cluster'].value_counts())

# spliting the dataframe into diffrent clusters.
# grp0 = scaled_data.loc[scaled_data['Cluster'] == 0]
# grp1 = scaled_data.loc[scaled_data['Cluster'] == 1]
# grp2 = scaled_data.loc[scaled_data['Cluster'] == 2]

# print(len(grp0), len(grp1), len(grp2))


def find_best_cluster():
    idx = -1
    for i in range(0, 3):
        min_len = 9999999
        temp = scaled_data.loc[scaled_data['Cluster'] == i]
        length = len(temp)
        if length <= min_len:
            min_len = length
            idx = i
    return scaled_data.loc[scaled_data['Cluster'] == idx]


best_bowler = find_best_cluster()
