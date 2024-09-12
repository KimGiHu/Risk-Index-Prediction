import spacy
import en_core_web_lg

nlp = spacy.load("en_core_web_lg")
nlp = en_core_web_lg.load()
doc = nlp("This is a sentence.")
for token in doc :
    print(token.text, token.pos_, token.dep_)

def tokenizer(text):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)
    words = [token.lemma_ for token in doc if token.pos_ in ['NOUN'] if not token.is_stop and not token.is_punct and not token.is_oov and '+' not in token.lemma_]
    return words

print(tokenizer(doc))

tokenized_corpus = tokenizer(doc)

from rank_bm25 import BM25Okapi

bm25_words = BM25Okapi(tokenized_corpus)

# 인덱싱된 결과들을 살펴보면 BM25 점수 계산에 필요한 항들이 들어있는 것을 확인할 수 있다.
# doc_len : 파생된 문서의 길이
print(bm25_words.doc_len)

# doc_freqs : 문서에 있는 각각의 토큰 빈도(각 문서내에서 딕셔너리 형태로 저장)
print(bm25_words.doc_freqs)

# 그렇다면 뉴스 기사들을 전처리한 full text들에서 명사단위로 끊어서 토큰빈도를 저장할 수 있을까?

exit()
# print([(w.text, w.pos_) for w in doc]) # 해당 토큰의 단어와 종류를 알려줌.

# BM25 알고리즘 기반의 tokenized_corpus 분석
from rank_bm25 import BM25Okapi

words =[(w.lemma_) for w in doc]

bm25_words = BM25Okapi("This is a sentence.")

# 인덱싱된 결과들을 살펴보면 BM25 점수 계산에 필요한 항들이 들어있는 것을 확인할 수 있다.
# doc_len : 파생된 문서의 길이
print(bm25_words.doc_len)

# doc_freqs : 문서에 있는 각각의 토큰 빈도(각 문서내에서 딕셔너리 형태로 저장)
print(bm25_words.doc_freqs)

# 그렇다면 뉴스 기사들을 전처리한 full text들에서 명사단위로 끊어서 토큰빈도를 저장할 수 있을까?
