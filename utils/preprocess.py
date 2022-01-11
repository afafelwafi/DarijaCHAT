from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
import re 
import string
import nltk
from nltk.corpus import stopwords

# Preprocessing
nltk.download('stopwords')

UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOW = "abcdefghijklmnopqrstuvwxyz"
LATIN = "Ààéêèç"
SPACE = '\t\n\r\v\f'
fr_stopwords=stopwords.words('french')

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#all_latin_chars = UP + LOW + LATIN

punctuations = string.punctuation

punctuations_list =  punctuations + SPACE

french_punctuations_list= punctuations_list.replace("'","")


#Full List of emogies to be removed
emoji_pattern = re.compile("["
                       #u"\U0001F600-\U0001F64F"  # emoticons to keep 
                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       u"\U00002702-\U000027B0"
                       u"\U000024C2-\U0001F251"
                       u"\U0001f932"
                       u"\u200f"
                       u"\U0001F914"
                       u"\U0001F923"
                       u"\u200D"
                       u"\u202c"
                       u"\u2069"
                       u"\u2066"
                       u"\U0001F926"
                       u"\U0001F917"
                       u"\U0001f928"
                       u"\t"
                       u"\u200e"
                       "]+", flags=re.UNICODE)

print(punctuations)

# Remove punctuation
def remove_french_punctuations(text):
    translator = str.maketrans('', '', french_punctuations_list)
    return text.translate(translator)
#remove french stop words, here we specified just Fr stop words, you can add other DZ word that you juge as stop words 
def remove_fr_stop_words(text):
    temp_text=[]
    for word in text.split(" "):
        if word not in fr_stopwords:
            temp_text.append(word)
    return ' '.join(temp_text)
# remove digits delimited with white space
def remove_digits(text):
    text= re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", text)
    return text

# remove emogies 
def remove_emoji(text):
    return emoji_pattern.sub(r' ' , text)

#remove all arabic characters from a text
def remove_french_chars(text):
    new_text = ""
    for char in text:
        if char not in LETTERS:
            new_text += char
    return new_text

# remove digits delimited with white space
def remove_digits(text):
    text= re.sub(r'\d+', '', text)
    return text

# remove extra stop words 
def remove_extra_white_spaces(text):
    text= ' '.join(text.split())
    return text

#this is the pipeline of preprocessing 
def preprocess(text,list_words=[]):
    text=remove_french_chars(text)
    text=remove_digits(text) 
    text=remove_french_punctuations(text) 
    text=remove_fr_stop_words(text) 
    text=remove_extra_white_spaces(text) 
    text=remove_emoji(text)
   # text=rem_vowel(text)
   # text=remove_noise(text)
    return text

