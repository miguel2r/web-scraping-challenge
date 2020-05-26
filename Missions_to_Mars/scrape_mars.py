#Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above 
#and return one Python dictionary containing all of the scraped data.
#Importing packages
from selenium import webdriver
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time


#NASA Mars News variables
news_title=[]
news_p=[]
date_ele =[]
pic_ele =[]

#JPL Mars Space Images - Featured Image
featured_image_url =[]
#Mars Weather
mars_weather=[]
#Mars Facts
html_file=[]
#Mars Hemispheres
title=[]
img_url=[]



def mars_news():


#driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
        executable_path = {'executable_path': 'C:/webdrivers/chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        #Scrap for elements required
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain nasa web site
            
        news_elems= soup.find_all('li', class_='slide')
        # Iterate through each 
            
        x=0

        global news_title 
        global news_p
        global date_ele
        global title_ele
        global pic_ele   
        seq_ele=[]

        for news_elem in news_elems:
        # Each news is a new BeautifulSoup object.
        # You can use the same methods on it as you did before.
            if x == 0:
                date_elem = news_elem.find('div', class_='list_date')
                title_elem = news_elem.find('div', class_='content_title')
                desc_elem = news_elem.find('div', class_='article_teaser_body')
                img_elem = news_elem.find('div', class_='list_image')
                href_elem = img_elem.find('img')['src']    
                seq_ele.append(x)
                date_ele.append(date_elem.text)
                news_title.append(title_elem.text)
                news_p.append(desc_elem.text)
                pic_ele.append(href_elem)
            x +=1
                
                
        
        print('Date:',date_ele)
        print('Title:',news_title)
        print('News Paragraph:',news_p)
        print("Picture:",pic_ele)

        # Close the browser after scraping
        browser.quit()




def jpl_mars():
       
        #JPL Mars Space Images - Featured Image
        #Importing packages
        from selenium import webdriver
        import pandas as pd
        from splinter import Browser
        from bs4 import BeautifulSoup
        import requests
        global featured_image_url

        executable_path = {'executable_path': 'C:/webdrivers/chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=False)
        url ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url)

        browser.click_link_by_partial_text('more news')
        for x in range(1, 3):
                html = browser.html
                soup = BeautifulSoup(html, 'html.parser')
                # get the number of pics to be reviewed within this page
                vl_jpl_pics = soup.find_all('li', class_='slide')
                #news_title='33'
                v_count = 0
                v_pag  =0
                vl_href=[]
                for vc_jpl_pics in vl_jpl_pics:
                    link_href = vc_jpl_pics.find('a')
                    link_href= link_href['href']      
                    vl_links_t= vc_jpl_pics.find('div', class_='content_title') 
                    # finding  the picture
                    if vl_links_t.text.strip() == news_title[0]:
                        print('===founded====')
                        print('Title:',v_count," ",vl_links_t.text.strip() )
                        # Click on the picture link reference
                        browser.click_link_by_href(link_href)          
                        html = browser.html
                        soup = BeautifulSoup(html, 'html.parser')
                        xvl_jpl_pics = soup.find_all('div', class_='article_image_container')
                        for xvc_jpl_pics in xvl_jpl_pics:
                            xlink_href = xvc_jpl_pics.find('a')
                            featured_image_url= xlink_href['href']
                            print('Link to Img :',featured_image_url)

                    break
                    vl_href.append(vl_links_t)
                    v_count +=1
                    v_pag +=1
                    print ('pag',x,"Count",v_count)
            # browser.click_link_by_partial_text('MORE')

            # Close the browser after scraping
        browser.quit()

           
      
def Mars_Weather():

#Importing packages
    from selenium import webdriver
    import pandas as pd
    from splinter import Browser
    from bs4 import BeautifulSoup
    import requests

    global mars_weather
    seq_ele=[]
    # the following connection works
    #driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
    executable_path = {'executable_path': 'C:/webdrivers/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    #scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called
    # mars_weather

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain nasa web site
    news_elems= soup.find_all('div', class_='css-1dbjc4n')
    # Iterate through each 
    x=0
    for news_elem in news_elems: 
        if x == 0:
            time.sleep(1)
            mars_weather= news_elem.find('div', class_='css-901oao r-jwli3a r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
            time.sleep(5)
            link_z = mars_weather.find('span')
            seq_ele.append(x)   
        x +=1     
    mars_weather = link_z.text
    print('Data Expected :',mars_weather)
    browser.quit()


def Mars_Facts():

    #Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts
    #about the planet including Diameter, Mass, etc.

    global html_file
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Description', 'Measure']
    #Use Pandas to convert the data to a HTML table string.
    html_file = df.to_html()
    #html_file =vf_html
    print(html_file)
    text_file = open("C:/Users/user/Documents/ITESM_DA/web-scraping-challenge/web-scraping-challenge/Missions_to_Mars/facts.html", "w")
    text_file.write(html_file)
    text_file.close()
    
  
    



def Mars_Hemispheres():
    #Importing packages
    from selenium import webdriver
    import pandas as pd
    from splinter import Browser
    from bs4 import BeautifulSoup
    import requests

    # the following connection works
    #driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
    executable_path = {'executable_path': 'C:/webdrivers/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # get the number of pic to be reviewed
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    vl_pics = soup.find_all('div', class_='item')

    vl_href=[]
    for vc_pics in vl_pics:        
        link = vc_pics.find('a')
        href = link['href']            
        #print('Page:', href)
        vl_href.append(href)
  
    v_count=len(vl_href)


    vl_img_url = []
    vl_title   = []
    vl_dic={}
    global title 
    global img_url 

    for i in range(v_count):
  
        links_found = browser.find_by_tag('h3')[i]
        #k =k + 1
        links_found.click()
   
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        ve_pics = soup.find_all('div', class_='downloads')
        for vc_pics  in ve_pics:
            titlex= soup.h2.text.strip()      
            link = vc_pics.find('a')
            img_urlx = link['href']            
            print('Page',i," ",titlex," ",img_urlx)
            title.append(titlex)
            img_url.append(img_urlx)
            

        
   
        browser.back()
        #convert it to a dictionary
      #  vl_dic= {'title': vl_title,'img_url':vl_img_url}
      # title =vl_dic
        #convert it to df
      #  df = pd.DataFrame(vl_dic)
      #  img_url = df
    # Close the browser after scraping
    browser.quit()
    
    print('Final',title," ",img_url)



def scrape():
  print('-- NASA Mars News Scraping process begins--')
  mars_news()
  print('--NASA Mars Sraping News process done--')
  print('--JPL Mars Space Images process begins--')
  jpl_mars()
  print('--JPL Mars Space Images process done--')
  print('--Mars Weather Space Images process begins--')
  Mars_Weather()
  print('--Mars Weather Space Images process done--')
  print('--Mars Facts Space Images process begins--')
  Mars_Facts()
  print('--Mars Facts Space Images process done--')
  print('--Mars Hemispheres Space Images process begins--')
  Mars_Hemispheres()
  print('--Mars Hemispheres Space Images process done--')

  if len(title) != 0 :
        mars_data = {
                "news_date":date_ele[0],
                "news_title": news_title[0],
                "news_p": news_p[0],
                "news_pic":pic_ele[0],
                "news_picf":featured_image_url,
                "news_m_weather":mars_weather,
                "news_tit0":title[0],
                "news_img0":img_url[0],
                "news_tit1":title[1],
                "news_img1":img_url[1],
                "news_tit2":title[2],
                "news_img2":img_url[2],
                "news_tit3":title[3],
                "news_img3":img_url[3]  
                }
  else:
        mars_data = {
                "news_date":date_ele[0],
                "news_title": news_title[0],
                "news_p": news_p[0],
                "news_pic":pic_ele[0],
                "news_picf":featured_image_url,
                "news_m_weather":mars_weather 
                }


  return mars_data




if __name__ == "__main__":
   print('Scraping ---Begins')
   scrape()
   print('Scraping ---Done')