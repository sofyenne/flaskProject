from bs4 import BeautifulSoup as bs 
import requests 
from flask import Flask,jsonify
import requests
import json
from flask_cors import CORS
import urllib.request as ulib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


app = Flask(__name__)
CORS(app)

def get_html(source):
    with ulib.urlopen(source) as u:
        return u.read()

@app.route('/mytek/phone')
def scrap_mytek_tel():

 url = "https://www.mytek.tn/telephonie-tunisie/smartphone-mobile-tunisie/smartphone-tunisie.html"
 index = 0
 nombre_produit=1
 currentpage = 1
 produits = []
 from bs4 import BeautifulSoup as bs

 print(nombre_produit)
 while   index <=nombre_produit:

    
    
    page = get_html(url)
    soup = bs(page)
    blocpagination = soup.find("p" ,  attrs={"id" :"toolbar-amount"}).text.strip()
    nbprod = blocpagination[19:]
    nombre_produit = int(nbprod)
    

    bloc = soup.find_all("ol", attrs={"class": "products list items product-items"})

    for produitlist in bloc:
        produit = produitlist.find_all("li")
        for item in produit:
            produit = {}
            image = item.div.div.a.span.span.img["src"].strip()
            
            name = item.find("strong" , attrs={"class" : "product name product-item-name"}).a.text
            
            lien = item.div.div.a["href"].strip()
            
            categorie = "smartphone"
            
            prix = item.find("span" , attrs={ "class" : "price"}).text.strip()
            prix = int(prix[:-4])

            site_officiel="mytek"

            etat = "disponible"
            
            marque=""
            marques = ["ALCATEL" , "CROSSCALL" , "EVERTEK" , "HUAWEI" ,"INFINIX" , "ITEL" , "LP" , "CONDOR","DOOGEE","HONOR" ,"IKU","IPRO","LEAGOO","NOKIA","REALME","SMARTEC","XIAOMI"]
            for im in marques :
                if(im in name):
                    marque = im
                    break

            
            refernece = item.find("div" , attrs={"class" : "product-item-inner"}).div.div.form["data-product-sku"]
            
            index = index + 1

            produit['nom'] = name
            produit['image']= image
            produit['prix']=prix
            produit['description']= ""
            produit['etat']=etat
            produit['marque']=marque
            produit['lien']=lien
            produit['site_officiel']=site_officiel
            produit['categorie'] = categorie
            produit['reference'] = refernece
            produits.append(produit)
              
    print(nombre_produit)  
    print(index)
         
    currentpage =currentpage +1
    curr = str(currentpage)
    url="https://www.mytek.tn/telephonie-tunisie/smartphone-mobile-tunisie/smartphone-tunisie.html?p="+curr
    print(url)
        

 return jsonify(
       
        produits
    )


@app.route('/mytek/pc')
def scrap_mytek_pc():

 url = "https://www.mytek.tn/informatique/ordinateurs-portables/pc-portable.html"
 index = 0
 nombre_produit=1
 currentpage = 1
 produits = []
 from bs4 import BeautifulSoup as bs

 print(nombre_produit)
 while   index <=nombre_produit:

    
    
    page = get_html(url)
    soup = bs(page)
    blocpagination = soup.find("p" ,  attrs={"id" :"toolbar-amount"}).text.strip()
    nbprod = blocpagination[19:]
    nombre_produit = int(nbprod)
    

    bloc = soup.find_all("ol", attrs={"class": "products list items product-items"})

    for produitlist in bloc:
        produit = produitlist.find_all("li")
        for item in produit:
            produit = {}
            image = item.div.div.a.span.span.img["src"].strip()
            
            name = item.find("strong" , attrs={"class" : "product name product-item-name"}).a.text
            
            lien = item.div.div.a["href"].strip()
            
            categorie = "PcPortable"
            
            prix = item.find("span" , attrs={ "class" : "price"}).text.strip()
            prix = int(prix[:-4])

            site_officiel="mytek"

            etat = "disponible"
            
            marque=""
            marques = ["ACER" , "DELL" , "ASUS" , "LENOVO" ,"VEGA" , "HP" , "MSI" , "VERSUS"]
            for im in marques :
                if(im in name):
                    marque = im
                    break

            
            refernece = item.find("div" , attrs={"class" : "product-item-inner"}).div.div.form["data-product-sku"]
            
            index = index + 1

            produit['nom'] = name
            produit['image']= image
            produit['prix']=prix
            produit['description']= ""
            produit['etat']=etat
            produit['marque']=marque
            produit['lien']=lien
            produit['site_officiel']=site_officiel
            produit['categorie'] = categorie
            produit['reference'] = refernece
            produits.append(produit)
              
    print(nombre_produit)  
    print(index)
         
    currentpage =currentpage +1
    curr = str(currentpage)
    url="https://www.mytek.tn/informatique/ordinateurs-portables/pc-portable.html?p="+curr
    print(url)
        

 return jsonify(
       
        produits
    )


@app.route('/tunisianet/pc')
def scrap_tunisia_net():
    url = "https://www.tunisianet.com.tn/702-ordinateur-portable"
    produits = []
    currentpage = 1
    nombre_produit = 1
    index = 0
    while nombre_produit > index:
        from bs4 import BeautifulSoup as bs
        import requests
        r = requests.get(url)
        soup = bs(r.content)
        bloc = soup.find_all("div", attrs={"class": "products product-thumbs row wb-product-list"})
        for i in bloc:
            prod = i.find_all("div", attrs={"class": "item-product col-xs-12"})

            for item in prod:
                produit = {}

                lien = item.article.div.div.a["href"].strip()

                image = item.article.div.div.a.img["src"].strip()

                nom = item.find("h2", attrs={"class": "h3 product-title"}).text

                site_officiel="tunisia_net"





                etat = item.find("div", attrs={"id": "stock_availability"}).text.strip()

                marque = item.find("div", attrs={"class": "product-manufacturer"}).a.img["alt"].strip()
                marque = marque.upper()

                categorie = "PcPortable"

                prix = item.find("span", attrs={"class": "price"}).text
                prix = prix[:-7]
                if len(prix) >= 4:
                    prix = prix.replace(prix[1], "")

                ref = item.find("span", attrs={"class": "product-reference"}).text
                ref = ref[1:-1]
                index = index + 1
                produit['nom'] = nom
                produit['image'] = image
                produit['prix'] = prix

                produit['etat'] = etat
                produit['marque'] = marque
                produit['lien'] = lien
                produit['site_officiel'] = site_officiel
                produit['categorie'] = categorie
                produit['reference'] = ref
                produits.append(produit)
        currentpage = currentpage + 1
        curr = str(currentpage)
        bloc2 = soup.find("section", attrs={"id": "products"})
        element = bloc2.find("div",
                             attrs={
                                 "class": "col-md-4 col-lg-4 col-xl-4 hidden-lg-down total-products text-xs-right"}).p.text

        y = element.replace(" ", "-")

        z = y[7:10]

        b = int(z)

        url = "https://www.tunisianet.com.tn/702-ordinateur-portable?page="+curr
        
        nombre_produit = b
        
    return jsonify(
       
        produits
    )
