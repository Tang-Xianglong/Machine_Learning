
from numpy import *

def loadDataSet():
#    postingList = [['my', 'dog', 'has', 'flea', \
#                    'problems', 'help', 'please'],
#                   ['maybe', 'not', 'take', 'him', \
#                    'to', 'dog', 'park', 'stupid'],
#                   ['my', 'dalmation', 'is', 'so', 'cute', \
#                    'I', 'love', 'him'],
#                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
#                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', \
#                    'to', 'stop', 'him'],
#                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
#    classVec = [0,1,0,1,0,1]
    word_list = [['c','e'],['b','c','d'],['a','b','e'],['b','c','e'],['a','c','e']]
    class_list = [0,1,0,1,0]
    return word_list, class_list

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print "the word: %s is not in my Vocabulary!" % word
    return returnVec

def bagOfWords2VecMN(unique_word_list, word_in_doc):
    return_vec = [0]*len(unique_word_list)
    for word in word_in_doc:
        if word in unique_word_list:
            return_vec[unique_word_list.index(word)] += 1
    return return_vec

def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    print "numTrainDocs = %d" % numTrainDocs
    num_words = len(trainMatrix[0])
    print "num_words = %d" % num_words
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0_num = ones(num_words); p1_num = ones(num_words)
    p0_denom = 2.0; p1_denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1_num += trainMatrix[i]
            p1_denom += sum(trainMatrix[i])
        else:
            p0_num += trainMatrix[i]
            p0_denom += sum(trainMatrix[i])
    p1_vect = p1_num/p1_denom
    p0_vect = p0_num/p0_denom
#    p1_vect = p1_num/float(sum(trainCategory)+2)
#    p0_vect = p0_num/float(len(trainCategory)-sum(trainCategory)+2)
    print 'p1_vec: ', p1_vect
    print 'p0_vec: ', p0_vect
    return log(p0_vect), log(p1_vect), pAbusive

def classifyNB(vec_2_classify, p0_vect, p1_vect, p_class_1):
    p1 = sum(vec_2_classify * p1_vect) + log(p_class_1)
    p0 = sum(vec_2_classify * p0_vect) + log(1.0 - p_class_1)
    print 'p1 = ', p1, ' p0 = ', p0
    if p1 > p0:
        return 1
    else:
        return 0

def testingNB():
    word_list, class_list = loadDataSet()
    unique_word_list = createVocabList(word_list)
    print unique_word_list
    trainMatrix = []
    for word_in_doc in word_list:
        trainMatrix.append(setOfWords2Vec(unique_word_list, word_in_doc))
    p0v, p1v, pAb = trainNB0(array(trainMatrix), array(class_list))
    test_entry = ['a', 'c']
    this_doc = array(setOfWords2Vec(unique_word_list, test_entry))
    print this_doc
    print test_entry, 'classfied as: ', classifyNB(this_doc, p0v, p1v, pAb)
    test_entry = ['b', 'c', 'd']
    this_doc = array(setOfWords2Vec(unique_word_list, test_entry))
    print this_doc
    print test_entry, 'classfied as: ', classifyNB(this_doc, p0v, p1v, pAb)

def text_parse(big_string):
    import re
    list_of_tokens = re.split(r'\W*', big_string)
    return [tok.lower() for tok in list_of_tokens if len(tok) > 2]

def email_test():
    doc_list = []; class_list = []; full_text = []
    for i in range(1, 11):
        word_list = text_parse(open('sample_emails/paper/%d.txt' % i).read())
        doc_list.append(word_list)
        full_text.append(word_list)
        class_list.append(1)
        word_list = text_parse(open('sample_emails/marry/%d.txt' % i).read())
        doc_list.append(word_list)
        full_text.append(word_list)
        class_list.append(0)
    unique_word_list = createVocabList(doc_list)
    training_set = range(20); test_set = []
    for i in range(4):
        rand_index = int(random.uniform(0, len(training_set)))
        test_set.append(training_set[rand_index])
        del(training_set[rand_index])
    train_mat = []; train_class = []
    for doc_index in training_set:
        train_mat.append(setOfWords2Vec(unique_word_list, doc_list[doc_index]))
        train_class.append(class_list[doc_index])
    p0v, p1v, p_email = trainNB0(array(train_mat), array(train_class))
    error_count = 0
    for doc_index in test_set:
        word_vector = setOfWords2Vec(unique_word_list, doc_list[doc_index])
        if classifyNB(array(word_vector), p0v, p1v, p_email) != class_list[doc_index]:
            error_count += 1
    print 'the error rate is: ', float(error_count)/len(test_set)


