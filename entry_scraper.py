import urllib.request, sys
from bs4 import BeautifulSoup

search = sys.argv[1]
url = 'https://eksisozluk.com/'+search
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response.read(), 'html.parser')
page_count = soup.find(class_='pager')['data-pagecount']

with open(search+".txt", "w") as file:
    for i in range(1,int(page_count)+1):
        response = urllib.request.urlopen(url+'?p='+str(i))
        soup = BeautifulSoup(response.read(), 'html.parser')

        file.write('PAGE ' + str(i) + '\n')
        file.write('----------------\n')
        file.writelines([item.text.strip('\n') for item in soup.find_all(class_='content')])
        file.write('\n')