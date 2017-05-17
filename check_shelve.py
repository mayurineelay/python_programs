import shelve
db = shelve.open('people-shelve')
print(db['mayuri'])
db.close()
