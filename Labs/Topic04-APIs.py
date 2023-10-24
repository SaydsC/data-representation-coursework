#lecture 4
#Data Representation 23/24

#bookapidao

import requests
url="http://andrewbeatty1.pythonanywhere.com/books"

def getallbooks():
    response = requests.get(url)
    return response.json()

def getbookByID(id):
    geturl = url + "/" + str(id)
    response =  requests.get(geturl)
    return response.json()

def CreateBook(book):
    pass

def updatebook(bookdiff):
    pass

def deletebook(id):
    geturl = url + "/" + str(id)
    response =  requests.delete(geturl)
    return response.json()
    

if __name__ == "__main__":
    #print(getallbooks())
    #print(getbookByID(326))
    #print(deletebook(32))