from big_scrape import scrape as scrape

def search():
    #first search
    inp1 = raw_input("What is the first game you are looking for? ")
    inp1 = inp1.replace(' ','-').lower()
    platform1 = raw_input("On which platform? ")
    platform1 = platform1.replace(' ','-').lower()
    scrape(platform1, inp1)

    #second search
    inp2 = raw_input("What is the second game you are looking for? ")
    inp2 = inp2.replace(' ','-').lower()
    platform2 = raw_input("On which platform? ")
    platform2 = platform2.replace(' ','-').lower()
    scrape(platform2, inp2)
    
search()