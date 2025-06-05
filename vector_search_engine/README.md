:

🔍 Vector Space Search Engine (Python)
A simple and interactive Vector Space Search Engine built using Python that demonstrates core principles of Information Retrieval. It uses cosine similarity to compare document vectors and ranks search results based on relevance.

📦 Features
Adds documents and stores a concordance (word frequency map) for each

Supports searching with a user query using cosine similarity

Interactive CLI for querying, checking engine stats, and document listing

Clean modular code using object-oriented design

📁 Project Structure
bash
Copy
Edit
vector_search_engine/
│
├── engine.py         # Main implementation of vector search
├── README.md                # This file
🚀 Getting Started
✅ Requirements
Python 3.6 or higher

🛠 Installation & Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/vector-search-engine.git
cd vector-search-engine
Run the search engine:

bash
Copy
Edit
python search_engine.py
🧠 How It Works
Concordance Creation
Each document is processed to count occurrences of each word (frequency map).

Vector Representation
The frequency maps are treated as high-dimensional vectors.

Cosine Similarity
The similarity between the query and each document is computed using:

cosine_similarity
=
𝐴
⃗
⋅
𝐵
⃗
∣
∣
𝐴
∣
∣
×
∣
∣
𝐵
∣
∣
cosine_similarity= 
∣∣A∣∣×∣∣B∣∣
A
 ⋅ 
B
 
​
 
Ranking
Results are ranked by relevance score (cosine similarity) and returned to the user.

🕹️ How to Use
Once you start the engine, you’ll be prompted in an interactive CLI.

🔧 Available Commands:
search term → returns top 5 relevant documents

stats → shows number of documents and vocabulary size

docs → lists all available document IDs

exit / quit → exits the CLI

📈 Example
text
Copy
Edit
Search> captcha

Found 3 results for 'captcha':
--------------------------------------------------
1. Score: 0.6542 | Document: captcha
   Why You Shouldnt roll your own CAPTCHA At a TechEd...

2. Score: 0.4721 | Document: captcha_numbers
   Why CAPTCHA Never Use Numbers 0 1 5 7 Interestingly...

3. Score: 0.0845 | Document: git
   Setting up GIT to use a Subversion SVN style workflow...
✅ Current Limitations
No text preprocessing (e.g., stopword removal, punctuation stripping)

No stemming or lemmatization

Case-sensitive matching is only partially handled (.lower() applied)

No support for TF-IDF weighting (uses raw frequency counts)

🔄 Next Steps: Enhancements with Text Preprocessing
To significantly improve the quality of the search results:

1. Text Preprocessing Pipeline
Enhance concordance() by adding:

Lowercasing

Removing punctuation

Token normalization (remove numbers, symbols)

Stopword removal (nltk.corpus.stopwords)

Optional: Stemming or Lemmatization (nltk.stem or spaCy)

python
Copy
Edit
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess(text):
    # Lowercase, remove punctuation, split words
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    words = text.split()
    
    # Remove stopwords and apply stemming
    return [stemmer.stem(word) for word in words if word not in stop_words]
2. TF-IDF Scoring
Use TfidfVectorizer from sklearn instead of raw word counts for smarter ranking.

3. Web Interface
Use Flask or FastAPI to serve the search engine via a REST API or frontend.

4. Persistence
Allow saving/loading documents and index using pickle, sqlite, or json.

