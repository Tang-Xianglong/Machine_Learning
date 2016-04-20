from numpy import *

def load_simple_data():
    data_mat = matrix([[1.0, 2.1],
                       [2.0, 1.1],
                       [1.3, 1.0],
                       [1.0, 1.0],
                       [2.0, 1.0]])
    label_mat = [1.0, 1.0, -1.0, -1.0, 1.0]
    return data_mat, label_mat

def stump_classify(data_mat, charac_id, thresh_value, thresh_modle):
    ret_array = ones((shape(data_mat)[0], 1))
    if thresh_modle == 'lt':
        ret_array[data_mat[:, charac_id] <= thresh_value] = -1.0
    else:
        ret_array[data_mat[:, charac_id] > thresh_value] = -1.0
    return ret_array

def build_stump(data_arr, class_labels, sample_weights):
    data_mat = mat(data_arr); label_mat = mat(class_labels).T
    m, n = shape(data_mat); min_error = inf; best_strump = {}
    best_predict_labels = mat(zeros((m, 1)))
    num_step = 10.0;
    for i in range(n):
        min_value = data_mat[:, i].min(); max_value = data_mat[:, i].max()
        step_size = (max_value - min_value)/num_step
        for j in range(-1, int(num_step)+1):
            thresh_value = min_value + j * step_size
            for k in ['lt', 'gt']:
                pridect_labels = stump_classify(data_mat, i, thresh_value, k)
                error_labels = mat(ones((m, 1)))
                error_labels[pridect_labels == label_mat] = 0
                weight_error = sample_weights.T * error_labels
                print 'feature %d, thresh_value %f, model %s, the weighted error is %f' % \
                    (i, thresh_value, k, weight_error)
                if weight_error < min_error:
                    min_error = weight_error
                    best_predict_labels = pridect_labels.copy()
                    best_strump['feature'] = i
                    best_strump['thresh_value'] = thresh_value
                    best_strump['model'] = k
    return best_strump, min_error, best_predict_labels

def adaboost_train(data_arr, class_labels, num_iteration):
    weak_classify_array = []
    m =

