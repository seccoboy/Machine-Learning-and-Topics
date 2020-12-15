import nltk 
import gensim
from nltk.tokenize import RegexpTokenizer
from gensim.models import Phrases
from gensim.utils import simple_preprocess as process

def lemmantizator():
    file = open('arquivao.txt', 'r')
    docs = file.readlines()
    # Split the documents into tokens.
    tokenizer = RegexpTokenizer(r'\w+')
    for idx in range(len(docs)):
        docs[idx] = docs[idx].lower()  # Convert to lowercase.
        docs[idx] = tokenizer.tokenize(docs[idx])  # Split into words.

    # Remove numbers, but not words that contain numbers.
    docs = [[token for token in doc if not token.isnumeric()] for doc in docs]

    # Remove words that are only one character.
    docs = [[token for token in doc if len(token) > 3] for doc in docs]
    nltk.download('wordnet')
    from nltk.stem.wordnet import WordNetLemmatizer

    lemmatizer = WordNetLemmatizer()
    docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]

    # Remove rare and common tokens.
    from gensim.corpora import Dictionary
    # Create a dictionary representation of the documents.
    dictionary = Dictionary(docs)
    # Filter out words that occur less than 20 documents, or more than 50% of the documents.
    dictionary.filter_extremes(no_below=20, no_above=0.5)
    # Bag-of-words representation of the documents.
    corpus = [dictionary.doc2bow(doc) for doc in docs]
    print('Number of unique tokens: ', len(dictionary))
    print('Number of documents: ', len(corpus))
    
  
    # Add bigrams and trigrams to docs (only ones that appear 20 times or more).
    bigram = Phrases(docs, min_count=20)
   
    docs=[bigram[d] for d in docs]
   
    with open('bigrammed.txt', 'w') as f:
        for item in docs:
            f.write("%s" % item)
    f.close()
    
def main():
    lemmantizator() #DONE
    print('Created bigrammed.txt')
main()