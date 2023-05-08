# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:47:49 2022
Updated on Thu Oct 27 08:38:22 2022

@author: GabrielADKN
"""
import requests
from bs4 import BeautifulSoup
from shortlink import short

def recherche_ecrit(donnee_recherche):
    texte = 'Service indisponible'
    try:
        lien_recherche = 'https://www.bing.com/search?q='
        donnee_recherche = donnee_recherche
        lien = lien_recherche + donnee_recherche + " site%3Aagridigitale.net&go=Rechercher&qs=ds&form=QBRE"
        #lien = "https://www.bing.com/search?q=recherche+sur+recherche+sur+la+culture+de+l%27oignon+site%3Awww.agridigitale.net&qs=n&form=QBRE&sp=-1&pq=recherche+sur+recherche+sur+la+culture+de+l%27oignon+site%3Awww.agridigitale.net&sc=0-76&sk=&cvid=A39E05F36AFC45F48B10ACCCEA26C834&ghsh=0&ghacc=0&ghpl="
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
        lien_final = []
        texte = 'Service indisponible'

        response = requests.get(url=lien, headers=headers)
        #print("Chargement ...")
        try:
            if (response.ok):
                soup = BeautifulSoup(response.text, 'lxml')

                balise_a = soup.findAll('div', {'class': 'b_snippetBigText'})

                for a in balise_a:
                    texte = a.text

                #recp_lien = soup.find('div', {'class': 'b_title'}).find('a')
                recp_lien = soup.findAll('a', {'class': 'gb_lnk'})
                for a in recp_lien:
                    href = a['href']

                    lien_final.append(short(href))
                    #lien_final.append(href)

                texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+lien_final[0]+"' target='_blank'>"+lien_final[0]+"</a>"
                #texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+lien_final[0]+"' target='_blank'>"+lien_final[0]+"</a>"
                return texte
            else:
                texte = "Veuillez bien vérifier l’état de votre connexion réseau et reformuler votre demande ou nous contacter via ce lien : <a href='https://bit.ly/3Xmw9no' target='_blank'>https://bit.ly/3Xmw9no</a> ou <a href='https://wa.me/22893109808?text=Chabot redirection vers une persoone physique' target='_blank'>https://bit.ly/3gNRzZW</a>"
                return texte

        except Exception:
            try:
                texte = recherche(donnee_recherche)
                return texte
            except Exception:
                lien_utile = soup.findAll('div', {'class': 'b_attribution'})
                list_temp = []
                for value in lien_utile:
                    if "search" or "SEARCH" in value.text:
                        temp = value.text
                        list_temp.append(temp)
                texte = recherche2(list_temp[0],donnee_recherche)
                return texte
    except Exception:
        try:
            texte = recherche_hors_agd(donnee_recherche)
            return texte
        except Exception:
            texte = "Je n'ai pas compris, veuillez reformuler votre demande ou nous contacter via ce lien : <a href='https://wa.me/22893109808?text=Chabot redirection vers une persoone physique' target='_blank'>https://bit.ly/3gNRzZW</a> "
            return texte

def recherche(donnee_recherche):
    lien_recherche = 'https://www.bing.com/search?q='
    donnee_recherche = donnee_recherche
    lien = lien_recherche + donnee_recherche + ' site%3Aagridigitale.net&go=Rechercher&qs=ds&form=QBRE'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
    lien_final = []
    texte = ''

    response = requests.get(url=lien, headers=headers)

    if (response.ok):

        soup = BeautifulSoup(response.text, 'lxml')
        #print(response.text)
        balise_a = soup.findAll('li', attrs={'class': 'b_algo'})
        #print("ici1")
        #final_a = balise_a.a
        #print(final_a)
        #print("ici2")
        for value in balise_a:
            href = value.a['href']
            if "search" not in href and  href != "https://www.agridigitale.net" :
                lien_final.append(href)
        # href = final_a['href']
        # lien_final.append(href)
        #print(lien_final)

        lien = lien_final[0]
        response = requests.get(url=lien, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')
        titre = soup.findAll('h2', {'class': 'utf_post_title post-title'})
        sous_titre = soup.findAll('b', {'class': 'post-lead'})
        #contenu = soup.findAll('div', {'class': 'post-detail margin-b50'})
        contenu1 = soup.find_all('div', {'style': 'text-align:justify;'})[1].text
        contenu2 = soup.find_all('p')[2].text
        contenu3 = soup.find_all('p')[3].text

        for value in titre:
            temp = value.text
        texte = "<b>" + temp + "</b>"

        for value in sous_titre:
            temp = value.text
        texte = texte + "<br>" + temp

        texte = texte + "<br>" + contenu1 + contenu2 + contenu3 + "..."

        temp = "<br>En savoir plus via ce lien : " + "<a href='"+short(lien_final[0])+"' target='_blank'>"+short(lien_final[0])+"</a>"
        #temp = "<br>Voici le lien de l'articles sur le notre site : <br>" + "<a href='"+lien_final[0]+"' target='_blank'>"+lien_final[0]+"</a>"
        texte = texte + temp

        temp = "<br>Voici d'autres articles qui pouront vous interesser : <br>" + "<a href='"+short(lien_final[1])+"' target='_blank'>"+short(lien_final[1])+"</a>" + "<br>" + "<a href='"+short(lien_final[2])+"' target='_blank'>"+short(lien_final[2])+"</a>" + "<br>" + "<a href='"+short(lien_final[3])+"' target='_blank'>"+short(lien_final[3])+"</a>" + "<br>"
        #temp = "<br>Voici d'autres articles qui pouront vous interesser : <br>" + "<a href='"+lien_final[1]+"' target='_blank'>"+lien_final[1]+"</a>" + "<br>" + "<a href='"+lien_final[2]+"' target='_blank'>"+lien_final[2]+"</a>" + "<br>" + "<a href='"+lien_final[3]+"' target='_blank'>"+lien_final[3]+"</a>" + "<br>"
        texte = texte + temp
        return texte
    else:
        texte = "Veuillez bien vérifier l’état de votre connexion réseau et reformuler votre demande ou nous contacter via ce lien : <a href='https://bit.ly/3Xmw9no' target='_blank'>https://bit.ly/3Xmw9no</a> ou <a href='https://wa.me/22893109808?text=Chabot redirection vers une persoone physique' target='_blank'>https://bit.ly/3gNRzZW</a>"
    return texte

def recherche2(lien,donnee_recherche):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36'}
    lien_final = []
    texte = ''

    response = requests.get(url=lien, headers=headers)

    try:
        if (response.ok):
            soup = BeautifulSoup(response.text, 'lxml')

            balise_a = soup.findAll('a', {'class': 'titleSousTitreBix'})
            for a in balise_a:
                href = a['href']
                lien_final.append("https://www.agridigitale.net/" + href)

            lien = lien_final[0]
            response = requests.get(url=lien, headers=headers)

            titre = soup.findAll('a', {'class': 'titleHeightSousTitre'})
            sous_titre = soup.findAll('p', {'class': 'titleSousTitreLast1'})
            contenu1 = soup.find_all('p')[1].text
            contenu2 = soup.find_all('p')[2].text
            contenu3 = soup.find_all('p')[3].text

            for value in titre:
                temp = value.text
            texte = "<b>" + temp + "</b>"

            for value in sous_titre:
                temp = value.text
            texte = texte + temp

            texte = texte + "<br>" + contenu1 + contenu2 + contenu3 + "..."

            temp = "<br>En savoir plus via ce lien : " + "<a href='"+short(lien_final[0])+"' target='_blank'>"+short(lien_final[0])+"</a>"
            #temp = "<br>Voici le lien de l'articles sur le notre site : <br>" + "<a href='"+lien_final[0]+"' target='_blank'>"+lien_final[0]+"</a>"
            texte = texte + temp

            temp = "<br>Voici d'autres articles qui pouront vous interesser : <br>" + "<a href='"+short(lien_final[1])+"' target='_blank'>"+short(lien_final[1])+"</a>" + "<br>" + "<a href='"+short(lien_final[2])+"' target='_blank'>"+short(lien_final[2])+"</a>" + "<br>" + "<a href='"+short(lien_final[3])+"' target='_blank'>"+short(lien_final[3])+"</a>" + "<br>"
            #temp = "<br>Voici d'autres articles qui pouront vous interesser : <br>" + "<a href='"+lien_final[1]+"' target='_blank'>"+lien_final[1]+"</a>" + "<br>" + "<a href='"+lien_final[2]+"' target='_blank'>"+lien_final[2]+"</a>" + "<br>" + "<a href='"+lien_final[3]+"' target='_blank'>"+lien_final[3]+"</a>" + "<br>"
            texte = texte + temp
            return texte

        else:
            texte = "Veuillez bien vérifier l’état de votre connexion réseau et reformuler votre demande ou nous contacter via ce lien : <a href='https://bit.ly/3Xmw9no' target='_blank'>https://bit.ly/3Xmw9no</a> ou <a href='https://wa.me/22893109808?text=Chabot redirection vers une persoone physique' target='_blank'>https://bit.ly/3gNRzZW</a>"

    except Exception:
        try:
            texte = recherche_hors_agd(donnee_recherche)
        except Exception:
            texte = "Je n'ai pas compris, veuillez reformuler votre demande ou nous contacter via ce lien : <a href='https://bit.ly/3Xmw9no' target='_blank'>https://bit.ly/3Xmw9no</a> ou <a href='https://wa.me/22893109808?text=Chabot redirection vers une persoone physique' target='_blank'>https://bit.ly/3gNRzZW</a> "
    return texte

def recherche_hors_agd(donnee_recherche):
    texte = ''
    #print("Recherche en cours")
    lien_recherche = 'https://www.bing.com/search?q='
    donnee_recherche = donnee_recherche
    lien = lien_recherche + donnee_recherche
    #lien = "https://www.bing.com/search?q=recherche+sur+recherche+sur+la+culture+de+l%27oignon+site%3Awww.agridigitale.net&qs=n&form=QBRE&sp=-1&pq=recherche+sur+recherche+sur+la+culture+de+l%27oignon+site%3Awww.agridigitale.net&sc=0-76&sk=&cvid=A39E05F36AFC45F48B10ACCCEA26C834&ghsh=0&ghacc=0&ghpl="
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
    lien_final = []
    texte = ''

    response = requests.get(url=lien, headers=headers)
    #print("Chargement ...")


    if (response.ok):
        soup = BeautifulSoup(response.text, 'lxml')
        try:
            balise_a = soup.findAll('div', attrs={'class': 'b_algo'})
            for value in balise_a:
                href = value.a['href']
                lien_final.append(href)

            balise_a = soup.findAll('div', {'class': 'rwrl rwrl_pri rwrl_padref'})

            for a in balise_a:
                texte = a.text
                #print("Chargement ...")

            #recp_lien = soup.find('div', {'class': 'b_title'}).find('a')
            if texte == '':
                texte = "J'ai trouvé des informations qui pouront vous intéresser."
                texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+short(lien_final[0])+"' target='_blank'>"+short(lien_final[0])+"</a>"
                return texte

            texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+short(lien_final[0])+"' target='_blank'>"+short(lien_final[0])+"</a>"
            #texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+lien_final[0]+"' target='_blank'>"+lien_final[0]+"</a>"
            return texte
        except Exception:
            balise_a = soup.findAll('li', attrs={'class': 'b_algo'})
            for value in balise_a:
                href = value.a['href']
                lien_final.append(href)
            texte = "J'ai trouvé des informations qui pouront vous intéresser."
            texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+short(lien_final[0])+"' target='_blank'>"+short(lien_final[0])+"</a>"
            return texte

    else:
        texte = "Veuillez bien vérifier l’état de votre connexion réseau et reformuler votre demande ou nous contacter via ce lien : <a href='https://bit.ly/3Xmw9no' target='_blank'>https://bit.ly/3Xmw9no</a> ou <a href='https://wa.me/22893109808?text=Chabot redirection vers une persoone physique' target='_blank'>https://bit.ly/3gNRzZW</a>"
        return texte



print(recherche("piment"))