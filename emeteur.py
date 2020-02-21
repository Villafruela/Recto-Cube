# Programme du "Recto-Cube" pour Scénario Starfinder
# "Recto-Cube" Program for Starfinder. An artefact to use in different Scenari
# Emeteur / Emiter

# IMPORTATIONS

import microbit as m
import radio

# INITIALISATIONS
radio.on()

# BOUCLE / LOOP
while True:
    m.display.clear() 
    if m.button_a.was_pressed():
        radio.send('oui') # replace with Yes in english
        m.display.show(m.Image.YES)
        m.sleep(1000)
    if m.button_b.was_pressed():
        radio.send('non') # replace with No in english
        m.display.show(m.Image.NO)
        m.sleep(1000)