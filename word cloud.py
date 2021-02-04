import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys

def calculate_frequencies(file_contents):
    # Uninteresting words to remove
    uninteresting_words = ["about", "over", "like", "so", "in", "into", "then", "on", "there", "for", "said", "up", "the", "out", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # Convert string of text into dictionary of words and frequencies
    all_words = file_contents.split()
    clean_words = {}
    for word in all_words:
        word = word.lower().strip('!()-[]{};:\'"\,<>./?@#$%^&*_~')
        if word in uninteresting_words:
            continue
        elif word in clean_words:
            clean_words[word] += 1
        else:
            clean_words[word] = 1
    
    # Generate wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(clean_words)
    
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

#Open and read the Gatsby text file
    
g = open('great_gatsby.txt', 'r')
gatsby = ''

for line in g:
    gatsby += line
g.close()

# Call the function
calculate_frequencies(gatsby)

