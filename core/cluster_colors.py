# from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
from numpy import array


def transform_image(img, n_colors, random_state):
    # clusterer = KMeans(n_clusters=n_colors, random_state=random_state)
    clusterer = MeanShift()
    data = array(img).reshape((img.size[0] * img.size[1], 3))
    clustered_data = clusterer.fit_predict(data)
    labels = clusterer.cluster_centers_
    colored_data = array([labels[p] for p in clustered_data])
    colored_data = colored_data.astype('uint8')
    return colored_data.reshape(img.size[1], img.size[0], 3)
