import math
import string
import sys

#read file

def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print(f"error while opening or reading input file: {filename})
        sys.exit()

#split lines to words

translation_table = string.maketrans(string.punctuation + string.uppercase, " "*len(string.punctuation) + string.lowercase)

def get_words_from_line(text):
    text = text.translate(translational_table)
    word_list = text.split()
    return word_list

# count word frequencies

def count_frequency(word_list):
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word] + 1
        else:
            D[new_word] = 1
    return D

#compute frequncy from input file 
 
def word_frequencies(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line(line_list)
    freq_mapping = count_frequency(word_list)
    
    print(f"File:{filename}, {len(line_list)} lines, {len(word_list)} words, {len(freq_mapping)} distinctive words")
    return freq_mapping

# inner product 

def inner_product(D1,D2):
    sum = 0.0
    for key in D1:
        if key in D2:
            sum += D1[key] * D2[key]
    return sum

def vector_angle(D1,D2):
    numerator = innner_product(D1,D2) 
    denominator = math.sqrt(inner_product(D1,D1)*inner_product(D2,D2)
    return math.acos(numerator/denominator)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: Program_file.py {filename_1} {filename_2}")
    else:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
        sorted_word_list1 = word_frequencies(filename_1)
        sorted_word_list2 = word_frequencies(filename_2)
        distance = vector_angle(sorted_word_list1, sorted_word_list2)
        print("The distance betweem the documents is: %0.6f (radians)", %distance)
                            
#initiater
if __name__=="__main__":
    import profile
    profile.run("main()")                            
                            
