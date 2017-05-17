import shelve
fieldnames = {'name','age','salary'}
db = shelve.open('people-shelve')
while True:
    key = input('key? =>') 
    if not key: break
    try:
        record = db[key]
    except:
        print('No matching key')
    else:
        for field in fieldnames:
            print(getattr(record,field)) 
