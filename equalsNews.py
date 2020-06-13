file = open('index.txt', 'r')
length = file.readline()
file.close()

titles = []
for i in range(int(length)):
  news = open('news/'+str(i)+'.txt', 'r')
  title = news.readline()
  if title in titles:
    print('Notícia repetida! ---> Arquivo: ', i)
  else:
    titles.append(title)
  news.close()