import pickle

NAME_ARQ = 'cache.pickle'
READ = 'rb'
WRITE = 'wb'

def import_disc(cache) -> bool:
    pickle.dump(cache,open(NAME_ARQ,WRITE))
    return True

def export_disc():
    try:    
        return pickle.load(open(NAME_ARQ,READ))
    except:
        cache = {}
        return cache



