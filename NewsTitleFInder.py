
"""
This is a simple python program to get the latest news from different sources. This code can be changed to 
get information from difffrent sources. This is a concept that can be used for a bigger project where information
is to be gathered from different sources. This code also provides the user with the option to save the information
to a json file. Again this can also be changed, use my code as a framework if you will. We can see a few examples
of pulling data from different sources with diffrent protocals (http & https).
"""
import xml.etree.ElementTree as ET       
import xml.etree.ElementTree as ET       
from bs4 import BeautifulSoup           
import requests 
import json

def FN():
    Url='http://feeds.foxnews.com/foxnews/tech'
    FNREQU=requests.get(Url)
    FNSOUP=BeautifulSoup(FNREQU.content ,'lxml-xml')
    FNTITLES=FNSOUP.find_all('title')
    print(f"The source IP: {Url}")
    counter=1
    output=[]
    for index, title in enumerate(FNTITLES):
        text = title.text.split("<title>")[0]
        if text:
            print(f'  {counter}, {title.text.split("<title>")[0]}')
            output.append({"source": "Fox News", "number": counter, "title": text})
            counter+=1
    return output

def CNN():
    Url='http://rss.cnn.com/rss/cnn_tech.rss'
    CNNREQU=requests.get(Url)
    CNNSOUP=BeautifulSoup(CNNREQU.content ,'lxml-xml')
    CNNTITLES=CNNSOUP.find_all('title')
    print(f"The source IP: {Url}")
    counter=1
    output=[]
    for index, title in enumerate(CNNTITLES[2:]):
        text = title.text.split("<title>")[0]
        if text:
            print(f'  {counter}, {title.get_text().split("<title>")[0]}')
            output.append({"source": "CNN News", "number": counter, "title": text})
            counter+=1
    return output

def BBCN():
    Url='http://feeds.bbci.co.uk/news/technology/rss.xml'
    BBCNREQU=requests.get(Url)
    BBCNSOUP=BeautifulSoup(BBCNREQU.content ,'lxml-xml')
    BBCNTITLES=BBCNSOUP.find_all('title')
    print(f"The source IP: {Url}")
    counter=1
    output=[]
    for index, title in enumerate(BBCNTITLES[2:]):
        text= text = title.text.split("<title>")[0]
        if text:
            print(f'  {counter}, {title.text.split("<title>")[0]}')
            output.append({"source": "British Broad Casting", "number": counter, "title": text})
            counter+=1
    return output

def ABC():
    Url='http://feeds.abcnews.com/abcnews/technologyheadlines'
    ABCREQU=requests.get(Url)
    ABCSOUP=BeautifulSoup(ABCREQU.content ,'lxml-xml')
    ABCTITLES=ABCSOUP.find_all('title')
    print(f"The source IP: {Url}")
    counter=1
    output=[]
    for index, title in enumerate(ABCTITLES[2:]):
        text= text = title.text.split("<title>")[0]
        if text:
            print(f'  {counter}, {title.text.split("<title>")[0]}')
            output.append({"source": "ABC News", "number": counter, "title": text})
            counter+=1
    return output

def CBS():
    Url='http://feeds.abcnews.com/abcnews/technologyheadlines'
    ABCREQU=requests.get(Url)
    ABCSOUP=BeautifulSoup(ABCREQU.content ,'lxml-xml')
    ABCTITLES=ABCSOUP.find_all('title')
    print(f"The source IP: {Url}")
    counter=1
    output=[]
    for index, title in enumerate(ABCTITLES[2:]):
        text= text = title.text.split("<title>")[0]
        if text:
            print(f'  {counter}, {title.text.split("<title>")[0]}')
            output.append({"source": "CBS News", "number": counter, "title": text})
            counter+=1
    return output
def NYT():
        Url='https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml'
        NYTREQU=requests.get(Url)
        NYTSOUP=BeautifulSoup(NYTREQU.content ,'lxml-xml')
        NYTTITLES=NYTSOUP.find_all('title')
        print(f"The source IP: {Url}")
        counter=1
        output=[]
        for index, title in enumerate(NYTTITLES[2:]):
            text = title.text.split("<title>")[0]
            if text:
                print(f'  {counter}, {title.text.split("<title>")[0]}')
                output.append({"source": "The New York Times", "number": counter, "title": text})
                counter+=1
        return output

def WP():
        Url='https://www.washingtonpost.com/business/technology/?outputType=rss'
        WPREQU=requests.get(Url)
        WPSOUP=BeautifulSoup(WPREQU.content ,'lxml-xml')
        WPTITLES=WPSOUP.find_all('title')
        print(f"The source IP: {Url}")
        counter=1
        output=[]
        for index, title in enumerate(WPTITLES[2:]):
            text = title.text.split("<title>")[0]
            if text:
                print(f'  {counter}, {title.text.split("<title>")[0]}')
                output.append({"source": "The Washington Post", "number": counter, "title": text})
                counter+=1
        return output
def main():
    fn_output = FN()
    print('')
    cnn_output = CNN()
    print('')
    bbcn_output = BBCN()
    print('')
    abc_output = ABC()
    nyt_output= NYT()
    print('')
    wp_output = WP()
    print('')
    write_file = input("Do you want to create a file with the results? (y/n): ")
    
    if write_file.lower() == 'y':
        with open('News_Stories.json', 'a') as f:
            json.dump(fn_output + cnn_output + bbcn_output + abc_output, f)
    elif write_file.lower() == 'n':
        print("Thank you for using the News Stories program.")
        exit()
 
if __name__=='__main__':
    main()
