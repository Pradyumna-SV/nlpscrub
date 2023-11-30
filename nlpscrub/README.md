## Installation

pip install nlpscrub


### `text_processor` Class

The `text_processor` class provides various functions for cleaning, tokenizing, and parsing text data.

#### Initialization:

```python
from NLPScrub import text_processor

# Create an instance of TextProcessor
processor = text_processor()
```

#### Options Handling:

The `set_options` method allows you to configure various options for text processing:

```python
processor.set_options(
    clean_reserved_words=True,
    clean_urls=True,
    clean_hashtags=True,
    clean_mentions=True,
    clean_emojis=True,
    clean_smileys=True,
    remove_punctuation=True,
    remove_numbers=True,
    remove_special_characters=True,
    convert_to_lowercase=True,
    remove_extra_whitespace=True,
    extract_emojis=True,
    count_emoji_frequency=True,
    remove_emojis=True,
)
```

### Functions:

#### `clean_text(text)`

Cleans the input text based on the specified options.

- **Parameters:**
  - `text` (str): The input text to be cleaned.

- **Returns:**
  - `ParseResult`: An object containing the cleaned text and parsed elements.

#### `clean_reserved_words(text)`

Removes reserved words (e.g., RT, FAV) from the text.

#### `clean_urls(text)`

Removes URLs from the text.

#### `clean_hashtags(text)`

Removes hashtags from the text.

#### `clean_mentions(text)`

Removes mentions (e.g., @user) from the text.

#### `clean_emojis(text)`

Removes emojis from the text.

#### `clean_smileys(text)`

Removes smileys (e.g., :-)) from the text.

#### `remove_punctuation(text)`

Removes punctuation from the text.

#### `remove_numbers(text)`

Removes numbers from the text.

#### `remove_special_characters(text)`

Removes special characters from the text.

#### `convert_to_lowercase(text)`

Converts the text to lowercase.

#### `remove_extra_whitespace(text)`

Replaces multiple consecutive whitespaces with a single whitespace.

#### `extract_emojis(text)`

Extracts emojis from the text.

- **Parameters:**
  - `text` (str): The input text.

- **Returns:**
  - `List[str]`: A list of extracted emojis.

#### `count_emoji_frequency(text)`

Counts the frequency of each emoji in the text.

- **Parameters:**
  - `text` (str): The input text.

- **Returns:**
  - `Counter`: A Counter object with emoji frequencies.

#### `remove_emojis(text)`

Removes emojis from the text.

#### `remove_stopwords(text)`

Removes stopwords from the text using NLTK's English stopword list.

- **Parameters:**
  - `text` (str): The input text.

- **Returns:**
  - `str`: The text with stopwords removed.

#### `lemmatize_text(text)`

Lemmatizes words in the text using NLTK's WordNet lemmatizer.

- **Parameters:**
  - `text` (str): The input text.

- **Returns:**
  - `str`: The lemmatized text.

#### `embed_emojis(text)`

Converts emojis in the text to text representations using the `emoji` library.

- **Parameters:**
  - `text` (str): The input text.

- **Returns:**
  - `str`: The text with embedded emojis.

#### `tokenize(text)`

Tokenizes the text into a list of words.

- **Parameters:**
  - `text` (str): The input text.

- **Returns:**
  - `List[str]`: A list of tokenized words.

#### `parse(text)`

Parses the text to extract URLs, hashtags, mentions, reserved words, emojis, and smileys.

- **Parameters:**
  - `text` (str): The input text.

- **Returns:**
  - `ParseResult`: An object containing parsed elements.

#### `clean_file(file_name, options=None)`

Cleans the text from a file based on specified options.

- **Parameters:**
  - `file_name` (str): The name of the input file.
  - `options` (dict, optional): A dictionary of options to override default options.

- **Returns:**
  - None

### Demo Script:

For more examples, see the [demo script](demo.py) provided in this repository.

### License:

This project is licensed under the MIT License 