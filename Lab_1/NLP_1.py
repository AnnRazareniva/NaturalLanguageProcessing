
import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
import pymorphy3
m = pymorphy3.MorphAnalyzer()



f = open('mumiTroll.txt', 'r', encoding='utf-8')

text = f.read()
text_segmentation = sent_tokenize(text)

for i in range (len(text_segmentation)):
    token = word_tokenize(text_segmentation[i])
    m = pymorphy3.MorphAnalyzer()
   
    for j in range (len(token)-1): 
        w1 = m.parse(token[j])[0]
        w2 = m.parse(token[j+1])[0]
        if (w1.tag.gender == w2.tag.gender and 
            w1.tag.number == w2.tag.number and 
            w1.tag.case == w2.tag.case and 
            (w1.tag.POS == 'NOUN' and w2.tag.POS == 'ADJF' or
             w1.tag.POS == 'ADJF' and w2.tag.POS == 'NOUN')):
            print(w1.normal_form, w2.normal_form)