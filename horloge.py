import time
import keyboard

en_pause = False
  
def afficher_heure(heure, mode_12_heures=False):
    heure_affichee = list(heure) 

    if mode_12_heures:
        am_pm = "AM" if heure_affichee[0] < 12 else "PM"
        heure_affichee[0] = heure_affichee[0] % 12
        heure_str = "{:02d}:{:02d}:{:02d} {}".format(heure_affichee[0], heure_affichee[1], heure_affichee[2], am_pm)
    else:
        heure_str = "{:02d}:{:02d}:{:02d}".format(heure_affichee[0], heure_affichee[1], heure_affichee[2])

    print(heure_str, end='\r', flush=True)

def choisir_mode_affichage():
    while True:
        choix = input("Choisissez le mode d'affichage (12 heures/24 heures) : ").lower()
        if choix == "12 heures":
            return True
        elif choix == "24 heures":
            return False
        else:
            print("Choix invalide. Veuillez choisir entre '12 heures' et '24 heures'.")

def regler_heure():
    heures = int(input("Entrez l'heure : "))
    minutes = int(input("Entrez les minutes : "))
    secondes = int(input("Entrez les secondes : "))
    return heures, minutes, secondes

def mettre_en_pause():
    global en_pause
    if keyboard.is_pressed("p"):
        en_pause = not en_pause

# Entrée du mode d'affichage
mode_12_heures = choisir_mode_affichage()
def regler_alarme():
    heures_alarme = int(input("Réglez l'heure de l'alarme : "))
    minutes_alarme = int(input("Réglez les minutes de l'alarme : "))
    secondes_alarme = int(input("Réglez les secondes de l'alarme : "))
    print("Alarme mise pour {:02d}:{:02d}:{:02d}".format(heures_alarme, minutes_alarme, secondes_alarme))
    return heures_alarme, minutes_alarme, secondes_alarme
# Entrée de l'heure utilisateur
heure = regler_heure()

# Réglage de l'alarme utilisateur
alarme = regler_alarme()
print("Pour mettre en pause, appuyer sur 'p'")
try:
    while True:
        mettre_en_pause()

        if not en_pause:
            afficher_heure(heure, mode_12_heures)

            if heure == alarme:
                print("Ding ding ding !! Il est {:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2]))

            heure = (heure[0], heure[1], heure[2] + 1)

            # Si les secondes atteignent 60, ajoute 1 minute
            if heure[2] == 60:
                heure = (heure[0], heure[1] + 1, 0)

            # Si les minutes atteignent 60, ajoute 1 heure
            if heure[1] == 60:
                heure = (heure[0] + 1, 0, 0)

            # Si les heures atteignent 24, réinitialiser les heures à 0
            if heure[0] == 24:
                heure = (0, 0, 0)

        time.sleep(1)

except KeyboardInterrupt:
    print("\nArrêt du programme.")