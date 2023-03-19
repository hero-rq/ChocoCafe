import click
import requests
import re
from bs4 import BeautifulSoup
from collections import Counter

def fetch_html_content(url):
    """Fetches the HTML content of a webpage at a given URL."""
    response = requests.get(url)
    response.raise_for_status() # raise an exception for non-200 status codes
    return response.text

def extract_words_from_text(text, min_length=0):
    """Extracts all words from a given text with a minimum length."""
    return [word.lower() for word in re.findall(r'\w+', text) if len(word) >= min_length]

def count_word_occurrences_in_list(words):
    """Counts the number of occurrences of each word in a list of words."""
    return Counter(words)

def print_top_words_in_dict(word_counts, n=10):
    """Prints the n most common words and their counts in a word count dictionary."""
    for word, count in word_counts.most_common(n):
        print(f'{word}: {count}')

@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL of webpage to extract from.')
@click.option('--min-length', '-l', default=0, help='Minimum word length (default: 0, no limit).')
def main(url, min_length):
    """Main function that extracts words from a webpage, counts their occurrences, and prints the top words."""
    html = fetch_html_content(url)
    words = extract_words_from_text(html, min_length)
    word_counts = count_word_occurrences_in_list(words)
    print_top_words_in_dict(word_counts)

if __name__ == '__main__':
    main()
