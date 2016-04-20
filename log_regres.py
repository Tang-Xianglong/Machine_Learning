from numpy import *

def load_data_set():
    data_mat = []; label_mat = []
    fr = open('test_set.txt')
    for line in fr.readlines():
        line_array = line.strip().split()
        data_mat.append([1.0, float(line_array[0]), float(line_array[1])])
        label_mat.append(int(line_array[2]))
    return data_mat, label_mat

def sigmoid(inx):
    return 1.0/(1+exp(-inx))

def grad_ascent(data_mat_in, label_mat_in):
    data_mat = mat(data_mat_in)
    label_mat = mat(label_mat_in).transpose()
    m, n = shape(data_mat)
    alpha = 0.001
    max_cycles = 50
    weights = ones((n, 1))
    for k in range(max_cycles):
        h = sigmoid(data_mat * weights)
        error = (label_mat - h)
        weights = weights + alpha * data_mat.transpose() * error
    return weights

def stoc_grad_ascent0(data_mat, label_mat):
    from numpy import *
    m, n = shape(data_mat)
    alpha = 0.01
    weights = ones(n)
    for i in range(m):
        h = sigmoid(sum(data_mat[i])*weights)
        error = label_mat[i] - h
        weights = weights + alpha * error * data_mat[i]
    return weights

def stoc_grad_ascent1(data_mat, label_mat, num_iter = 150):
    m, n = shape(data_mat)
    weights = ones(n)
    for j in range(num_iter):   data_index = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.01
            rand_index = int(random.uniform(0, len(data_index)))
            h = sigmoid(sum(data_mat[rand_index] * weights))
            error = label_mat[rand_index] - h
            weights = weights + alpha * error * data_mat[rand_index]
            del(data_index[rand_index])
    return weights


def plot_best_fit(weights):
    import matplotlib.pyplot as plt
#    weights = wei.getA()
    data_mat, label_mat = load_data_set()
    data_array = array(data_mat)
    n = shape(data_array)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(label_mat[i]) == 1:
            xcord1.append(data_array[i, 1]); ycord1.append(data_array[i, 2])
        else:
            xcord2.append(data_array[i, 1]); ycord2.append(data_array[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s = 30, c = 'red', marker = 's')
    ax.scatter(xcord2, ycord2, s = 30, c = 'green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()

def classify_vector(inx, weights):
    prob = sigmoid(sum(inx * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0

def colic_test():
    fr_train = open('horse_colic_training.txt')
    fr_test = open('horse_colic_test.txt')
    training_set = []; training_labels = []
    for line in fr_train.readlines():
        curr_line = line.strip().split('\t')
        line_array = []
    for i in range(21):
        line_array.append(float(curr_line[i]))
    training_set.append(line_array)
    training_labels.append(float(curr_line[21]))
    training_weights =