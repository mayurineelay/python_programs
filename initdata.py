mayuri = {'name':'mayuri gadewar','age':1,'salary':50000}
anay = {'name':'anay neelay','age':2,'salary':100000}
nitin = {'name':'nitin neelay','age':5}
db = {}
db['mayuri'] = mayuri
db['anay'] = anay
db['nitin'] = nitin

if __name__ == '__main__':
    for key in db:
        print(key ,'=> ',db[key])   	  
