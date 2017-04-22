import os

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
processed = os.path.join(parent, 'corpus', 'processed')
unprocessed = os.path.join(parent, 'corpus', 'unprocessed')
blacklist = set(['.DS_Store'])

def get_path(*args):
    return os.path.join(*[str(arg) for arg in args])

def get_corpus_analytics(corpus):
    corpus = get_path(parent, 'corpus', corpus)
    for folder in os.listdir(corpus):
        folder_sum = 0
        if folder not in blacklist:
            path = get_path(corpus, folder)
            for item in os.listdir(path):
                path = get_path(corpus, folder, item)
                f = open(path, 'r', encoding='ISO-8859-1').read().strip().split('\n')
                folder_sum += len(f)
            print(folder, folder_sum)

get_corpus_analytics('processed')
get_corpus_analytics('unprocessed')
