# 🔍 Vector Space Search Engine

This project implements a basic vector space search engine in Python, leveraging **cosine similarity** to find relevant documents based on a given query. It's a foundational example demonstrating how text can be represented as vectors and compared for semantic similarity.

---

## ✨ Features

* **Document Indexing:** Easily add multiple documents to the search engine.
* **Vector Representation:** Converts documents into numerical vectors (concordances).
* **Cosine Similarity:** Calculates the similarity between query vectors and document vectors.
* **Relevance Ranking:** Ranks search results by relevance score (highest similarity first).
* **Interactive CLI:** A simple command-line interface to interact with the search engine, add documents, and perform searches.

---

## 🛠️ How It Works (Core Concepts)

The search engine operates on the principle of the **Vector Space Model**, where documents and queries are represented as vectors in a multi-dimensional space.

* **Concordance (Term Frequency):** The `concordance` function creates a dictionary for each document (and query) where keys are unique words and values are their frequencies. This dictionary serves as the raw vector representation.
* **Magnitude:** The `magnitude` method calculates the "length" of a vector using the Euclidean norm. This is essential for normalizing vectors before calculating similarity.
* **Relation (Cosine Similarity):** The `relation` method computes the **cosine similarity** between two vectors. Cosine similarity measures the cosine of the angle between two non-zero vectors. A score closer to 1 indicates higher similarity, while a score closer to 0 indicates lower similarity.

    $CosineSimilarity(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$

    Where:
    * $A \cdot B$ is the dot product of vectors A and B.
    * $\|A\|$ and $\|B\|$ are the magnitudes (Euclidean norms) of vectors A and B, respectively.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.6+

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/vector-search-engine.git](https://github.com/your-username/vector-search-engine.git)
    cd vector-search-engine
    ```
    (Replace `your-username/vector-search-engine.git` with the actual path to your repository if you host it elsewhere.)
2.  **No external dependencies:** This project uses only standard Python libraries.

### Running the Search Engine

Execute the main script from your terminal:

```bash
python main.py
```
(Assuming your provided code is saved as `main.py`. If it's saved as `search_engine.py`, use `python search_engine.py`.)

### Interactive Usage

Once running, you'll see a prompt:

```
Vector Space Search Engine Prototype
======================================================================
Interactive Search Engine
Enter search queries to find relevant documents.
Type 'quit', 'exit', or press Ctrl+C to stop.
Type 'stats' to see engine statistics.
Type 'docs' to list all document IDs.

Loaded 7 documents.

Search>
```

You can then:
* **Enter a query:** Type your search query (e.g., `performance issues`) and press Enter.
* **View statistics:** Type `stats`.
* **List document IDs:** Type `docs`.
* **Exit:** Type `quit`, `exit`, or press `Ctrl+C`.

---

## 📈 Next Steps for Enhancement: Text Preprocessing

The current implementation provides a solid foundation, but the search experience can be significantly optimized by incorporating robust text preprocessing techniques. This will improve the accuracy and relevance of search results by standardizing text and reducing noise.

Consider adding a dedicated preprocessing step within the `add_document` method, or before the `concordance` function, that includes:

1.  **Punctuation Removal:**
    * **Problem:** Punctuation marks (e.g., `.`, `,`, `!`, `?`) can be treated as part of words, leading to separate entries in the concordance for "word" and "word.".
    * **Solution:** Remove all punctuation from the text. Python's `string.punctuation` module can be helpful.

2.  **Stop Word Removal:**
    * **Problem:** Common words like "the", "a", "is", "and" (known as **stop words**) appear frequently but carry little semantic weight. They can skew relevance scores.
    * **Solution:** Create a list of common stop words and remove them from documents and queries. Libraries like `nltk` provide comprehensive stop word lists.

3.  **Stemming or Lemmatization:**
    * **Problem:** Different forms of a word (e.g., "run," "running," "runs," "ran") are treated as unique words, even though they share the same root meaning.
    * **Solution:**
        * **Stemming:** Reduces words to their root form (e.g., "running" $\rightarrow$ "run"). This is a heuristic process and might not always result in a valid word (e.g., `universal` $\rightarrow$ `univers`). Popular stemmers include Porter Stemmer and Snowball Stemmer.
        * **Lemmatization:** Reduces words to their base or dictionary form (**lemma**), considering their part of speech. This is more linguistically accurate than stemming (e.g., `better` $\rightarrow$ `good`).
        * Libraries like `nltk` or `spaCy` offer robust implementations for both.

4.  **Tokenization Refinement:**
    * **Problem:** The current `document.split()` is a basic tokenization that splits only by whitespace. This might miss cases like hyphenated words or contractions, or not handle complex sentence structures.
    * **Solution:** Use more advanced tokenizers (e.g., `word_tokenize` from `nltk`) that can handle various linguistic nuances and correctly separate words.

### Example of Preprocessing Integration

You could create a new function `preprocess_text(text)` that chains these operations and call it before creating the concordance. Here's a conceptual example using `nltk` (you'd need to `pip install nltk` and download necessary data like `stopwords` and `wordnet` first):

```python
import re
import string
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer, WordNetLemmatizer

# Run these once if using NLTK:
# nltk.download('stopwords')
# nltk.download('wordnet')

def preprocess_text(text: str) -> str:
    # 1. Lowercasing (already done in your code, but good to ensure here)
    text = text.lower()

    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 3. Remove numbers (optional, depending on whether numbers are relevant to your search)
    # text = re.sub(r'\d+', '', text)

    # 4. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # 5. Tokenization (more robust than simple .split())
    # tokens = nltk.word_tokenize(text)

    # 6. Stop word removal (uncomment if using NLTK stopwords)
    # stop_words = set(stopwords.words('english'))
    # filtered_tokens = [word for word in tokens if word not in stop_words]

    # 7. Stemming or Lemmatization (uncomment if using NLTK)
    # stemmer = PorterStemmer() # For stemming
    # lemmatizer = WordNetLemmatizer() # For lemmatization
    # processed_tokens = [stemmer.stem(word) for word in filtered_tokens] # Example with stemming
    # processed_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens] # Example with lemmatization

    # If using nltk, you'd join the processed tokens:
    # return ' '.join(processed_tokens)

    # If not using nltk, return the text after basic cleaning:
    return text

# Then, in your VectorSearchEngine's add_document method:
# self.index[doc_id] = self.vector_compare.concordance(preprocess_text(content))
# And also for the query:
# query_concordance = self.vector_compare.concordance(preprocess_text(query))
```

Implementing these steps will significantly enhance the search engine's ability to find relevant documents by dealing with variations in text and focusing on meaningful terms.
