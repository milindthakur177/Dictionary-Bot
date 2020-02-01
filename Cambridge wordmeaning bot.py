def useresp(response):
  import requests
  from bs4 import BeautifulSoup
  user= "https://dictionary.cambridge.org/dictionary/english/"+response
  result= requests.get(user)
  soup= BeautifulSoup(result.text,"lxml")
  div= soup.find('div',{'class':'pos-body'})
  for row in div.find_all('div',{'class':'def ddef_d db'}):
    meaning= row.text
    meaning= meaning.split(':')
    return meaning[0]

def response(sentence):
  for word in sentence.split(' '):
    try:
      respond= useresp(word)
      return respond
    except Exception:
      return "Please write a valid word!!!"

while True:
  sentence= input("You: ")
  responsed= response(sentence)

  if sentence=="byebot":
    break
  else:
    print("Bot: "+responsed)















