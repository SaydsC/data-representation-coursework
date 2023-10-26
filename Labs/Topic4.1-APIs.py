#lecture 4
#Data Representation 23/24

#bookapidao

import requests
import json
url="http://andrewbeatty1.pythonanywhere.com/books"

def getallbooks():
    response = requests.get(url)
    return response.json()

def getbookByID(id):
    geturl = url + "/" + str(id)
    response =  requests.get(geturl)
    return response.json()

def CreateBook(book):
    
    response=requests.post(url,json=book)
    #headers={"Content-type":"application/json"}
    #response=requests.post(url, data=json.dumps(book), headers=headers)
    return response.json()

def updatebook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response=requests.put(updateurl, json=bookdiff)
    return response.json()

def deletebook(id):
    deleteurl = url + "/" + str(id)
    response =  requests.delete(deleteurl)
    return response.json()
    

if __name__ == "__main__":
    book = {
        'Author':"test",            
        'Title':"test title",
        "Price": 123
    }
    bookdiff = {
        "Price": 1000000
    }
    #print(getallbooks())
    #print(getbookByID(32))
    #print(deletebook(358))
    #print(CreateBook(book))
    print(updatebook(350, bookdiff))
