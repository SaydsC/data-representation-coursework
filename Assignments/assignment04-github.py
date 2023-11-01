# Assignment 04

#Write a program in python that will read a file from a repository, 
#The program should then replace all the instances of the text "Andrew" with your name
#The program should then commit those changes and push the file back to the repository.
#I do not need to see your keys (see lab2, to follow)

from github import Github
import requests

from config import config as cfg #import key from hidden file


file_path = 'https://api.github.com/repos/SaydsC/dataRepresentationPrivate'
github_user = 'SaydsC'
github_repo = 'dataRepresentationPrivate'

github_token = cfg["githubkey"]
g = Github(github_token)

#Specifying private Github repo
repo = g.get_repo("SaydsC/dataRepresentationPrivate")

#Checking repo for required file and getting it's URL
namefile = repo.get_contents("namechange.txt")
nameURL = namefile.download_url

#File content is retrieved 
response = requests.get(nameURL)
contentofthefile = response.text

#Replacing the 5 instances of the name Andrew with the name Sadie
updatednamefile = contentofthefile.replace("Andrew","Sadie")

#Updated text file is pushed to Github
githubpush=repo.update_file(namefile.path,"updated by prog",
updatednamefile,namefile.sha)

print ("Name replaced succesfully")
