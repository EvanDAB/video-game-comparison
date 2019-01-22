from big_scrape import scrape as scrape

def search():
    inp1 = raw_input("What is the first game you are looking for? ")
    inp1 = inp1.replace(' ','-').lower()

    inp2 = raw_input("What is the second game you are looking for? ")
    inp2 = inp2.replace(' ','-').lower()

    scrape(inp1)
    print('=======  Now looking for the second game =======')
    scrape(inp2)

search()