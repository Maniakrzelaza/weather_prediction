import pandas as pd
import numpy as np
from apyori import apriori

from preprocess import *
from constants import *


def filter_results(row):
    return ('RainTomorrowYes' in row[0]) or ('RainTomorrowNo' in row[0])


def sort_results(row):
    return row[1]


def do_association_rules():
    data = get_categorized_processed_data()
    data = data.loc[:, all_column_names_for_associations]
    print("START")
    final_rule = apriori(data.to_numpy(), min_support=0.1, min_confidence=0.9 )
    result = filter(filter_results, final_rule)
    result = list(result)
    result.sort(reverse=True, key=sort_results)
    for i in result:
        if 'RainTomorrowNo' in i[0]:
            print(str(list(filter(lambda x: x != 'RainTomorrowNo',i[0]))) + " -> RainTomorrowNo")
        else:
            print(str(list(filter(lambda x: x != 'RainTomorrowYes', i[0]))) + " -> RainTomorrowYes")

    print("End")