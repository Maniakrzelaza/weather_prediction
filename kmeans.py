from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, accuracy_score

from preprocess import *
from constants import *


def do_kmeans():
    processed_data = get_processed_data()
    min_temp = map_to_numeric(get_column(processed_data, MinTemp))
    max_temp = map_to_numeric(get_column(processed_data, MaxTemp))
    wind_speed_9am = map_to_numeric(get_column(processed_data, WindSpeed9am))
    humidity_9am = map_to_numeric(get_column(processed_data, Humidity9am))
    humidity_3pm = map_to_numeric(get_column(processed_data, Humidity3pm))
    rain_tomorrow = get_column(processed_data, RainTomorrow)
    rain_tomorrow_processed = []
    for elem in rain_tomorrow:
        if elem == 'Yes':
            rain_tomorrow_processed.append(1)
        else:
            rain_tomorrow_processed.append(0)
    features = list(zip(min_temp, max_temp, wind_speed_9am, humidity_9am, humidity_3pm))

    features = [list(elem) for elem in features]
    x_train, x_test, y_train, y_test = train_test_split(features, rain_tomorrow_processed, test_size=0.33, random_state=42)
    kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=200)
    start = time.time()
    kmeans.fit(x_train, y_train)
    end = time.time()
    elapsed_time = end - start
    y_pred = kmeans.predict(x_test)

    print("Kmeans:")
    print("Confusion matrix: ", confusion_matrix(y_test, y_pred))
    print("Accuracy: ", accuracy_score(y_test, y_pred))
    return elapsed_time, accuracy_score(y_test, y_pred), confusion_matrix(y_test, y_pred)