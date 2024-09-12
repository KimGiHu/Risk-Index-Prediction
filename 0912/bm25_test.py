import spacy
import en_core_web_lg

nlp = spacy.load("en_core_web_lg")
nlp = en_core_web_lg.load()
doc = nlp("\
    week rate mortgage matching week \
    rate rate month recovery improvement economy \
    malaise combination mortgage rate labor market \
    consumer confidence housing market improvement sale \
    summer fall week week time rate mortgage week rate \
    rate week image highlight week change teen angst product \
    person circumstance gender race class era content generation \
    people explanation majority reader male hand conversation \
    student writing class network people coming age perspective \
    woman form rebellion school district presence curriculum adult \
    girl kid colour student school teacher suspicion identity reader \
    shift culture malaise resonant concept isolation adult core anathema \
    kid age culture crush projection era teen bootstrap idea couple day \
    contact adult life kid leash parent child geolocation device freedom \
    heaping neglect people adult classmate brother morning shooter drill \
    homeroom lifetime grownup melancholia comparison kid stage life time age education kid school stomping ground ennui people love college morphine drip nostalgia departure youth search friend appeal sensitivity crush projection guy life friend literature writing book time brand portrait character syllable reading bit kid love book adult reader craftsmanship proposal reader time life brat money opportunity stand teenager individual injusticeThis is a sentence.")

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
""" 테스트 결과 : 토큰을 품사단위로 분리하는 것이 하나의 문자로 분리하기에 추가적인 전처리 혹은 옵션을 주는 기능에 대해서 살펴볼 필요가 있다."""
exit()
