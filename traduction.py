# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:14:43 2022

@author: GabrielADKN
"""

from googletrans import Translator

def traduire(texte,source,destination):
    try :
        translater = Translator()

        out = translater.translate(texte, src=source, dest=destination)
        return out.text
    except Exception:
        return texte

# texte = "Faire des billons, des planches ou repique le piment sur le sol à plat, épandre sur l’espace à repiquer, une à deux brouettes de fumier ou de compost +1 kg de NPK 15-15-15 avant labour sur les sols lourds, une semaine après repiquage sur les sols sablonneux ou sableux. Choisir lors du repiquage, les plants vigoureux, courts et trapus d ...."
# print(traduire(texte,"fr","en"))