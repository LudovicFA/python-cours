from nltk.stem import WordNetLemmatizer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

lemmatizer = WordNetLemmatizer()
text = "Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked."

def lemma_me(sentence):
    sentence_token = nltk.word_tokenize(sentence.lower())
    sentence_lemma = []
    pos_tags = nltk.pos_tag(sentence_token)
    for token,pos_tag in zip(sentence_token, pos_tags):
        if(pos_tag[1][0].lower() in ['n','v', 'a','r']):
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemma.append(lemma)
    return sentence_lemma

sentence_tokens = nltk.sent_tokenize(text)
print(sentence_tokens)
tv = TfidfVectorizer(tokenizer=lemma_me)
tf = tv.fit_transform(sentence_tokens)
# print(lemma_me("Vegetables are types of plants."))
# print(lemma_me("A vegetables is a type of plant."))