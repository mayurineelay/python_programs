from initdata import mayuri,nitin
import shelve
db = shelve.open('people-shelve')
db['mayuri'] = mayuri
db['nitin']=nitin
db.close()
