import requests
from bs4 import BeautifulSoup
import pprint # Used to align the printed logs in a readable style

web_url = input("Enter Website URL: ")

def scrap(web_url):
    res = requests.get(web_url)
    print(res)
    extract_data = BeautifulSoup(res.text,'html.parser')
    head = extract_data.head
    body = extract_data.body
    div = extract_data.find_all('div')
    extract_id = extract_data.find(id='score_35032922')
    extract_id = extract_data.select('.score')
#     print(extract_id)

def get_points_scrap(web_url):
    append_data = []
    higher_rank = []
    res = requests.get(web_url)
    print(res)
    set_text = BeautifulSoup(res.text, 'html.parser')
    extract_links = set_text.select('.titleline')
    extract_vote = set_text.select('.rank')

    for i, item in enumerate(extract_links):
        title = extract_links[i].getText() # getText() -> Gets the content
        links = extract_links[i].get("href", None) # get() -> Gets the atribs
        rank = int(extract_vote[i].getText().replace(".", ""))
        # print(votes)
        append_data.append({'title': title, 'links': links, 'rank':rank})
        if rank <= 3:
            higher_rank.append({'title': title, 'links': links, 'rank':rank})
            pprint.pprint(higher_rank)
    # print(append_data)
    return append_data

pprint.pprint(get_points_scrap(web_url))

