from fastapi import FastAPI
app = FastAPI()

myList=[10,20,30,40,50]

@app.get('/')  # Read
def index():
    return myList

@app.post('/add/{n:int}')  # create
def add(n:int):
    myList.append(n)
    return myList 

@app.put('/update/{n:int}')  #update
def update(n:int,a:int):
    myList[n]=a
    return myList

@app.delete('/remove/{n:int}') # delete
def remove(n:int):
    myList.remove(n)
    return myList
    
