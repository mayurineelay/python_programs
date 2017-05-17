mayuri = {'name':'mayuri gadewar','age':1,'salary':50000}
anay = {'name':'anay neelay','age':2,'salary':100000}
nitin = {'name':'nitin neelay','age':5}
db = {}
db['mayuri'] = mayuri
db['anay'] = anay
db['nitin'] = nitin

import pickle
dbfile = open('people','wb')
pickle.dump(db,dbfile)
dbfile.close()
