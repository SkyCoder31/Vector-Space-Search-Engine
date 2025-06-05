🔍 Vector Space Search Engine
This project implements a basic vector space search engine in Python, leveraging cosine similarity to find relevant documents based on a given query. It's a foundational example demonstrating how text can be represented as vectors and compared for semantic similarity.
✨ Features
Document Indexing: Easily add multiple documents to the search engine.
Vector Representation: Converts documents into numerical vectors (concordances).
Cosine Similarity: Calculates the similarity between query vectors and document vectors.
Relevance Ranking: Ranks search results by relevance score (highest similarity first).
Interactive CLI: A simple command-line interface to interact with the search engine, add documents, and perform searches.
🛠️ How It Works (Core Concepts)
The search engine operates on the principle of the Vector Space Model, where documents and queries are represented as vectors in a multi-dimensional space.
Concordance (Term Frequency): The concordance function creates a dictionary for each document (and query) where keys are unique words and values are their frequencies. This dictionary serves as the raw vector representation.
Magnitude: The magnitude method calculates the "length" of a vector using the Euclidean norm. This is essential for normalizing vectors before calculating similarity.
Relation (Cosine Similarity): The relation method computes the cosine similarity between two vectors. Cosine similarity measures the cosine of the angle between two non-zero vectors. A score closer to 1 indicates higher similarity, while a score closer to 0 indicates lower similarity.
CosineSimilarity(A,B)=∣A∣∣B∣A⋅B​
Where:
A⋅B is the dot product of vectors A and B.
∣A∣ and ∣B∣ are the magnitudes (Euclidean norms) of vectors A and B, respectively.
🚀 Getting Started
Prerequisites
Python 3.6+
Installation
Clone the repository:
git clone https://github.com/your-username/vector-search-engine.git
cd vector-search-engine


No external dependencies: This project uses only standard Python libraries.
Running the Search Engine
Execute the main script from your terminal:
python your_script_name.py


(Replace your_script_name.py with the actual filename of the provided code, e.g., search_engine.py)
Interactive Usage
Once running, you'll see a prompt:
Vector Space Search Engine Prototype
======================================================================
Interactive Search Engine
Enter search queries to find relevant documents.
Type 'quit', 'exit', or press Ctrl+C to stop.
Type 'stats' to see engine statistics.
Type 'docs' to list all document IDs.

Loaded 7 documents.

Search>


You can then:
Enter a query: Type your search query (e.g., performance issues) and press Enter.
View statistics: Type stats.
List document IDs: Type docs.
Exit: Type quit, exit, or press Ctrl+C.
📈 Next Steps for Enhancement: Text Preprocessing
The current implementation provides a solid foundation, but the search experience can be significantly optimized by incorporating robust text preprocessing techniques. This will improve the accuracy and relevance of search results by standardizing text and reducing noise.
Consider adding a dedicated preprocessing step within the add_document method, or before the concordance function, that includes:
Punctuation Removal:
Problem: Punctuation marks (e.g., ., ,, !, ?) can be treated as part of words, leading to separate entries in the concordance for "word" and "word.".
Solution: Remove all punctuation from the text. Python's string.punctuation module can be helpful.
Stop Word Removal:
Problem: Common words like "the", "a", "is", "and" (known as stop words) appear frequently but carry little semantic weight. They can skew relevance scores.
Solution: Create a list of common stop words and remove them from documents and queries. Libraries like nltk provide comprehensive stop word lists.
Stemming or Lemmatization:
Problem: Different forms of a word (e.g., "run," "running," "runs," "ran") are treated as unique words, even though they share the same root meaning.
Solution:
Stemming: Reduces words to their root form (e.g., "running" → "run"). This is a heuristic process and might not always result in a valid word. (e.g. universal → univers).
Lemmatization: Reduces words to their base or dictionary form (lemma), considering their part of speech. This is more linguistically accurate than stemming. (e.g. better → good).
Libraries like nltk or spaCy offer robust implementations for both.
Tokenization Refinement:
Problem: The current document.split() is a basic tokenization that splits only by whitespace. This might miss cases like hyphenated words or contractions.
Solution: Use more advanced tokenizers (e.g., word_tokenize from nltk) that can handle various linguistic nuances and correctly separate words.
Example of Preprocessing Integration
You could create a new function preprocess_text(text) that chains these operations and call it before creating the concordance:
import re
import string
# from nltk.corpus import stopwords # Uncomment if using NLTK for stopwords
# from nltk.stem import PorterStemmer, WordNetLemmatizer # Uncomment if using NLTK for stemming/lemmatization
# import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')

def preprocess_text(text: str) -> str:
    # 1. Lowercasing (already done in your code, but good to include here for completeness)
    text = text.lower()

    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Remove numbers (optional, depending on use case)
    text = re.sub(r'\d+', '', text)

    # 4. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # 5. Stop word removal (requires nltk)
    # stop_words = set(stopwords.words('english'))
    # tokens = text.split()
    # filtered_tokens = [word for word in tokens if word not in stop_words]
    # text = ' '.join(filtered_tokens)

    # 6. Stemming or Lemmatization (requires nltk)
    # stemmer = PorterStemmer()
    # lemmatizer = WordNetLemmatizer()
    # tokens = text.split()
    # stemmed_tokens = [stemmer.stem(word) for word in tokens] # For stemming
    # lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens] # For lemmatization
    # text = ' '.join(stemmed_tokens) # Or lemmatized_tokens

    return text

# Then, in your add_document method:
# self.index[doc_id] = self.vector_compare.concordance(preprocess_text(content))


Implementing these steps will significantly enhance the search engine's ability to find relevant documents by dealing with variations in text and focusing on meaningful terms.
