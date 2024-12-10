import requests
from bs4 import BeautifulSoup


url = "https://www.geeksforgeeks.org/how-to-extract-pdf-tables-in-python/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

i = 0

for link in links:
    if ('.pdf' in link.get('href', [])):
        i += 1
        print("Downlaoding file:", i)

        response = requests.get(link.get('href'))

        pdf = open("pdf"+str(i)+".pdf",'wb')
        pdf.write(response.content)
        pdf.close()
        print("file", i, "downloaded")
print("All PDF files downloaded")