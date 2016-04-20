def load_data_set(file_name):
    data_mat = []; label_mat = []
    fr = open(file_name)
    for line in fr.readlines():
        line_arry = line.strip().split()
        data_mat.append([float(line_arry[0]), float(line_arry[1])])
        label_mat.append(float(line_arry[2]))
    return data_mat, label_mat

def select_J_rand(i, m):
    j = i
    while (j == i):
        j = int(random.unform(0, m))
    return j

def clip_alpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj