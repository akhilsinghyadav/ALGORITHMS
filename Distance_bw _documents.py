#This algorithm is used to find out variation between 2 documents.(i.e. Somehow like Cheating Catcher)

import math
import sys

def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.readlines()
    except IOError:
        print("Error opening or reading input file: ", filename)
    
        sys.exit()

def get_words_from_line_list(L):
    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list = word_list + words_in_line
    return word_list

def get_words_from_string(line):
    word_list = []          # accumulates words in line
    character_list = []     # accumulates characters in word
    for c in line:
        if c.isalnum():
            character_list.append(c)
        elif len(character_list)>0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
            character_list = []
    if len(character_list)>0:
        word = "".join(character_list)
        word = word.lower()
        word_list.append(word)
    return word_list
    
def insertion_sort(A):
    for j in range(len(A)):
        key = A[j]
        # insert A[j] into sorted sequence A[0..j-1]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A
    
def word_frequencies_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    insertion_sort(freq_mapping)

    print("File",filename,":")
    print(len(line_list),"lines,")
    print(len(word_list),"words,")
    print(len(freq_mapping),"distinct words")

    return freq_mapping
    
def count_frequency(word_list):
    L = []
    for new_word in word_list:
        for entry in L:
            if new_word == entry[0]:
                entry[1] = entry[1] + 1
                break
        else:
            L.append([new_word,1])
    return L
    
def inner_product(L1,L2):
    sum = 0.0
    for word1, count1 in L1:
        for word2, count2 in L2:
            if word1 == word2:
                sum += count1 * count2
    return sum
    
def vector_angle(L1,L2):
    numerator = inner_product(L1, L2)
    denominator = math.sqrt(inner_product(L1,L2)*inner_product(L2,L2))
    return math.acos(numerator/denominator)
    
# if you want to run code in IDE then just replace sys.argv[1] and sys.argv[2] to "file 1 name" and "file 2 name"


def main():
    if len(sys.argv) != 3:
         print("Usage: docdist1.py filename_1 filename_2")
    else:
        filename_1 = sys.argv[1]  
        filename_2 = sys.argv[2]
        sorted_word_list_1 = word_frequencies_for_file(filename_1)
        sorted_word_list_2 = word_frequencies_for_file(filename_2)
        distance = vector_angle(sorted_word_list_1,sorted_word_list_2)
        print("The distance between the documents is: %0.6f (radians)"%distance)
if __name__=="__main__":
    import profile
    profile.run("main()")
