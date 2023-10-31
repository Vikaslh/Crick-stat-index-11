# importing necessary libraries.
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot  as plt
import numpy as np
import glob
import function
import p

allrounder_t20 = pd.read_csv("final.csv")
#allrounder_t20.head(20)

features = ['Player','Team','Ave','SR', 'Wkts','Econ','Bowl_Ave','Bowl_SSR'] # features considered.
allrounder_t20 = allrounder_t20.dropna(subset=features) # remove rows not dont have numerical value from the features.
allrounder_t20 = allrounder_t20[features].copy()
#allrounder_t20

# removing incorrect data
allrounder_t20 = allrounder_t20.dropna()
#allrounder_t20

# scaling the data.
scaler = StandardScaler()
features = ['Ave','SR', 'Wkts','Econ','Bowl_Ave','Bowl_SSR']
scaled_data = pd.DataFrame( scaler.fit_transform(allrounder_t20[features]) , columns = features )
df = PCA(2).fit_transform(scaled_data)
#scaled_data

''' To find how many clusers are to be formed '''
def elbow_plot( min_k, max_k, k_max_iter):
    sum_squared_distances = []
    k_range = range(min_k,max_k+1)
    for k in k_range:
        km = KMeans(n_clusters=k, max_iter=k_max_iter, n_init=50)
        km.fit(df)
        sum_squared_distances.append(km.inertia_)
        
    # Plot the score for each value of k
    plt.plot(k_range, sum_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum of squared distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()

#elbow_plot(2,5,50)

# Clustering the players using k-means algorithm
km = KMeans(n_clusters=5,n_init=50)
label = km.fit_predict(df)
scaled_data['Cluster'] = km.labels_ # assigning the cluster number for each datapoint in the dataframe.
scaled_data['Cluster'].value_counts()
#label

'''centroids = km.cluster_centers_
u_labels = np.unique(label)
for i in u_labels:
    plt.scatter(df[label==i,0],df[label==i,1], label=i)
plt.scatter(centroids[:,0], centroids[:,1], s=80, color = 'k')
plt.legend()
plt.show()'''

scaled_data.insert(0,'Player',allrounder_t20['Player']) # adding player name to the cluster...
scaled_data.insert(1,'Team',allrounder_t20['Team'])

# scaled_data
# spliting the dataframe into diffrent clusters.
# b0 = scaled_data.loc[scaled_data['Cluster']==0]
# b1 = scaled_data.loc[scaled_data['Cluster']==1]
# b2 = scaled_data.loc[scaled_data['Cluster']==2]
# b3 = scaled_data.loc[scaled_data['Cluster']==3]
# b4 = scaled_data.loc[scaled_data['Cluster']==4]

#len(b0),len(b1),len(b2),len(b3),len(b4)
# def find_best_cluster(data, k):
#     # TODO Update this method functionality.
#     cluster_avg = {}
#     for i in range(0, k):
#         avg = 0.0
#         temp = data.loc[data['Cluster'] == i]  # extract each cluster.
#         # print(temp)
#         cluster_mean = list(
#             temp.mean(
#                 axis=0,
#                 skipna=True,
#                 numeric_only=True)
#         )
#         # remove cluster no.
#         cluster_mean.pop()
#         # calculating overall average of the cluster.
#         for j in cluster_mean:
#             avg += j
#         # assign each cluster average with cluster number.
#         cluster_avg[i] = avg
#     # print(cluster_avg)
#     best = max(zip(cluster_avg.values(), cluster_avg.keys()))[1]
#     return data.loc[data['Cluster'] == best]

# print(scaled_data['Cluster'].value_counts())
# def cluster_data(data, column_name ,value):
#     return( data[data[column_name] == value])


# column_value = 'INDIA'
# allresult = find_best_cluster(scaled_data,3)
# allresult = cluster_data(allresult, column_name ,column_value)
# all={}
# print(allresult)

best_allrounder = function.find_best_cluster(scaled_data,'Team',p.team_name)
print(best_allrounder)