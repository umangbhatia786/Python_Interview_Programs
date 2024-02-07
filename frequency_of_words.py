def get_frequency_of_words(input_string):
    word_list = input_string.replace('.','').split(' ')

    return {word:word_list.count(word) for word in word_list}


sample_string = input('Input your sentence here: ')

print('******** Your Word Frequency in the sentence is as below **********')

frequency_dict = get_frequency_of_words(sample_string)

for k,v in frequency_dict.items():
    print(f'{k} : {v}')