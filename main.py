from naive_bayes import *
from knn import *
from decision_tree import *
from kmeans import *
from random_forest import *
from support_vector_machines import *
from multi_layer_preceptron import *
from association_rules import *

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def make_plots():
    objects = ('Naive Bayes', '\nKNN-3', 'KNN-5', '\nKNN-11', 'Decision Tree', '\nKMeans', '\n\nRandom Forest', '\nSVM', 'MLP')
    # , '\nSVM', 'MLP'
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    y_pos = np.arange(len(objects))
    elapsed_times = []
    accs = []

    elapsed_time, acc_score, c_matrix = do_naive_bayes()
    elapsed_times.append(elapsed_time)
    accs.append(acc_score)
    elapsed_time, acc_score, c_matrix = do_knn(3)
    elapsed_times.append(elapsed_time)
    accs.append(acc_score)
    elapsed_time, acc_score, c_matrix = do_knn(5)
    elapsed_times.append(elapsed_time)
    accs.append(acc_score)
    elapsed_time, acc_score, c_matrix = do_knn(11)
    elapsed_times.append(elapsed_time)
    accs.append(acc_score)
    elapsed_time, acc_score, c_matrix = do_decision_tree()
    elapsed_times.append(elapsed_time)
    accs.append(acc_score)
    elapsed_time, acc_score, c_matrix = do_kmeans()
    elapsed_times.append(elapsed_time)
    accs.append(acc_score)
    elapsed_time, acc_score, c_matrix = do_random_forest()
    elapsed_times.append(elapsed_time)
    accs.append(acc_score)

    elapsed_time, acc_score, c_matrix = do_SVM()
    elapsed_times.append(elapsed_time)
    accs.append(acc_score)
    elapsed_time, acc_score, c_matrix = do_MLP()
    elapsed_times.append(elapsed_time)
    accs.append(acc_score)

    # count_frequency_columns()
    # count_min_max_mean_columns()
    print(accs)
    plt.bar(y_pos, elapsed_times, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Time')
    plt.title('Time')
    fig = plt.gcf()
    for index, value in enumerate(elapsed_times):
        plt.text(index - 0.2, elapsed_times[index], str("%.3f" % elapsed_times[index]))
    fig.savefig(f'time.png', dpi=100)
    plt.close(fig)
    plt.close()

    plt.bar(y_pos, accs, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Accuracy')
    plt.title('Accuracy')
    fig = plt.gcf()
    for index, value in enumerate(y):
        plt.text(index - 0.2, accs[index], str("%.3f" % accs[index]))
    fig.savefig(f'Accuracy.png', dpi=100)
    plt.close(fig)
    plt.close()


# do_association_rules()
make_plots()