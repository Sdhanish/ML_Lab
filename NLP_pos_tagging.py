import nltk
from nltk import pos_tag, word_tokenize, ngrams
from nltk.chunk import RegexpParser
from collections import Counter
# Download necessary NLTK resources
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
# Sample text
text = "The quick brown fox jumps over the lazy dog."
# Step 1: POS Tagging
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
print("POS Tags:", pos_tags)
# Step 2: N-gram Generation (Bigrams)
n = 2  # Use 2 for bigrams, 3 for trigrams, etc.
bigrams = list(ngrams(tokens, n))
print("\nBigrams:", bigrams)
# Step 3: Simple Smoothing using Laplace Smoothing
bigram_counts = Counter(bigrams)
vocab_size = len(set(tokens))
total_bigrams = sum(bigram_counts.values())
# Laplace Smoothing
smoothed_probs = {bigram: (count + 1) / (total_bigrams + vocab_size) for bigram, count in bigram_counts.items()}
print("\nSmoothed Probabilities of Bigrams:", smoothed_probs)
# Step 4: Chunking with a simple noun phrase (NP) grammar
grammar = "NP: {<DT>?<JJ>*<NN>}"  # Rule for noun phrase (NP)
