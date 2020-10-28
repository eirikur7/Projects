def censor_word(main_str, censor_str, insert_str):
    '''Censores str from a_str, inserts another string instead'''
    main_str_lower = main_str.lower()
    if censor_str in main_str:
        # Find indexes on each side of word
        i_1 = main_str.find(censor_str)
        i_2 = i_1 + len(censor_str)
        # What will be put instead of the word
        censor = insert_str * len(censor_str)
        # Makes the new string
        main_str = main_str[:i_1] + censor + main_str[i_2:]
    return main_str

def list_censor_word(a_list, a_str, censor_str):
    new_list = []
    for line in a_list:
        for occurences in range(line.count(a_str)):
            line = censor_word(line, a_str, censor_str)
        new_list.append(line)
    return new_list

def list_censor_list(main_list, censor_list, insert_str):
    for word in censor_list:
        main_list = list_censor_word(main_list, word, insert_str)
    return main_list

def list_censor_word_occurenses(main_list, censor_list, insert_str, occurences):
    new_list = []
    for line in main_list:
        for word in censor_list:
            counter = 0
            # How many time the word comes upp in the list
            for num in range(line.count(word)):
                counter += 1
                if counter > occurences:
                    line = censor_word(line, word, insert_str)
        new_list.append(line)
    return new_list


    
def main():
    censor_ch = '-'
    email_one = open("email_one.txt", "r").read().split('\n')
    censor_word = 'learning algorithms'
    email_one = list_censor_word(email_one, censor_word, censor_ch)
    
    email_two = open("email_two.txt", "r").read().split('\n')
    proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
    email_two = list_censor_list(email_two, proprietary_terms, censor_ch)

    email_three = open("email_three.txt", "r").read().split('\n')
    negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed",
     "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", 
     "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
    OCCURANCES = 2
    email_three = list_censor_word_occurenses(email_three, negative_words, censor_ch, OCCURANCES)
    for line in email_three:
        print(line)

main()