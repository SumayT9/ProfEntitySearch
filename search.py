import data_collector
from nltk import sent_tokenize
from sentence_transformers import SentenceTransformer, util


def generate_keyphrases(query, model):
    urls = data_collector.search_google(query, 5)
    text = ""
    for url in urls:
        try:

            newText = data_collector.extract_data_from_url(url).strip().replace("\t", "")
            text += newText
            print(url)
        except:
            continue

    sentences = sent_tokenize(text)
    out = find_sentences(query, sentences ,model)
    return out[:3]



def find_sentences(query, text, model):
    query_emb = model.encode(query)
    doc_emb = model.encode(text)
    scores = util.dot_score(query_emb, doc_emb)[0].cpu().tolist()
    doc_score_pairs = list(zip(text, scores))
    doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
    out = []
    for doc, score in doc_score_pairs:
        doc = doc.strip()
        if doc not in out and len(doc) > 5 and doc != "B.S.":
            out.append(doc)
    return out[:3]

def generate_page(person):
    queries = {
        "Awards": "What awards has " + person + " won?", 
       "Research Interests" : person + " research areas", 
       "Achievements" : person + " achievements", 
       "Education" : person + " education background",
       "Work Experience" : person + " work experience",
       "Research Activity" : person + " research activity"
    }
    """
    Models used:
    'sentence-transformers/msmarco-distilbert-base-tas-b'
    'sentence-transformers/multi-qa-mpnet-base-dot-v1
    'sentence-transformers/all-distilroberta-v1'
    """
    model=SentenceTransformer('sentence-transformers/multi-qa-mpnet-base-dot-v1')
    page = ""
    for topic, query in queries.items():
        page += topic + " \n" + (" ").join(generate_keyphrases(query, model)) + "\n\n"
    return page



txt = generate_page("Hari Sundaram")
print()
print()
print(txt)

"""
Test cases: Hari Sundaram-not amazing not terrible
            Geoffrey Challen - mid
            Benjamin Cosman - bad
            Joe Biden - amazing

"""