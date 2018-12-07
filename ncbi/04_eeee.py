import requests
url = "https://www.ncbi.nlm.nih.gov/pubmed/30517910"

result = requests.get(url)
print(result)