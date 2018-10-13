import re, pprint, os , numpy
import nltk
from sklearn.metrics.cluster import *
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import adjusted_rand_score
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
import string
from nltk.stem.porter import PorterStemmer


def translate_text(text):

    if TextBlob(text).detect_language() != 'en':
        return TextBlob(text).translate(to = "en").string
    else:
        return text


def remove_stopwords(tokens):

    not_stopwords_tokens = []
    for token in tokens:
        token = token.lower()
        if token not in set(stopwords.words('english')):
            not_stopwords_tokens.append(token)

    return not_stopwords_tokens


def clean_others(tokens):
    others = list(string.digits + string.punctuation)

    no_others = []
    for token in tokens:
        if token not in others and re.search('[a-zA-Z]', token):
            no_others.append(token)

    return no_others


def wordnet_value(value):

    if value.startswith('J'):
        return wordnet.ADJ
    elif value.startswith('V'):
        return wordnet.VERB
    elif value.startswith('N'):
        return wordnet.NOUN
    elif value.startswith('R'):
        return wordnet.ADV
    else:
        return ''

def lemmatize(tokens):
    tokens = nltk.pos_tag(tokens)
    wn_lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = []

    for token in tokens:
        if len(token) > 0:
            pos = wordnet_value(token[1])

            if pos != '':
                lemma = wn_lemmatizer.lemmatize(str(token[0]).lower(), pos=pos)
                lemmatized_tokens.append(lemma)

    return lemmatized_tokens

def stemming(tokens):
    stemmer = PorterStemmer()
    stemmer_token = []
    for token in tokens:
        stems = stemmer.stem(token)
        stemmer_token.append(stems)
    tokens = stemmer_token
    return tokens


def named_entities(tree):
    ne = []
    if hasattr(tree, 'label') and tree.label:
        if tree.label() == 'NE':
            for child in tree:
                ne.append(' '.join(child[0]))
        else:
            for child in tree:
                ne.extend(named_entities(child))
    return ne



def cluster_texts(texts, clustersNumber, distance):
    #Load the list of texts into a TextCollection object.
    collection = nltk.TextCollection(texts)
    print("Created a collection of", len(collection), "terms.")

    #get a list of unique terms
    unique_terms = list(set(collection))

    print("Unique terms found: ", len(unique_terms))

    ### And here we actually call the function and create our array of vectors.
    vectors = [numpy.array(TF(f,unique_terms, collection)) for f in texts]
    print("Vectors created.")

    # initialize the clusterer
    clusterer = AgglomerativeClustering(n_clusters=clustersNumber,
                                      linkage="average", affinity=distance)
    clusters = clusterer.fit_predict(vectors)

    return clusters

# Function to create a TF vector for one document. For each of
# our unique words, we have a feature which is the tf for that word
# in the current document
def TF(document, unique_terms, collection):
    word_tf = []
    for word in unique_terms:
        word_tf.append(collection.tf(word, document))
    return word_tf

if __name__ == "__main__":

    named_ent = True

    folder = "CorpusNoticiasPractica1718"

    # Empty list to hold text documents.
    texts = []

    listing = sorted(os.listdir(folder))
    for file in listing:

        if file.endswith(".txt") :

            url = folder+"/"+file
            f = open(url, encoding="utf-8");
            raw = f.read()
            f.close()

            # Traducir a ingles
            text = translate_text(raw)

            # Tokenizamos por frase
            sentences = nltk.sent_tokenize(text)

            # Tokenizamos por palabra
            tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

            final_tokens = []

            # Si utilizamos entidades nombradas

            if named_ent:
                tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
                chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

                for sentence in chunked_sentences:
                    final_tokens.extend(named_entities(sentence))

            # Si no utilizamos entidades nombradas
            else:

                for tokens in tokenized_sentences:

                    tokens = remove_stopwords(tokens)
                    tokens = clean_others(tokens)
                    tokens = lemmatize(tokens)
                    tokens = stemming(tokens)
                    final_tokens.extend(tokens)

            text = nltk.Text(final_tokens)
            texts.append(text)

    print("Prepared ", len(texts), " documents...")
    print("They can be accessed using texts[0] - texts[" + str(len(texts)-1) + "]")

    distanceFunction ="cosine"
    #distanceFunction = "euclidean"
    test = cluster_texts(texts,5,distanceFunction)
    print("test: ", test)
    # Gold Standard
    reference =[0, 5, 0, 0, 0, 2, 2, 2, 3, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 0, 2, 5]
    print("reference: ", reference)

    # Evaluation
    print("rand_score: ", adjusted_rand_score(reference, test))
