import requests
import bs4
from urllib import urlopen
from bs4 import BeautifulSoup

# match = soup.title        // only title with its tags around it
# match = soup.title.text   // only title text
# match = soup.div          // all div elements and all the elements with the div elements
# match = soup.find('footer', class_='page-footer')  find specific element and all the elements within it

def scrape(platform, searchItem):
    try: 
        print('======= Loading =======')

        url = 'http://www.metacritic.com/game/'+ platform +'/' + searchItem + '/'
        url2 = 'http://www.metacritic.com/game/'+ platform +'/' + searchItem + '/critic-reviews'

        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,}

        r = requests.get(url, headers=headers)
        r3 = requests.get(url2, headers=headers)

        stat = r.status_code

        text = r.text
        text2 = r3.text 

        soup = BeautifulSoup(text, 'lxml')
        soup2 = BeautifulSoup(text2, 'lxml')

        gameTitle = soup.find('div', class_='product_title')
        gameTitleText = gameTitle.a.h1.text
        metaRating = soup.find('div', class_='metascore_w')
        metaRatingText = metaRating.span.text
        userRating = soup.find('div', class_='user')
        userRatingText = userRating.text
        print('Product Title: ' + gameTitleText)

        summary = soup.find('span', class_='blurb')
        sumText = summary.text
        print('Summary: ' + sumText)


        dev = soup.find('li', class_="developer")
        devSpan = dev.findAll('span')
        devText = devSpan[1].text
        print('Developer: ' + devText)

        gen = soup.find('li', class_="product_genre")
        genSpan = gen.findAll('span')
        print('Genres: ')
        for i in genSpan[1:]: 
            print( i.text)

        esrb = soup.find('li', class_="product_rating")
        esrbSpan = esrb.findAll('span')
        esrbText = esrbSpan[1].text
        print('ESRB Rating: ' + esrbText)
        print('Metascore rating: ' + metaRatingText)
        print('Metascore UserRating: ' + userRatingText)

        ign = soup2.find('a', string='IGN')
        ignP = ign.parent.parent.parent
        ignS = ignP.find('div', class_="review_grade")
        ignST = ignS.div.text
        print('IGN: ' + ignST)

        gi = soup2.find('a', string='Game Informer')
        giP = gi.parent.parent.parent
        giS = giP.find('div', class_="review_grade")
        giST = giS.div.text
        print('GameInformer: ' + giST)

        gs = soup2.find('a', string='GameSpot')
        gsP = gs.parent.parent.parent
        gsS = gsP.find('div', class_="review_grade")
        gsST = gsS.div.text
        print('GameSpot: ' + gsST)

    except AttributeError as inst:
        print('Sorry we were unable to find ', self)
        print(inst)



