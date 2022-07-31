#import libraries
import pandas as pd
import numpy as np
import requests
import bs4 as BeautifulSoup

my_url = 'https://www.ambitionbox.com/list-of-companies?page=1'

#Opening up connection, grabbing the page
webpage = requests.get(my_url).text
soup = BeautifulSoup.BeautifulSoup(webpage,'lxml')

final_df=pd.DataFrame()
for j in range(1,5):
   webpage=requests.get('https://www.ambitionbox.com/list-of-companies?page={}'.format(j)).text
   soup = BeautifulSoup.BeautifulSoup(webpage,'lxml')
   
   company=soup.find_all('div',class_='company-content-wrapper')
   
   name=[]
   rating=[]
   reviews=[]
   ctype=[]
   hq=[]
   how_old=[]
   no_of_employee=[]
   
   for i in company:
      try:
         name.append(i.find('h2').text.strip())
      except:
         name.append(np.nan)
      
      try:
         rating.append(i.find('p',class_='rating').text.strip())
      except:
         rating.append(np.nan)
      
      try:
        reviews.append(i.find('a' , class_='review-count').text.strip())
      except:
        reviews.append(np.nan)
      
      try:
        ctype.append(i.find_all('p',class_='infoEntity')[0].text.strip())
      except:
          ctype.append(np.nan)
      
      try:
        hq.append(i.find_all('p',class_='infoEntity')[1].text.strip())
      except:
        hq.append(np.nan)
      
      try:
        how_old.append(i.find_all('p',class_='infoEntity')[2].text.strip())
      except:
        how_old.append(np.nan)
      
      try:
         no_of_employee.append(i.find_all('p',class_='infoEntity')[3].text.strip())
      except:
        no_of_employee.append(np.nan)
      
      df=pd.DataFrame({
          'name':name,
          'rating':rating,
          'reviews':reviews,
          'company_type':ctype,
          'Head_Quarters':hq,
          'Company_Age':how_old,
          'No_of_Employee':no_of_employee,
        })
      
      final_df=pd.concat([final_df, df], ignore_index=True)
      
final_df.to_csv("company.csv", sep='\t', encoding='utf-8')