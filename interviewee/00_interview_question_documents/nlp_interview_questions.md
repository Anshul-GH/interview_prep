1. What is NLP (Natural Language Processing)?
- Field of Computer Science that deals with communication between computer systems and humans
- A stream of AI that deals with processing human languages.
- Additionally, python supports objects, modules, threads, exception-handling, and automatic memory management
***

2. Real-life applications of NLP?
- Google Translate
- Chatbots
***

3. What are Stop Words?
- Words that bind the sentences but do not add to meaning.
- Articles, prepositions etc
- In NLPs context, Stop Words are generally ignored while interpreting the meaning
***

4. What is NLTK?
- NLTK is a python library that stands for 'Natural Language Toolkit'.
- It helps with:
    * Parsing
    * Tokenization
    * Lemmatization
    * Stemming
***

5. What is Syntactic Analysis?
- Techniqe of analyzing sentences for extracting meaning from it.
- Using syntactic analysis, a machine can analyse and understand the order of words arranged in a sentence.

![](https://intellipaat.com/blog/wp-content/uploads/2020/05/11-1.jpg)

- Syntactic Analysis flow:
    * Parsing: Helps in deciding the strucutre of a sentence or text in a document. It helps in analyzing the words in the text based on the grammar of the language.
    * Word Segmentation: The segmentation of words segregates the text into small significant units.
    * Morphological Segmentation: The purpose of morphological segmentation is to break words into their base form.
    * Stemming: It is the process of removing the suffix from a word to obtain its root word.
    * Lemmatization: It helps combine words using suffixes, without altering the meaning of the word.
***

6. What is Sementic Analysis?
- Sementic analysis helps make a machine understand the meaning of a text.
- It uses various algorithms for the interpretation of words in sentences.
- It also helps in understanding the structure of a sentence.

![](https://intellipaat.com/blog/wp-content/uploads/2020/05/14.jpg)

- Techniques:
    * Named entity recognition: Process of information retrieval that helps identify entities such as the name of the person, organization, place, time, emotion etc
    * Word sense disambiguation: It helps identify the sense of a word used in different sentences
    * Natural language generation: It is a process used by the software to convert structured data into human spoken language.
***

7. List the components of NLP.
- Entity Extraction: It refers to the retrieval of information by segmentation of sentence. It helps with recognition of an entity in a text.
- Syntactic Analysis: Syntactic analysis helps draw the specific meaning of a text
- Pragmatic Analysis: Process of finding useful information from text
***

8. What is TF-IDF?
- Term Frequency - Inverse Document Frequency indicates the importance of a word in a set.
- It helps in information retrieval with numerical statistics.
- TF helps in calculating the ratio of the frequency of a term in a document and the total number of terms.
- IDF denotes the importance of a term in a document.
- When (TF * IDF) is high, the frequency of the term is less and vice-versa.

    * TF(W) = (Frequency of W in the document)/(Total number of terms in the document)
    * IDF(W) = log_e((Total number of documents)/(Number of documents having the term, W))
***

9. What is POS?.
- POS stands for Part-Of-Speech
- It is a process of converting a semtence into various forms, like:
    * list of words
    * list of tuples
- These forms get 'tags' which indicate whether the word is a noun, adjective, verb etc
- Code Snippet:
```
from nltk.tag import DefaultTagger

# defining the tag
tagging = DefaultTagger('NN')

# tagging
tagging.tag(['Hello', 'Geeks'])

# Output: [('Hello', 'NN'), ('Geeks', 'NN')]

```
- Each tagger has a 'tag()' method that takes a list of tokens (list of words produced by the word tokenizer), where each token is a single word.
***

10. Unigrams, Bigrams, Trigrams and n-grams in NLP.
- Unigram: Parsing the sentence, one word at a time.
- Bigram: Parsing the sentence, two words at a time.
....
- n-gram: Parsing the sentence, 'n' words at a time.
*** 

11. What are the steps involved in solving an NLP problem?
- Gather text
- Apply stemming and lemmatization for cleanup
- Feature engineering
- Embed using word2vec
- Train the built model using Neural Network based or other ML approaches
- Evaluate the model performance
- Make appropriate changes to the model to optimize
- Deploy the model
***

