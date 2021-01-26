from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

from preprocess import *
from constants import *


def do_MLP():
    processed_data = get_processed_data()
    min_temp = map_to_numeric(get_column(processed_data, MinTemp))
    max_temp = map_to_numeric(get_column(processed_data, MaxTemp))
    wind_speed_9am = map_to_numeric(get_column(processed_data, WindSpeed9am))
    humidity_9am = map_to_numeric(get_column(processed_data, Humidity9am))
    humidity_3pm = map_to_numeric(get_column(processed_data, Humidity3pm))

    rain_tomorrow = get_column(processed_data, RainTomorrow)
    features = list(zip(min_temp, max_temp, wind_speed_9am, humidity_9am, humidity_3pm))
    features = [list(elem) for elem in features]

    model = MLPClassifier(activation='logistic', solver='adam', alpha=1e-2,
                    hidden_layer_sizes=(11, 5, 11), random_state=42, max_iter=1000)

    x_train, x_test, y_train, y_test = train_test_split(features, rain_tomorrow, test_size=0.33, random_state=42)

    start = time.time()
    model.fit(x_train, y_train)
    end = time.time()
    elapsed_time = end - start
    a = model.score(x_train, y_train)

    predicted = model.predict(x_test)
    print("Accuracy: ", metrics.accuracy_score(y_test, predicted))
    print(a)
    print("Multi-layer Perceptron")
    print("Confusion matrix: ", metrics.confusion_matrix(y_test, predicted))
    return elapsed_time, metrics.accuracy_score(y_test, predicted), metrics.confusion_matrix(y_test, predicted)
