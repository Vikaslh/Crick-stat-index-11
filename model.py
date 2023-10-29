from matplotlib import pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def scale_data(data, features):
    scaler = StandardScaler()
    s = scaler.fit_transform(data[features])
    data.loc[:, features] = s
    # converting all features into 2D
    features = PCA(2).fit_transform(data[features])
    # for i in range(0, len(data)):
    #     print(s[i])
    #     print(data.loc[i, :])
    #     print()
    return [data, features]


def kmeansCluster(data, features):
    # intialzing kmeans.
    km = KMeans(
        n_clusters=3,
        n_init=50,
        # init='k-means++',
        # random_state=0
    )
    # TODO: Find why same cluster number is assigned ...
    label = km.fit_predict(features)
    data['Cluster'] = km.labels_  # assigning cluster numbers the dataframe.

    def plot_cluster():
        # finding centroids...
        centroids = km.cluster_centers_
        u_labels = np.unique(label)
        # iterating over each cluster
        for i in u_labels:
            # ploting all datapoints in a cluster
            plt.scatter(
                features[label == i, 0],
                features[label == i, 1],
                label=i
            )
        # ploting centroids
        plt.scatter(centroids[:, 0], centroids[:, 1], s=80, color='k')
        plt.legend()
        plt.title('Clusters')
        plt.show()

    def elbow_plot(min_k, max_k, k_max_iter):
        sum_squared_distances = []
        k_range = range(min_k, max_k+1)
        for k in k_range:
            km = KMeans(
                n_clusters=k,
                max_iter=k_max_iter,
                init='k-means++',
                n_init=50,
                random_state=0
            )
            km.fit(features)
            sum_squared_distances.append(km.inertia_)

        # Plot the score for each value of k
        plt.plot(k_range, sum_squared_distances, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Sum of squared distances')
        plt.title('Elbow Method For Optimal k')
        plt.show()

    # elbow_plot(1, 10, 20)
    # plot_cluster()
    return data


def find_best_cluster(data, k):
    # TODO Update this method functionality.
    cluster_avg = {}
    for i in range(0, k):
        avg = 0.0
        temp = data.loc[data['Cluster'] == i]  # extract each cluster.
        # print(temp)
        cluster_mean = list(
            temp.mean(
                axis=0,
                skipna=True,
                numeric_only=True)
        )
        # remove cluster no.
        cluster_mean.pop()
        # calculating overall average of the cluster.
        for j in cluster_mean:
            avg += j
        # assign each cluster average with cluster number.
        cluster_avg[i] = avg
    # print(cluster_avg)
    best = max(zip(cluster_avg.values(), cluster_avg.keys()))[1]
    return data.loc[data['Cluster'] == best]
