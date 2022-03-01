import math

def mean(labels):
    return sum(labels)/len(labels)

def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)

def KMeans(datapoints,centroids):
  centroids = centroids
  for iteration in range(0,5):
    cluster_map = {}

    for point in datapoints:
      min_distance = 100000
      assigned_centroid_index=0
      # assign nearest distance cluster to point
      for centroid_index in range(0,len(centroids)):
        distance = euclidean_distance(point,centroids[centroid_index])
        if(distance < min_distance):
          min_distance = distance
          assigned_centroid_index = centroid_index
      """
      cluster_map[certain index of cluster] = [
        [list of x coordinates of points assigned to that cluster]
        [list of y coordinates of points assigned to that cluster]
      ]
      """
      if assigned_centroid_index in cluster_map:
        cluster_map[assigned_centroid_index][0].append(point[0])
        cluster_map[assigned_centroid_index][1].append(point[1])
      else :
        cluster_map[assigned_centroid_index] = [[point[0]],[point[1]]]

    centroids = []
    # update centroids by taking mean of x_coordinate and y_coordinate arrays
    for key in list(cluster_map.keys()):
      centroids.append((mean(cluster_map[key][0]),mean(cluster_map[key][1])))
    print(iteration)

  return centroids

dataset = [
  (0.1,0.6),
  (0.15,0.71),
  (0.08,0.9),
  (0.16, 0.85),
  (0.2,0.3),
  (0.25,0.5),
  (0.24,0.1),
  (0.3,0.2)
]
centers = [
  (0.1,0.6),
  (0.3,0.2)
]
kmeans = KMeans(dataset, centers)
print(kmeans)

