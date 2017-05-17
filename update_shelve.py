from initdata import mayuri
import shelve
db = shelve.open('people-shelve')
mayuri = db['mayuri']
mayuri['salary'] *= 1.5
db['mayuri'] = mayuri
db.close()
