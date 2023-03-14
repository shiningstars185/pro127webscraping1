from bs4 import BeautifulSoup
import requests
import csv
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = requests.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["name", "Distance","Mass","Radius"]
    planet_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for th_tags in soup.find_all("th", attrs={"class","exoplanet"}):
            tr_tags = th_tag.find_all("tr")
            temp_list = []
            for index, th_tag in enumerate(th_tags):
                if index == 0:
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append( "")
            planet_data.append(temp_list)
        browser.find_element_by_xpath()
    with open("scrapper_2.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()
