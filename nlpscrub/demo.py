# Import the TextProcessor class
from nlpscrub.TextProcessor import TextProcessor
# Create an instance of TextProcessor
processor = TextProcessor()

# Sample text
sample_text = "RT @user: Preprocessor is #awesome 👍 https://github.com/s/preprocessor #NLP 123 !@#$"

# 1. Clean the text
cleaned_text_result = processor.clean_text(sample_text)

# Display the cleaned text and parsed elements
print("Cleaned Text:", cleaned_text_result)

# 2. Customize options and reclean the text
processor.set_options(remove_punctuation=False, remove_numbers=False)
result_custom = processor.clean_text(sample_text)

# Display the results with custom options
print("\nCleaned Text (Custom Options):", result_custom)

# 3. Count word frequency
word_frequency_result = processor.count_word_frequency(sample_text)
print("\nWord Frequency:", word_frequency_result)

# 4. Extract emojis
extracted_emojis_result = processor.extract_emojis(sample_text)
print("\nExtracted Emojis:", extracted_emojis_result)

# 5. Count emoji frequency
emoji_frequency_result = processor.count_emoji_frequency(sample_text)
print("\nEmoji Frequency:", emoji_frequency_result)

# 6. Remove emojis
text_without_emojis = processor.remove_emojis(sample_text)
print("\nText without Emojis:", text_without_emojis)

# 7. Remove stopwords
text_without_stopwords = processor.remove_stopwords(sample_text)
print("\nText without Stopwords:", text_without_stopwords)

# 8. Lemmatize text
lemmatized_text = processor.lemmatize_text(sample_text)
print("\nLemmatized Text:", lemmatized_text)

# 9. Embed emojis
embedded_emojis_text = processor.embed_emojis(sample_text)
print("\nEmbedded Emojis Text:", embedded_emojis_text)

# 10. Tokenize text
tokenized_text = processor.tokenize(sample_text)
print("\nTokenized Text:", tokenized_text)

# 11. Parse text
parsed_result = processor.parse(sample_text)
print("\nParsed Result:")
print("URLs:", parsed_result.urls)
print("Hashtags:", parsed_result.hashtags)
print("Mentions:", parsed_result.mentions)
print("Reserved Words:", parsed_result.reserved_words)
print("Emojis:", parsed_result.emojis)
print("Smileys:", parsed_result.smileys)

# 12. Clean a text file
file_name = "sample.txt"
processor.clean_file(file_name)

# 13. Set custom options and clean a text file
processor.set_options(remove_punctuation=True, remove_numbers=True)
processor.clean_file(file_name)
