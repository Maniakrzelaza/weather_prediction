from sklearn import preprocessing
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

from preprocess import *
from constants import *


def do_SVM():
    processed_data = get_processed_data()

    rain_today = get_column(processed_data, RainToday)
    wind_dir_9am = get_column(processed_data, WindDir9am)
    wind_dir_3pm = get_column(processed_data, WindDir3pm)
    rain_tomorrow = get_column(processed_data, RainTomorrow)

    le = preprocessing.LabelEncoder()
    rain_today = le.fit_transform(rain_today)
    wind_dir_9am = le.fit_transform(wind_dir_9am)
    wind_dir_3pm = le.fit_transform(wind_dir_3pm)
    rain_tomorrow = le.fit_transform(rain_tomorrow)

    features = list(zip(wind_dir_9am, wind_dir_3pm, rain_today))

    model = svm.SVC()

    x_train, x_test, y_train, y_test = train_test_split(features, rain_tomorrow, test_size=0.33, random_state=42)


    start = time.time()
    model.fit(x_train, y_train)
    end = time.time()
    elapsed_time = end - start

    predicted = model.predict(x_test)
    print("Accuracy: ", metrics.accuracy_score(y_test, predicted))
    print("Support Vector Machines")
    print("Confusion matrix: ", metrics.confusion_matrix(y_test, predicted))
    return elapsed_time, metrics.accuracy_score(y_test, predicted), metrics.confusion_matrix(y_test, predicted)
