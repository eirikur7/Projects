import matplotlib

def open_file(filename):
    '''Return file stream return none otherwise'''
    try:
        return open(filename)
    except FileNotFoundError:
        return None

def read_file(file_stream):
    '''Return a list of lists'''
    data_list = []
    for line in file_stream:
        data_list.append(line.strip().split())
    return data_list


### Main Code ###
FILENAME = 'sick'


