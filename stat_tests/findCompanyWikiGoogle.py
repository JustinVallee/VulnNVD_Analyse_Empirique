import requests
from bs4 import BeautifulSoup

def get_first_wikipedia_link(company_name):

    response = requests.get(f'https://www.google.com/search?q=Wikipedia+{company_name}+software+company')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first link in the search results
        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'url?q=' in href and 'wikipedia.org' in href:

                # Extract the URL
                url = href.split('url?q=')[1].split('&')[0]
                return url
    else:
        print(f"Failed to retrieve search results. Status code: {response.status_code}")
    return None


# Example usage
company = ("juniper")
first_wikipedia_link = get_first_wikipedia_link(company)
print(first_wikipedia_link)
