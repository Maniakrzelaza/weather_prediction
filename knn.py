from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from preprocess import *
from constants import *


def do_knn(n_number):
    processed_data = get_processed_data()
    min_temp = get_column(processed_data, MinTemp)
    max_temp = get_column(processed_data, MaxTemp)
    wind_speed_9am = get_column(processed_data, WindSpeed9am)
    humidity_9am = get_column(processed_data, Humidity9am)
    humidity_3pm = get_column(processed_data, Humidity3pm)

    rain_tomorrow = get_column(processed_data, RainTomorrow)
    features = list(zip(min_temp, max_temp, wind_speed_9am, humidity_9am, humidity_3pm))
    features = [list(elem) for elem in features]
    x_train, x_test, y_train, y_test = train_test_split(features, rain_tomorrow, test_size=0.33, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=n_number, metric='euclidean')
    start = time.time()
    knn.fit(x_train, y_train)
    end = time.time()
    elapsed_time = end - start
    y_pred = knn.predict(x_test)
    print(f'KNN {n_number}')
    print("Confusion matrix: ", confusion_matrix(y_test, y_pred))
    print("Accuracy: ", accuracy_score(y_test, y_pred))
    return elapsed_time, accuracy_score(y_test, y_pred), confusion_matrix(y_test, y_pred)