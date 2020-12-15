import requests
from bs4 import BeautifulSoup

def getContentPage(url):
  req = requests.get(url)
  if req.status_code == 200:
    content = req.content
  soup = BeautifulSoup(content, 'html.parser')
  return soup

def getTitle(soup, cID):
  header = soup.find(class_=cID)
  title = header.find('h1').text
  return title

def getText(soup, cID):
  text = ''
  body = soup.find(class_=cID)
  paragraphs = body.find_all('p')

  for p in paragraphs:
    text += p.text + ' '
  return text

def writeFile(url, index):
  f = open('news/'+str(index)+'.txt', 'w')
  soup = getContentPage(url)
  title = getTitle(soup, 'GP5k0')
  f.write(getTitle(soup, 'GP5k0'))
  f.write('\n')
  f.write(getText(soup, '_3zUVe'))
  f.write('\n')
  f.close()

def getLink():
  unreadLinks = open('links.txt', 'r')
  links = unreadLinks.readlines()
  unreadLinks.close()

  readLinks = open('readLinks.txt', 'a')
  readLinks.write(links[0])
  readLinks.close()

  return links

def treatLinks(links):
  readLinks = open('readLinks.txt', 'a')
  readLinks.write(links[0])
  readLinks.close()

  del links[0]
  unreadLinks = open('links.txt', 'w+')
  for link in links:
    unreadLinks.write(link)
  unreadLinks.close()

def getIndex():
  file = open('index.txt', 'r')
  index = file.readline()
  file.close()
  return index

def updateIndex(index):
  file = open('index.txt', 'w')
  file.write(str(int(index)+1))
  file.close()

def oldMain():
  index = getIndex()
  links = getLink()

  print('Working on: ', links[0])
  writeFile(links[0].replace('\n', ''), index)

  updateIndex(index)
  treatLinks(links)

def main():
  news = open('links.txt', 'r')
  links = news.readlines()
  it = []
  it.extend(links)

  for url in it:
    index = getIndex()

    print('Working on: ', url.replace('\n', ''))
    writeFile(url.replace('\n', ''), index)

    updateIndex(index)
    treatLinks(links)


main()