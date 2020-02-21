# Programme du Recto-Cube pour Scénario Starfinder
# "Recto-Cube" Program for Starfinder. An artefact to use in different Scenari
# Récepteur / Receptor

# IMPORTATIONS
import microbit as m
import random
import radio as r


# INITIALISATIONS
boutonA = m.button_a
boutonB = m.button_b
# Compteur pour gérer l'éclairage de la LED / Value to manage LED Brightness
compteur = 0
# Variables pour generation de la matrice d'images aléatoire / Variables for the image matrix random generation
imageTab = []
tempImage =[]


# FONCTIONS
# Activation du système radio pour recevoir les messages de l'émeteur / Radio receptor activation
r.on()
# Générateur aléatoire d'image / Random image generator
def generateur():
    listeChoix = ['0', '9']
    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    
    for i in range (6):
        for j in range (6):
                a += random.choice(listeChoix)
                b += random.choice(listeChoix)
                c += random.choice(listeChoix)
                d += random.choice(listeChoix)
                e += random.choice(listeChoix)
    chaine = a+': '+b+': '+c+': '+d+': '+e
    tempImage = m.Image(chaine)
    return tempImage

def battementCoeur(compteur):
        if compteur <=1000:
            m.pin0.write_analog(compteur)
            m.pin1.write_analog(compteur)
            m.pin2.write_analog(compteur)
        elif (compteur > 1000) and (compteur < 2000):
            m.pin0.write_analog(2000-compteur)
            m.pin1.write_analog(2000-compteur)
            m.pin2.write_analog(2000-compteur)
        if compteur == 2000:
            m.pin0.write_analog(0)
            m.pin1.write_analog(0)
            m.pin2.write_analog(0)
            compteur = 0
        compteur = compteur + 50
        return compteur


# CONSTRUCTEURS / CONSTRUCTOR
# Construction du tableau de 30 images aléatoires / Generation of a 30 images array
for i in range (31):
    imageTab.append (generateur())       


# BOUCLE / LOOP
while True:
    m.display.show(imageTab[random.randint(0, 30)])
    message = r.receive()
    if message == 'oui':
        m.display.show(m.Image.YES)
        m.sleep (1000)
    if message == 'non':
        m.display.show(m.Image.NO)
        m.sleep(1000)
    compteur = battementCoeur(compteur)
    m.sleep(300)