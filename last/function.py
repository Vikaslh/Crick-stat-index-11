def find_best_cluster(data, k, value):
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
    dumy =  data.loc[data['Cluster'] == best]
    return( dumy[dumy['Team'] == value])

# def cluster_data(data, column_name ,value):
#     return( data[data[column_name] == value])

# column_name = 'Team'
# column_value = 'INDIA'
# batresult = find_best_cluster(scaled_data,3)
# batresult = cluster_data(batresult, column_name ,column_value)
