class Censor:
    def __init__(self, string='', censor='-'):
        self.censor = censor
        if type(string) is list:
            self._StrLst = string
            self._StrLstLwr = [w.strip().lower() for w in string]
        else:
            self.__StringToList(string)

    def __str__(self):
        '''Return string in string format'''
        return ' '.join(self._StrLst)

    def add_email(self, string):
        '''Add string here'''
        self.__init__(string=string)

    # add words that are to be censored
    def add_censor_list(self, a_list):
        self.censor_lst = a_list

    # censors only one word from word_list
    def __CensorWord(self, word=''):
        '''Sensor one word from string'''
        word = word.lower().strip()

        for _ in self._StrLstLwr.count(word):
            the_censor = self.censor * len(word)

            idx = self._StrLstLwr.index(word)
            self._StrLstLwr[idx] = the_censor
            self._StrLst[idx] = the_censor

    # calls __CensorWord multiple times
    def censor_it(self, word_list=[]):
        '''Will censor multiple words.'''
        self.censor_lst = word_list
        for word in self.censor_lst:
            self.__CensorWord(word)
        return self.__str__()

    def __StringToList(self, string):
        '''Return a two list of word, one original and other with lowercase'''
        self._StrLst = []
        self._StrLstLwr = []
        for line in string.split('\n'):
            line += '\n'
            for word in line.split(' '):
                self._StrLst.append(word)
                self._StrLstLwr.append(word.strip().split())
        
def open_file(filename):
    try:
        return open(filename, 'r')
    except FileNotFoundError:
        return None
    
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", 
                    "learning algorithm", "her", "herself"]

path = 'C:/Users/ebben/Dropbox/Projects/Censor_Dispenser'
filename = '\email_four.txt'
file_object = open_file(path+filename)
if file_object:
    data = file_object.read()
    print(data)
    print('\n\n\n')

    email = Censor(data)
    email.add_censor_list(proprietary_terms)
    email.censor_it()
    print(email)
