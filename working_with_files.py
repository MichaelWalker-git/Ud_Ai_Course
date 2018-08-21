# f = open('/my_path/my_file.txt', 'r')
# file_data = f.read()
# f.close()
# # Closes and reduces the operation/ file handlers. Depends on OS. OSERROR\\

##########
# # File can be thought of as a huge string
# f = open('/my_path/my_file.txt', 'w')
# #  Writing mode, can overwrite
#
# # Use append instead of write
#
# # If it doesn't exist, python will create the file.
#

##########
# # Autoclose and only asseccible throught the scope block
# with open('another_file,text', 'r') as f:
#     file_data = f.read()
#     print(file_data)

##########
# with open("camelot.txt") as song:
#     print(song.read(2))
#     print(song.read(8))
#     print(song.read())

##########
# Utilizing readline, reads line by line. Strip removes the newline character.
# camelot_lines = []
# # with open("camelot.txt") as f:
# #     for line in f:
# #         camelot_lines.append(line.strip())
# #
# # print(camelot_lines)

##########
# def create_cast_list(filename):
#     cast_list = []
#     #use with to open the file filename
#     with open(filename) as f:
#         for line in f:
#             cast_list.append(line.split(',')[0])
#     return cast_list
#
# cast_list = create_cast_list('flying_circus_cast.txt')
# for actor in cast_list:
#     print(actor)
#
##########

# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
def generate_password():
    random_words = []
    i = 0
    word_length = len(word_list)
    while i < 3:
        ran_num = random.randrange(0, word_length)
        random_words.append(word_list[ran_num])
        i += 1
    return ' '.join(random_words)

# test your function
print(generate_password())