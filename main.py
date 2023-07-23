import asyncio
from contact_info_links_scrapper import LIProfilesScrapper as Lips
from contact_info_scrapper import LIInfoScrapper as Liis
from db_connect import db
from add_data import add_data, add_link


lips = Lips()
liis = Liis()

async def main():
    # setting first page
    page: int = 0
    await db.set_bind('postgresql://postgres:adminpass123@localhost/gino')
    await db.gino.create_all()
    while True:
        page += 1
        lips.get_links(page)
        print(lips.links)
        for link in lips.links:
            #data output
            liis.get_info(link)
            print(f'\n----{liis.name}----')
            print(f'Location: {liis.location}')
            print(liis.info)
            await add_data(liis.name, liis.location, liis.info)
            await add_link(link)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
