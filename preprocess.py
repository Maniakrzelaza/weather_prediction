import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

from constants import *


def filter_nas(array, *columns):
    result = array
    for column in range(len(columns)):
        result = list(filter(lambda x: x[columns[column]] != 'NONE', result))
    return result


def get_column(array, column):
    result = []
    for i in range(len(array)):
        result.append(array[i][column])
    return result


def get_original_data():
    original_data_set = pd.read_csv('weatherAUS.csv', sep=',')
    processed_data = original_data_set.to_numpy()
    return processed_data


def get_debug_data():
    original_data_set = pd.read_csv('debug.csv', sep=',')
    processed_data = original_data_set.to_numpy()
    return processed_data


def get_processed_data():
    processed_data = get_original_data()
    processed_data = filter_nas(
        processed_data,
        RainToday,
        WindDir9am,
        WindDir3pm,
        MinTemp,
        MaxTemp,
        RainTomorrow,
        WindSpeed9am,
        Humidity9am,
        Humidity3pm,
        WindGustSpeed,
        WindSpeed3pm,
        Pressure9am,
        Pressure3pm,
        Temp9am,
        Temp3pm
    )
    return processed_data


def get_categorized_processed_data():
    data = get_processed_data()
    df = DataFrame(data, columns=all_column_names)
    new_df = df.astype(all_column_names_data_types)
    for column_name in numeric_columns_names:
        cut_labels_3 = [f'{column_name}-Low', f'{column_name}-Medium', f'{column_name}-High']
        new_df[column_name] = pd.qcut(new_df[column_name], q=3, labels=cut_labels_3)
    # new_df.at['RainTomorrow', 'Yes'] = 'asa'
    print('KKKKK')
    updated_target_column = [];
    for val in new_df['RainTomorrow']:
        if val == 'Yes':
            updated_target_column.append('RainTomorrowYes')
        else:
            updated_target_column.append('RainTomorrowNo')
    updated_target_column_series = Series(updated_target_column)
    new_df['RainTomorrow'] = updated_target_column_series
    return new_df


def map_to_numeric(column):
    result = []
    for i in range(len(column)):
        result.append(float(column[i]))

    return result


def count_mean_max_min(column_name, column_number):
    data = get_processed_data()
    column = map_to_numeric(get_column(data, column_number))
    mean = 0
    min_value = 99999999
    max_value = -9999999
    for i in range(len(column)):
        mean += column[i]
        if column[i] < min_value:
            min_value = column[i]
        if column[i] > max_value:
            max_value = column[i]
    mean /= len(column)
    return mean, max_value, min_value, column_name


def count_frequency(column_name, column_number):
    data = get_processed_data()
    column = get_column(data, column_number)
    frequency_map = {}
    for i in range(len(column)):
        frequency_map[column[i]] = frequency_map.get(column[i], 0) + 1
    labels = []
    sizes = []
    for key, val in frequency_map.items():
        labels.append(key)
        sizes.append(val)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    fig = plt.gcf()
    plt.title(column_name)
    fig.savefig(f'{column_name}.png', dpi=100)
    plt.close(fig)
    plt.close()


def count_frequency_columns():
    columns_names = string_columns_names
    columns = string_columns
    for i in range(len(columns)):
        count_frequency(columns_names[i], columns[i])


def count_min_max_mean_columns():
    columns_names = numeric_columns_names
    columns = numeric_columns
    for i in range(len(columns)):
        print(count_mean_max_min(columns_names[i], columns[i]))

