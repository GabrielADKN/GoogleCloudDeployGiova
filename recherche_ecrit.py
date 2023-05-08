# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:47:49 2022
Updated on Thu Oct 27 08:38:22 2022

@author: GabrielADKN
"""
import requests
from bs4 import BeautifulSoup
from shortlink import short
import openai
import os

def recherche_ecrit(donnee_recherche):
    texte = 'Service indisponible'
    try:
        lien_recherche = 'https://www.bing.com/search?q='
        donnee_recherche = donnee_recherche
        lien = lien_recherche + donnee_recherche + " site%3Aagridigitale.net&go=Rechercher&qs=ds&form=QBRE"
        #lien = "https://www.bing.com/search?q=recherche+sur+recherche+sur+la+culture+de+l%27oignon+site%3Awww.agridigitale.net&qs=n&form=QBRE&sp=-1&pq=recherche+sur+recherche+sur+la+culture+de+l%27oignon+site%3Awww.agridigitale.net&sc=0-76&sk=&cvid=A39E05F36AFC45F48B10ACCCEA26C834&ghsh=0&ghacc=0&ghpl="
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
        lien_final = []
        lien_final2 = []
        texte = 'Service indisponible'
        texte2 = ''

        response = requests.get(url=lien, headers=headers)
        #print("Chargement ...")
        try:
            if (response.ok):
                soup = BeautifulSoup(response.text, 'lxml')

                balise_a = soup.findAll('div', {'class': 'b_snippetBigText'})
                balise_b = soup.findAll('li', attrs={'class': 'b_algo'})

                for a in balise_a:
                    texte = a.text

                #recp_lien = soup.find('div', {'class': 'b_title'}).find('a')
                recp_lien = soup.findAll('a', {'class': 'gb_lnk'})
                for a in recp_lien:
                    href = a['href']
                    #lien_final.append(short(href))
                    lien_final.append(href)

                for value in balise_b:
                        href = value.a['href']
                        if "search" not in href and  href != "https://www.agridigitale.net" :
                            lien_final2.append(href)

                #texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+lien_final[0]+"' target='_blank'>"+lien_final[0]+"</a>" + "<br><a href='"+lien_final2[0]+"' target='_blank'>"+lien_final2[0]+"</a>" + "<br><a href='"+lien_final2[1]+"' target='_blank'>"+lien_final2[1]+"</a>"
                texte = texte + "<br>En savoir plus via ces liens : " + "<a href='"+short(lien_final[0])+"' target='_blank'>"+short(lien_final[0])+"</a>" + "<br><a href='"+short(lien_final2[0])+"' target='_blank'>"+short(lien_final2[0])+"</a>" + "<br><a href='"+short(lien_final2[1])+"' target='_blank'>"+short(lien_final2[1])+"</a>"
                return texte
            else:
                lien_recherche = 'https://www.bing.com/search?q='
                donnee_recherche = donnee_recherche
                lien = lien_recherche + donnee_recherche + ' site%3Aagridigitale.net&go=Rechercher&qs=ds&form=QBRE'
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
                lien_final3 = []
                texte = ''

                response = requests.get(url=lien, headers=headers)

                if (response.ok):
                    soup = BeautifulSoup(response.text, 'lxml')
                    balise_a = soup.findAll('li', attrs={'class': 'b_algo'})

                    for value in balise_a:
                        href = value.a['href']
                        if "search" not in href and  href != "https://www.agridigitale.net" :
                            lien_final3.append(href)
                texte2 = repondre_ia(donnee_recherche)
                #texte = texte2 + "<br>En savoir plus via ces liens : " + "<a href='"+lien_final3[0]+"' target='_blank'>"+lien_final3[0]+"</a>" + "<br><a href='"+lien_final3[1]+"' target='_blank'>"+lien_final3[1]+"</a>" + "<br><a href='"+lien_final3[2]+"' target='_blank'>"+lien_final3[2]+"</a>"
                texte = texte2 + "<br>En savoir plus via ce lien : " + "<a href='"+short(lien_final3[0])+"' target='_blank'>"+short(lien_final3[0])+"</a>" + "<br><a href='"+short(lien_final3[1])+"' target='_blank'>"+short(lien_final3[1])+"</a>" + "<br><a href='"+short(lien_final3[2])+"' target='_blank'>"+short(lien_final3[2])+"</a>"
                return texte

        except Exception:
            try:
                lien_recherche = 'https://www.bing.com/search?q='
                donnee_recherche = donnee_recherche
                lien = lien_recherche + donnee_recherche + ' site%3Aagridigitale.net&go=Rechercher&qs=ds&form=QBRE'
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
                lien_final3 = []
                texte = ''

                response = requests.get(url=lien, headers=headers)

                if (response.ok):
                    soup = BeautifulSoup(response.text, 'lxml')
                    balise_a = soup.findAll('li', attrs={'class': 'b_algo'})

                    for value in balise_a:
                        href = value.a['href']
                        if "search" not in href and  href != "https://www.agridigitale.net" :
                            lien_final3.append(href)
                texte2 = repondre_ia(donnee_recherche)
                #texte = texte2 + "<br>En savoir plus via ce lien : " + "<a href='"+lien_final3[0]+"' target='_blank'>"+lien_final3[0]+"</a>" + "<br><a href='"+lien_final3[1]+"' target='_blank'>"+lien_final3[1]+"</a>" + "<br><a href='"+lien_final3[2]+"' target='_blank'>"+lien_final3[2]+"</a>"
                texte = texte2 + "<br>En savoir plus via ces liens : " + "<a href='"+short(lien_final3[0])+"' target='_blank'>"+short(lien_final3[0])+"</a>" + "<br><a href='"+short(lien_final3[1])+"' target='_blank'>"+short(lien_final3[1])+"</a>" + "<br><a href='"+short(lien_final3[2])+"' target='_blank'>"+short(lien_final3[2])+"</a>"
                return texte
            except Exception:
                texte = "Veuillez bien vérifier l’état de votre connexion réseau et reformuler votre demande ou nous contacter via ce lien : <a href='https://bit.ly/3Xmw9no' target='_blank'>https://bit.ly/3Xmw9no</a> ou <a href='https://wa.me/22893109808?text=Chabot redirection vers une persoone physique' target='_blank'>https://bit.ly/3gNRzZW</a>"
                return texte
    except Exception:
        try:
            try:
                lien_recherche = 'https://www.bing.com/search?q='
                donnee_recherche = donnee_recherche
                lien = lien_recherche + donnee_recherche + ' site%3Aagridigitale.net&go=Rechercher&qs=ds&form=QBRE'
                headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36'}
                lien_final3 = []
                texte = ''

                response = requests.get(url=lien, headers=headers)

                if (response.ok):

                    soup = BeautifulSoup(response.text, 'lxml')
                    balise_a = soup.findAll('li', attrs={'class': 'b_algo'})

                    for value in balise_a:
                        href = value.a['href']
                        if "search" not in href and  href != "https://www.agridigitale.net" :
                            lien_final3.append(href)

                texte2 = repondre_ia(donnee_recherche)
                #texte = texte2 + "<br>En savoir plus via ce lien : " + "<a href='"+lien_final3[0]+"' target='_blank'>"+lien_final3[0]+"</a>" + "<br><a href='"+lien_final3[1]+"' target='_blank'>"+lien_final3[1]+"</a>" + "<br><a href='"+lien_final3[2]+"' target='_blank'>"+lien_final3[2]+"</a>"
                texte = texte2 + "<br>En savoir plus via ces liens : " + "<a href='"+short(lien_final3[0])+"' target='_blank'>"+short(lien_final3[0])+"</a>" + "<br><a href='"+short(lien_final3[1])+"' target='_blank'>"+short(lien_final3[1])+"</a>" + "<br><a href='"+short(lien_final3[2])+"' target='_blank'>"+short(lien_final3[2])+"</a>"
                return texte
            except Exception:
                texte = recherche_hors_agd(donnee_recherche)
                return texte
        except Exception:
            texte = "Je n'ai pas compris, veuillez reformuler votre demande ou nous contacter via ce lien : <a href='https://wa.me/22893109808?text=Chabot redirection vers une persoone physique' target='_blank'>https://bit.ly/3gNRzZW</a> "
            return texte

def repondre_ia(question):
    # Call the OpenAI API to get the answer to the question
    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="repond a la question suivante d'une facon claire et conscise avec un maximum de 70 mots : "  + question + "?",
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0]['text'].strip()

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

            #recp_lien = soup.find('div', {'class': 'b_title'}).find('a')
            if texte == '':
                texte = "J'ai trouvé des informations qui pouront vous intéresser."
                #texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+short(lien_final[0])+"' target='_blank'>"+short(lien_final[0])+"</a>"
                texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+lien_final[0]+"' target='_blank'>"+lien_final[0]+"</a>"
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
            #texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+lien_final[0]+"' target='_blank'>"+lien_final[0]+"</a>"
            texte = texte + "<br>En savoir plus via ce lien : " + "<a href='"+short(lien_final[0])+"' target='_blank'>"+short(lien_final[0])+"</a>"
            return texte
    else:
        texte = "Veuillez bien vérifier l’état de votre connexion réseau et reformuler votre demande ou nous contacter via ce lien : <a href='https://bit.ly/3Xmw9no' target='_blank'>https://bit.ly/3Xmw9no</a> ou <a href='https://wa.me/22893109808?text=Chabot redirection vers une persoone physique' target='_blank'>https://bit.ly/3gNRzZW</a>"
        return texte

