import pickle
dbfile = open('people','rb')
db = pickle.load(dbfile)
print(db['mayuri'])
dbfile.close()
