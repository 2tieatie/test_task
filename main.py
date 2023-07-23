from contact_info_links_scrapper import LIProfilesScrapper as Lips
from contact_info_scrapper import LIInfoScrapper as Liis

lips = Lips()
liis = Liis()
page: int = 0

while True:
    page += 1
    lips.get_links(page)
    for link in lips.links:
        liis.get_info(link)
        print(f'\n----{liis.name}----')
        print(f'Location: {liis.location}')
        print(liis.info)
