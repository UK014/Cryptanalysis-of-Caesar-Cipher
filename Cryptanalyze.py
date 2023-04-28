import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string = []
f = open("Caeser Encrypt.txt","r")
encrypted_text = f.read().lower()
         
shift_possibility_1 = 1
shift_possibility_2 = 2
shift_possibility_3 = 3
shift_possibility_4 = 4
shift_possibility_5 = 5
shift_possibility_6 = 6
shift_possibility_7 = 7
shift_possibility_8 = 8
shift_possibility_9 = 9
shift_possibility_10= 10
shift_possibility_11= 11
shift_possibility_12= 12
shift_possibility_13= 13
shift_possibility_14= 14
shift_possibility_15= 15
shift_possibility_16= 16
shift_possibility_17= 17
shift_possibility_18= 18
shift_possibility_19= 19
shift_possibility_20= 20
shift_possibility_21= 21
shift_possibility_22= 22
shift_possibility_23= 23
shift_possibility_24= 24
shift_possibility_25= 25

f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_1 < 0:   
               string[count] = alphabet[26 - (shift_possibility_1 - count2 )]
               break
            elif count2 - shift_possibility_1 >= 0:
               string[count] = alphabet[count2 - shift_possibility_1]
               break
        elif string[count] == ' ':
           string[count] = ' '
encrypted_text1 = "".join(string) 
string.clear()

words = word_tokenize(encrypted_text1)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift1_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0

f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_2 < 0:   
               string[count] = alphabet[26 - (shift_possibility_2 - count2 )]
               break
            elif count2 - shift_possibility_2 >= 0:
               string[count] = alphabet[count2 - shift_possibility_2]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text2 = "".join(string)                   
string.clear()


words = word_tokenize(encrypted_text2)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift2_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_3 < 0:   
               string[count] = alphabet[26 - (shift_possibility_3 - count2 )]
               break
            elif count2 - shift_possibility_3 >= 0:
               string[count] = alphabet[count2 - shift_possibility_3]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text3 = "".join(string)         
string.clear()

words = word_tokenize(encrypted_text3)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift3_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_4 < 0:   
               string[count] = alphabet[26 - (shift_possibility_4 - count2 )]
               break
            elif count2 - shift_possibility_4 >= 0:
               string[count] = alphabet[count2 - shift_possibility_4]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text4 = "".join(string)
string.clear()
f.seek(0)

words = word_tokenize(encrypted_text4)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift4_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_5 < 0:   
               string[count] = alphabet[26 - (shift_possibility_5 - count2 )]
               break
            elif count2 - shift_possibility_5 >= 0:
               string[count] = alphabet[count2 - shift_possibility_5]
               break
        elif string[count] == ' ':
           string[count] = ' '
encrypted_text5 = "".join(string) 

string.clear()

words = word_tokenize(encrypted_text5)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift5_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0

f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_6 < 0:   
               string[count] = alphabet[26 - (shift_possibility_6 - count2 )]
               break
            elif count2 - shift_possibility_6 >= 0:
               string[count] = alphabet[count2 - shift_possibility_6]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text6 = "".join(string)                 
string.clear()

words = word_tokenize(encrypted_text6)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift6_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_7 < 0:   
               string[count] = alphabet[26 - (shift_possibility_7 - count2 )]
               break
            elif count2 - shift_possibility_7 >= 0:
               string[count] = alphabet[count2 - shift_possibility_7]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text7 = "".join(string)         

string.clear()
words = word_tokenize(encrypted_text7)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift7_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_8 < 0:   
               string[count] = alphabet[26 - (shift_possibility_8 - count2 )]
               break
            elif count2 - shift_possibility_8 >= 0:
               string[count] = alphabet[count2 - shift_possibility_8]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text8 = "".join(string)   

string.clear()
words = word_tokenize(encrypted_text8)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift8_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_9 < 0:   
               string[count] = alphabet[26 - (shift_possibility_9 - count2 )]
               break
            elif count2 - shift_possibility_9 >= 0:
               string[count] = alphabet[count2 - shift_possibility_9]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text9 = "".join(string)

string.clear()
words = word_tokenize(encrypted_text9)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift9_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_10 < 0:   
               string[count] = alphabet[26 - (shift_possibility_10 - count2 )]
               break
            elif count2 - shift_possibility_10 >= 0:
               string[count] = alphabet[count2 - shift_possibility_10]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text10 = "".join(string)

string.clear()
words = word_tokenize(encrypted_text10)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift10_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_11 < 0:   
               string[count] = alphabet[26 - (shift_possibility_11 - count2 )]
               break
            elif count2 - shift_possibility_11 >= 0:
               string[count] = alphabet[count2 - shift_possibility_11]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text11 = "".join(string)

string.clear()
words = word_tokenize(encrypted_text11)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift11_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_12 < 0:   
               string[count] = alphabet[26 - (shift_possibility_12 - count2 )]
               break
            elif count2 - shift_possibility_12 >= 0:
               string[count] = alphabet[count2 - shift_possibility_12]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text12 = "".join(string)

string.clear()
words = word_tokenize(encrypted_text12)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift12_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_13 < 0:   
               string[count] = alphabet[26 - (shift_possibility_13 - count2 )]
               break
            elif count2 - shift_possibility_13 >= 0:
               string[count] = alphabet[count2 - shift_possibility_13]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text13 = "".join(string)

string.clear()
words = word_tokenize(encrypted_text13)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift13_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_14 < 0:   
               string[count] = alphabet[26 - (shift_possibility_14 - count2 )]
               break
            elif count2 - shift_possibility_14 >= 0:
               string[count] = alphabet[count2 - shift_possibility_14]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text14 = "".join(string)

string.clear()
words = word_tokenize(encrypted_text14)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift14_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_15 < 0:   
               string[count] = alphabet[26 - (shift_possibility_15 - count2 )]
               break
            elif count2 - shift_possibility_15 >= 0:
               string[count] = alphabet[count2 - shift_possibility_15]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text15 = "".join(string)

string.clear()
words = word_tokenize(encrypted_text15)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift15_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_16 < 0:   
               string[count] = alphabet[26 - (shift_possibility_16 - count2 )]
               break
            elif count2 - shift_possibility_16 >= 0:
               string[count] = alphabet[count2 - shift_possibility_16]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text16 = "".join(string)
words = word_tokenize(encrypted_text16)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift16_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0

string.clear()

f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_17 < 0:   
               string[count] = alphabet[26 - (shift_possibility_17 - count2 )]
               break
            elif count2 - shift_possibility_17 >= 0:
               string[count] = alphabet[count2 - shift_possibility_17]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text17 = "".join(string)

string.clear()
words = word_tokenize(encrypted_text17)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift17_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_18 < 0:   
               string[count] = alphabet[26 - (shift_possibility_18 - count2 )]
               break
            elif count2 - shift_possibility_18 >= 0:
               string[count] = alphabet[count2 - shift_possibility_18]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text18 = "".join(string)
string.clear()
words = word_tokenize(encrypted_text18)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift18_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_19 < 0:   
               string[count] = alphabet[26 - (shift_possibility_19 - count2 )]
               break
            elif count2 - shift_possibility_19 >= 0:
               string[count] = alphabet[count2 - shift_possibility_19]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text19 = "".join(string)
string.clear()
words = word_tokenize(encrypted_text19)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift19_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_20 < 0:   
               string[count] = alphabet[26 - (shift_possibility_20 - count2 )]
               break
            elif count2 - shift_possibility_20 >= 0:
               string[count] = alphabet[count2 - shift_possibility_20]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text20 = "".join(string)
string.clear()
words = word_tokenize(encrypted_text20)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift20_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_21 < 0:   
               string[count] = alphabet[26 - (shift_possibility_21 - count2 )]
               break
            elif count2 - shift_possibility_21 >= 0:
               string[count] = alphabet[count2 - shift_possibility_21]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text21 = "".join(string)
string.clear()
words = word_tokenize(encrypted_text21)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift21_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_22 < 0:   
               string[count] = alphabet[26 - (shift_possibility_22 - count2 )]
               break
            elif count2 - shift_possibility_22 >= 0:
               string[count] = alphabet[count2 - shift_possibility_22]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text22 = "".join(string)
string.clear()
words = word_tokenize(encrypted_text22)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift22_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_23 < 0:   
               string[count] = alphabet[26 - (shift_possibility_23 - count2 )]
               break
            elif count2 - shift_possibility_23 >= 0:
               string[count] = alphabet[count2 - shift_possibility_23]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text23 = "".join(string)
string.clear()
words = word_tokenize(encrypted_text23)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift23_meaningful_word_count =len(words) - len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_24 < 0:   
               string[count] = alphabet[26 - (shift_possibility_24 - count2 )]
               break
            elif count2 - shift_possibility_24 >= 0:
               string[count] = alphabet[count2 - shift_possibility_24]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text24 = "".join(string)
string.clear()
words = word_tokenize(encrypted_text24)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift24_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
f.seek(0)
for l in range (len(encrypted_text)):
    string.append(f.read(1).lower())

for count in range(len(encrypted_text)): 
    for count2 in range(len(alphabet)):         
        if string [count] == alphabet[count2]:
            if count2 - shift_possibility_25 < 0:   
               string[count] = alphabet[26 - (shift_possibility_25 - count2 )]
               break
            elif count2 - shift_possibility_25 >= 0:
               string[count] = alphabet[count2 - shift_possibility_25]
               break
        elif string[count] == ' ':
           string[count] = ' '
          
encrypted_text25 = "".join(string)
words = word_tokenize(encrypted_text25)
filtered_words = [word for word in words if word not in stop_words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
shift25_meaningful_word_count = len(words) -len(lemmatized_words)
lemmatized_words = 0
meaningful_word=[shift1_meaningful_word_count,shift2_meaningful_word_count,shift3_meaningful_word_count,shift4_meaningful_word_count,shift5_meaningful_word_count,shift6_meaningful_word_count,shift7_meaningful_word_count,shift8_meaningful_word_count,shift9_meaningful_word_count,shift10_meaningful_word_count,shift11_meaningful_word_count,shift12_meaningful_word_count,shift13_meaningful_word_count,shift14_meaningful_word_count,shift15_meaningful_word_count,shift16_meaningful_word_count,shift17_meaningful_word_count,shift18_meaningful_word_count,shift19_meaningful_word_count,shift20_meaningful_word_count,shift21_meaningful_word_count,shift22_meaningful_word_count,shift23_meaningful_word_count,shift24_meaningful_word_count,shift25_meaningful_word_count] 
max_index = meaningful_word.index(max(meaningful_word))
fw = open("Possible Plain Texts.txt","w")
if max_index == 0:
    fw.write("Shift = 1: \n" + encrypted_text1)
elif max_index == 1:
    fw.write("Shift = 2: \n" + encrypted_text2 + "\n")
elif max_index == 2:
    fw.write("Shift = 3: \n" + encrypted_text3 + "\n")
elif max_index == 3:
    fw.write("Shift = 4: \n" + encrypted_text4 + "\n")
elif max_index == 4:
    fw.write("Shift = 5: \n" + encrypted_text5 + "\n")
elif max_index == 5:
    fw.write("Shift = 6: \n" + encrypted_text6 + "\n")
elif max_index == 6:
    fw.write("Shift = 7: \n" + encrypted_text7 + "\n")
elif max_index == 7:
    fw.write("Shift = 8: \n" + encrypted_text8 + "\n")
elif max_index == 8:
    fw.write("Shift = 9: \n" + encrypted_text9 + "\n")
elif max_index == 9:
    fw.write("Shift = 10: \n" + encrypted_text10 + "\n")
elif max_index == 10:
    fw.write("Shift = 11: \n" + encrypted_text11 + "\n")
elif max_index == 11:    
    fw.write("Shift = 12: \n" + encrypted_text12 + "\n")
elif max_index == 12:    
    fw.write("Shift = 13: \n" + encrypted_text13 + "\n")
elif max_index == 13:
    fw.write("Shift = 14: \n" + encrypted_text14 + "\n")
elif max_index == 14:
    fw.write("Shift = 15: \n" + encrypted_text15 + "\n")
elif max_index == 15:
    fw.write("Shift = 16: \n" + encrypted_text16 + "\n")
elif max_index == 16:
    fw.write("Shift = 17: \n" + encrypted_text17 + "\n")
elif max_index == 17:
    fw.write("Shift = 18: \n" + encrypted_text18 + "\n")
elif max_index == 18:
    fw.write("Shift = 19: \n" + encrypted_text19 + "\n")
elif max_index == 19:   
    fw.write("Shift = 20: \n" + encrypted_text20 + "\n")
elif max_index == 20:     
    fw.write("Shift = 21: \n" + encrypted_text21 + "\n")
elif max_index == 21:
    fw.write("Shift = 22: \n" + encrypted_text22 + "\n")
elif max_index == 22:     
    fw.write("Shift = 23: \n" + encrypted_text23 + "\n")
elif max_index == 23:     
    fw.write("Shift = 24: \n" + encrypted_text24 + "\n")
elif max_index == 24:               
    fw.write("Shift = 25: \n" + encrypted_text25 + "\n")
    
fw.close()    