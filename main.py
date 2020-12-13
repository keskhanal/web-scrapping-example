from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/p/pl?d=graphic+card'

#Opening up connection, grabbing the page
page = ureq(my_url)
page_html = page.read()
page.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each products
containers = page_soup.findAll("div",{"class":"item-container"})

file_name = "products.csv"
f = open(file_name, "w")

#headers of the file
headers = "brand, product_name, price, shipping_cost\n"
f.write(headers)
 
for container in containers:
    brand = ""
    try:
       brand = container.div.div.a.img["title"].title()
    except:
       pass
    # brand = container.div.div.a.img["title"].title()

    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    price_container = container.findAll("li",{"class":"price-current"})
    price = price_container[0].text
    
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping_price = shipping_container[0].text
    
    # print(f"Brand name of product: {brand}")   
    # print(f"Name of the product: {product_name}")
    # print(f"Price of product: {price}")
    # print(f"shipping price: {shipping_price}")

    f.write(brand + "," + product_name.replace(",","-") + "," + price + "," + shipping_price + "\n")

f.close()