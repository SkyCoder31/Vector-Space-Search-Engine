#!/usr/bin/env python3

import math
import re
import string
from typing import Dict, List, Tuple, Any


def concordance(document: str) -> Dict[str, int]:
    """
    Create a concordance (word frequency dictionary) from a document.
    """
    if not isinstance(document, str):
        raise ValueError('Supplied argument should be of type string')
    
    con = {}
    for word in document.split():
        if word in con:
            con[word] += 1
        else:
            con[word] = 1
    return con


class VectorCompare:
    """
    A class to perform vector space comparisons between documents using cosine similarity.
    """
    
    def magnitude(self, concordance: Dict[str, int]) -> float:
        """
        Calculate the magnitude (length) of a vector.

        """
        if not isinstance(concordance, dict):
            raise ValueError('Supplied argument should be of type dict')
        
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)
    
    def relation(self, concordance1: Dict[str, int], concordance2: Dict[str, int]) -> float:
        """
        Calculate cosine similarity between two vectors.
        
        """
        if not isinstance(concordance1, dict):
            raise ValueError('Supplied argument 1 should be of type dict')
        if not isinstance(concordance2, dict):
            raise ValueError('Supplied argument 2 should be of type dict')
        
        # Calculating the dot product
        dot_product = 0
        for word, count in concordance1.items():
            if word in concordance2:
                dot_product += count * concordance2[word]
        
        # Calculate the magnitudes
        magnitude1 = self.magnitude(concordance1)
        magnitude2 = self.magnitude(concordance2)
        
        # Avoiding division by zero
        if magnitude1 * magnitude2 != 0:
            return dot_product / (magnitude1 * magnitude2)
        else:
            return 0
    
    def concordance(self, document: str) -> Dict[str, int]:
        """
        Create concordance(included in class for convenience.)
        """
        return concordance(document)


class VectorSearchEngine:
    """
    A complete vector space search engine implementation.
    """
    
    def __init__(self): #initializing the search engine
        self.vector_compare = VectorCompare()
        self.documents = {}
        self.index = {}
        
    def add_document(self, doc_id: Any, content: str) -> None:
        """
        Adding a document to the search engine.
       
        """
        # Storing the original document
        self.documents[doc_id] = content
        
        # Creating and storing the concordance (transformed to lowercase)
        self.index[doc_id] = self.vector_compare.concordance(content.lower())
    
    def add_documents(self, documents_dict: Dict[Any, str]) -> None:
        """
        Adding multiple documents at once.
       
        """
        for doc_id, content in documents_dict.items():
            self.add_document(doc_id, content)
    
    def search(self, query: str, max_results: int = 10) -> List[Tuple[float, Any, str]]:
        """
        Searching for the documents matching the query.
        """
        if not query.strip():
            return []

        # Creating the query concordance
        query_concordance = self.vector_compare.concordance(query.lower())

        # Calculating relevance scores
        matches = []
        for doc_id in self.index:
            score = self.vector_compare.relation(query_concordance, self.index[doc_id])
            if score > 0:  # Only including documents with relevance
                snippet = self.documents[doc_id][:150] + "..." if len(self.documents[doc_id]) > 150 else self.documents[doc_id]
                matches.append((score, doc_id, snippet))

        # Sorting by relevance score (highest first)
        matches.sort(reverse=True, key=lambda x: x[0])
        
        return matches[:max_results]
    
    def get_document_count(self) -> int:
        return len(self.documents)
    
    def get_vocabulary_size(self) -> int:
        vocab = set()
        for concordance in self.index.values():
            vocab.update(concordance.keys())
        return len(vocab)


def main():
    #Entry Point for the search engine prototype
    print("Vector Space Search Engine Prototype")
    print("=" * 70)
    print("Interactive Search Engine")
    print("Enter search queries to find relevant documents.")
    print("Type 'quit', 'exit', or press Ctrl+C to stop.")
    print("Type 'stats' to see engine statistics.")
    print("Type 'docs' to list all document IDs.")
    
    # Initialize with the enhanced engine
    search_engine = VectorSearchEngine()
    
    # Add the original article documents
    original_docs = {
        'performance': '''At Scale You Will Hit Every Performance Issue I used to think I knew a bit about performance scalability and how to keep things trucking when you hit large amounts of data Truth is I know diddly squat on the subject since the most I have ever done is read about how its done To understand how I came about realising this you need some background''',
        'stallman': '''Richard Stallman to visit Australia Im not usually one to promote events and the like unless I feel there is a genuine benefit to be had by attending but this is one stands out Richard M Stallman the guru of Free Software is coming Down Under to hold a talk You can read about him here Open Source Celebrity to visit Australia''',
        'mysql': '''MySQL Backups Done Easily One thing that comes up a lot on sites like Stackoverflow and the like is how to backup MySQL databases The first answer is usually use mysqldump This is all fine and good till you start to want to dump multiple databases You can do this all in one like using the all databases option however this makes restoring a single database an issue since you have to parse out the parts you want which can be a pain''',
        'captcha': '''Why You Shouldnt roll your own CAPTCHA At a TechEd I attended a few years ago I was watching a presentation about Security presented by Rocky Heckman read his blog its quite good In it he was talking about security algorithms The part that really stuck with me went like this''',
        'development': '''The Great Benefit of Test Driven Development Nobody Talks About The feeling of productivity because you are writing lots of code Think about that for a moment Ask any developer who wants to develop why they became a developer One of the first things that comes up is I enjoy writing code This is one of the things that I personally enjoy doing Writing code any code especially when its solving my current problem makes me feel productive It makes me feel like Im getting somewhere Its empowering''',
        'git': '''Setting up GIT to use a Subversion SVN style workflow Moving from Subversion SVN to GIT can be a little confusing at first I think the biggest thing I noticed was that GIT doesnt have a specific workflow you have to pick your own Personally I wanted to stick to my Subversion like work-flow with a central server which all my machines would pull and push too Since it took a while to set up I thought I would throw up a blog post on how to do it''',
        'captcha_numbers': '''Why CAPTCHA Never Use Numbers 0 1 5 7 Interestingly this sort of question pops up a lot in my referring search term stats Why CAPTCHAs never use the numbers 0 1 5 7 Its a relativity simple question with a reasonably simple answer Its because each of the above numbers are easy to confuse with a letter See the below'''
    }
    
    search_engine.add_documents(original_docs)
    print(f"\nLoaded {search_engine.get_document_count()} documents.")
    
    try:
        while True:
            query = input("\nSearch> ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            elif query.lower() == 'stats':
                print(f"\nEngine Statistics:")
                print(f"  Documents: {search_engine.get_document_count()}")
                print(f"  Vocabulary: {search_engine.get_vocabulary_size()} unique words")
                continue
            elif query.lower() == 'docs':
                print(f"\nDocument IDs: {list(search_engine.documents.keys())}")
                continue
            elif not query:
                continue
                
            results = search_engine.search(query, max_results=5)
            
            if results:
                print(f"\nFound {len(results)} results for '{query}':")
                print("-" * 50)
                for i, (score, doc_id, snippet) in enumerate(results, 1):
                    print(f"{i}. Score: {score:.4f} | Document: {doc_id}")
                    print(f"   {snippet}")
                    print()
            else:
                print(f"No results found for '{query}'")
                
    except KeyboardInterrupt:
        print("\n\nSearch session ended.")


if __name__ == "__main__":
    main()