import requests
from bs4 import BeautifulSoup
infile=open("out.html",'w')
html = requests.get("https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States") #reading the website using request package
soup = BeautifulSoup(html.content, "html.parser") #Parsing the html content
req_list=soup.find('table',{"class" : "wikitable sortable plainrowheaders"}) #reading the specific table regarding the states and capitals
infile.write(str(req_list)) #writing the table to a html file


