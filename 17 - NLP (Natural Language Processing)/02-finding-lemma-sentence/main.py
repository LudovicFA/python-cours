from nltk.stem import WordNetLemmatizer
import nltk

lemmatizer = WordNetLemmatizer()

def lemma_me(sentence):
    sentence_token = nltk.word_tokenize(sentence.lower())
    sentence_lemma = []
    pos_tags = nltk.pos_tag(sentence_token)
    for token,pos_tag in zip(sentence_token, pos_tags):
        if(pos_tag[1][0].lower() in ['n','v', 'a','r']):
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemma.append(lemma)
    return sentence_lemma

print(lemma_me("Vegetables are types of plants."))
print(lemma_me("A vegetables is a type of plant."))