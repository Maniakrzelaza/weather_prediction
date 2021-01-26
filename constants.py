import time

Date = 0
Location = 1
MinTemp = 2
MaxTemp = 3
Rainfall = 4
Evaporation = 5
Sunshine = 6
WindGustDir = 7
WindGustSpeed = 8
WindDir9am = 9
WindDir3pm = 10
WindSpeed9am = 11
WindSpeed3pm = 12
Humidity9am = 13
Humidity3pm = 14
Pressure9am = 15
Pressure3pm = 16
Cloud9am = 17
Cloud3pm = 18
Temp9am = 19
Temp3pm = 20
RainToday = 21
RainTomorrow = 22

all_column_names = ['Date', 'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation',
                    'Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
                    'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am',
                    'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm', 'RainToday', 'RainTomorrow']

all_column_names_data_types = {'Date': 'object', 'Location': 'object', 'MinTemp': 'float64', 'MaxTemp': 'float64', 'Rainfall': 'object', 'Evaporation': 'object',
                    'Sunshine': 'object', 'WindGustDir': 'object', 'WindGustSpeed': 'float64', 'WindDir9am': 'object', 'WindDir3pm': 'object',
                    'WindSpeed9am': 'float64', 'WindSpeed3pm': 'float64', 'Humidity9am': 'float64', 'Humidity3pm': 'float64', 'Pressure9am': 'float64',
                    'Pressure3pm': 'float64', 'Cloud9am': 'object', 'Cloud3pm': 'object', 'Temp9am': 'float64', 'Temp3pm': 'float64', 'RainToday': 'object', 'RainTomorrow': 'object'}

string_columns = [Location, WindGustDir, WindDir9am, WindDir3pm, RainToday, RainTomorrow]
string_columns_names = ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow']

numeric_columns = [MinTemp, MaxTemp, WindGustSpeed, WindSpeed9am, WindSpeed3pm,
                   Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Temp9am, Temp3pm]
numeric_columns_names = ['MinTemp', 'MaxTemp', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm',
                         'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm']


all_column_names_for_associations = ['Location', 'MinTemp', 'MaxTemp',
                    'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
                    'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am',
                    'Pressure3pm', 'Temp9am', 'Temp3pm', 'RainToday', 'RainTomorrow']
