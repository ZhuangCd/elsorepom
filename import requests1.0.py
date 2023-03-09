
from bs4 import BeautifulSoup
import requests
import re
import json
import huspacy

def get_related_words(url, keyword_1, keyword_2):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_text = ''
    for p in soup.find_all('p'):
        article_text += p.text

    # Regular expression to find all words in the article text
    words = re.findall(r'\b\w+\b', article_text)

    # Filter out the common words
    common_words = {'a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'and', 'or', 'but', 'is', 'are', 'was', 'were', 'has', 'have', 'had', 'be', 'been', 'am', 'are', 'is', 'will', 'would', 'should', 'could'}
    words = [word.lower() for word in words if word.lower() not in common_words]

    # Find the related words
    related_words = {}
    for word in words:
        if keyword_1.lower() in word or keyword_2.lower() in word:
            if word not in related_words:
                related_words[word] = 1
            else:
                related_words[word] += 1

    # Sort the related words by frequency
    related_words = {k: v for k, v in sorted(related_words.items(), key=lambda item: item[1], reverse=True)}

    # Get the top 5 related words for each keyword
    top_related_words = {}
    for keyword in [keyword_1, keyword_2]:
        keyword_related_words = []
        for word in related_words:
            if keyword.lower() in word and len(keyword_related_words) < 5:
                keyword_related_words.append(word)
        top_related_words[keyword] = keyword_related_words

    return top_related_words

# Example usage
url = 'https://www.example.com'
related_words = get_related_words(url, 'Európai', 'Nemzeti')

# Save the related words to a JSON file
with open('related_words.json', 'w') as f:
    json.dump(related_words, f, indent=4)