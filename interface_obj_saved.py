'''
I have saved using pickle the result of the hello_word_ydk for later analysis
'''

import pickle

def save(object, filename):
    '''
    This will use the pickle library to save the object to a file
    :param object:
    :param filename:
    '''
    with open(filename, 'wb') as f:
        pickle.dump(object,f)

def load(filename):
    '''
    This will load an object from the previously created file
    :param filename:
    :return: object
    '''
    with open (filename, 'br') as f:
        object = pickle.load(f)
    return object

if __name__ == '__main__':
    filename = 'interface.pkl'
    interface = load(filename)

