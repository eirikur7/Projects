def censor_words(data_list, word):
    '''Censored (word) from (data_list), inserts ------ instead'''
    new_list = []
    # Each line is a whole sentence
    for line in data_list:
        new_line = line.lower()
        num_words = range(new_line.count(word))
        # Goes through instances where the word is often in sentence
        for instances in num_words:
                i_1 = new_line.find(word)
                i_2 = i_1 + len(word)
                censor = '-' * len(word)

                line = line[:i_1] + censor + line[i_2:]
                new_line = line

        new_list.append(line)

    return new_list

def censor_list(data_list,word_list):
    for word in word_list:
        data_list = censor_words(data_list, word)
    return data_list

def censor_after_X_occurences(data_list, word_list, X):
    '''Censored (word) from (data_list), inserts ------ instead'''
    new_list = []
    occurences = 0
    count = 0
    # Each line is a whole sentence
    for line in data_list:
        for word in word_list:
            new_line = line.lower()
            num_words = range(new_line.count(word))
            # Goes through instances where the word is often in sentence
            for instances in num_words:
                count += 1
                if count > X:
                    i_1 = new_line.find(word)
                    i_2 = i_1 + len(word)
                    censor = '-' * len(word)

                    line = line[:i_1] + censor + line[i_2:]
                    new_line = line

        new_list.append(line)

    return new_list

def main():
    email_one = open("email_one.txt", "r").read().split('\n')
    censor_word = 'learning algorithms'
    email_one = censor_words(email_one,censor_word)

    email_two = open("email_two.txt", "r").read().split('\n')
    proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
    email_two = censor_list(email_two,proprietary_terms)

    email_three = open("email_three.txt", "r").read().split('\n')
    negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed",
     "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", 
     "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
    OCCURANCES = 2
    email_three = censor_after_X_occurences(email_three, negative_words, OCCURANCES)

    for line in email_three:
        print(line)

    


main()

# email_one = open("email_one.txt", "r").read()
# email_two = open("email_two.txt", "r").read()
# email_three = open("email_three.txt", "r").read()
# email_four = open("email_four.txt", "r").read()

