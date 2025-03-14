from fastapi import FastAPI 

app=FastAPI()

@app.get('/hello/{name:str}/{age:int}')
def f(name:str,age:int):
    return f'{name} is {age} years old.'