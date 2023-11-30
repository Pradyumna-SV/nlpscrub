import re
import emoji
import nltk
import logging
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

class ParseResult:
    def __init__(self, text, urls=None, hashtags=None, mentions=None, reserved_words=None, emojis=None, smileys=None):
        self.text = text
        self.urls = urls or []
        self.hashtags = hashtags or []
        self.mentions = mentions or []
        self.reserved_words = reserved_words or []
        self.emojis = emojis or []
        self.smileys = smileys or []


class TextProcessor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

        # Configure logging
        logging.basicConfig(filename='text_processor.log', level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        # Options handling logic
        self.options = {
            'clean_reserved_words': True,
            'clean_urls': True,
            'clean_hashtags': True,
            'clean_mentions': True,
            'clean_emojis': True,
            'clean_smileys': True,
            'remove_punctuation': True,
            'remove_numbers': True,
            'remove_special_characters': True,
            'convert_to_lowercase': True,
            'remove_extra_whitespace': True,
            'extract_emojis': True,
            'count_emoji_frequency': True,
            'remove_emojis': True,
        }

    def set_options(self, **options):
        # Update options with the provided ones
        self.options.update(options)

    def clean_text(self, text):
        try:
            if self.options.get('clean_reserved_words', True):
                text = self.clean_reserved_words(text)
            if self.options.get('clean_urls', True):
                text = self.clean_urls(text)
            if self.options.get('clean_hashtags', True):
                text = self.clean_hashtags(text)
            if self.options.get('clean_mentions', True):
                text = self.clean_mentions(text)
            if self.options.get('clean_emojis', True):
                text = self.clean_emojis(text)
            if self.options.get('clean_smileys', True):
                text = self.clean_smileys(text)
            if self.options.get('remove_punctuation', True):
                text = self.remove_punctuation(text)
            if self.options.get('remove_numbers', True):
                text = self.remove_numbers(text)
            if self.options.get('remove_special_characters', True):
                text = self.remove_special_characters(text)
            if self.options.get('convert_to_lowercase', True):
                text = self.convert_to_lowercase(text)
            if self.options.get('remove_extra_whitespace', True):
                text = self.remove_extra_whitespace(text)
            if self.options.get('extract_emojis', True):
                emojis = self.extract_emojis(text)
                print("Extracted Emojis:", emojis)
            if self.options.get('count_emoji_frequency', True):
                emoji_frequency = self.count_emoji_frequency(text)
                print("Emoji Frequency:", emoji_frequency)
            if self.options.get('remove_emojis', True):
                text = self.remove_emojis(text)

            return text
        except Exception as e:
            logging.error(f"Error during text cleaning: {str(e)}")
            raise

    def clean_reserved_words(self, text):
        # Remove reserved words (RT, FAV, etc.)
        cleaned_text = re.sub(r'\b(?:RT|FAV)\b', '', text)
        return cleaned_text

    def clean_urls(self, text):
        # Remove URLs
        cleaned_text = re.sub(r'http\S+|www\S+|https\S+', '', text)
        return cleaned_text

    def clean_hashtags(self, text):
        # Remove hashtags
        cleaned_text = re.sub(r'#\w+', '', text)
        return cleaned_text

    def clean_mentions(self, text):
        # Remove mentions
        cleaned_text = re.sub(r'@\w+', '', text)
        return cleaned_text

    def clean_emojis(self, text):
        # Remove emojis
        cleaned_text = ''.join(c for c in text if c not in emoji.EMOJI_DATA)
        return cleaned_text

    def clean_smileys(self, text):
        # Remove smileys
        cleaned_text = re.sub(r'[:;]-[)D]', '', text)
        return cleaned_text

    def remove_punctuation(self, text):
        # Remove punctuation
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        return cleaned_text

    def remove_numbers(self, text):
        # Remove numbers
        cleaned_text = re.sub(r'\d+', '', text)
        return cleaned_text

    def remove_special_characters(self, text):
        # Remove special characters
        cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', text)
        return cleaned_text

    def convert_to_lowercase(self, text):
        # Convert to lowercase
        return text.lower()

    def remove_extra_whitespace(self, text):
        # Replace multiple consecutive whitespaces with a single whitespace
        cleaned_text = re.sub(r'\s+', ' ', text)
        return cleaned_text.strip()
    def count_word_frequency(self, text):
        try:
            # Count word frequency
            word_tokens = word_tokenize(text)
            word_frequency = Counter(word_tokens)
            return word_frequency
        except Exception as e:
            logging.error(f"Error during word frequency counting: {str(e)}")
            raise
    def extract_emojis(self, text):
        # Extract emojis from the text
        return [c for c in text if c in emoji.EMOJI_DATA]

    def count_emoji_frequency(self, text):
        # Count emoji frequency
        emojis = self.extract_emojis(text)
        return Counter(emojis)

    def remove_emojis(self, text):
        # Remove emojis from the text
        return ''.join(c for c in text if c not in emoji.EMOJI_DATA)

    def remove_stopwords(self, text):
        try:
            # Remove stopwords
            word_tokens = word_tokenize(text)
            filtered_text = [word for word in word_tokens if word.lower() not in self.stop_words]
            return ' '.join(filtered_text)
        except Exception as e:
            logging.error(f"Error during stopwords removal: {str(e)}")
            raise

    def lemmatize_text(self, text):
        try:
            # Lemmatization
            lemmatized_text = ' '.join([self.lemmatizer.lemmatize(word) for word in word_tokenize(text)])
            return lemmatized_text
        except Exception as e:
            logging.error(f"Error during lemmatization: {str(e)}")
            raise

    def embed_emojis(self, text):
        try:
            # Convert emojis to text representation
            embedded_text = emoji.demojize(text)
            return embedded_text
        except Exception as e:
            logging.error(f"Error during emoji embedding: {str(e)}")
            raise

    def tokenize(self, text):
        try:
            # Tokenize
            tokenized_text = word_tokenize(text)
            return tokenized_text
        except Exception as e:
            logging.error(f"Error during tokenization: {str(e)}")
            raise

    def parse(self, text):
        try:
            # Parse URLs, hashtags, mentions, reserved words, emojis, and smileys
            urls = re.findall(r'http\S+|www\S+|https\S+', text)
            hashtags = re.findall(r'#\w+', text)
            mentions = re.findall(r'@\w+', text)
            reserved_words = re.findall(r'\b(?:RT|FAV)\b', text)
            emojis = [c for c in text if c in emoji.EMOJI_DATA]
            smileys = re.findall(r'[:;]-[)D]', text)

            parsed_tweet = ParseResult(text, urls=urls, hashtags=hashtags, mentions=mentions,
                                       reserved_words=reserved_words, emojis=emojis, smileys=smileys)
            return parsed_tweet
        except Exception as e:
            logging.error(f"Error during parsing: {str(e)}")
            raise

    def clean_file(self, file_name, options=None):
        try:
            with open(file_name, 'r') as file:
                data = file.read()

            cleaned_text = self.clean_text(data)

            output_file_name = f"cleaned_{file_name}"
            with open(output_file_name, 'w') as output_file:
                output_file.write(cleaned_text)

            print(f"Saved the cleaned text to: {output_file_name}")
        except Exception as e:
            logging.error(f"Error during file processing: {str(e)}")
            raise
