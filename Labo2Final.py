import statistics
import math

#Étape 1
#https://stackoverflow.com/questions/35516096/reading-a-file-and-storing-contents-into-a-dictionary-python comment mettre des fichiers dans un dictionnaire
info_equipe = {}
fichier_equipe = ['data1.txt', 'data2.txt', 'data3.txt']
for fichier in fichier_equipe:
    with open(fichier, 'r') as f:
        lire = f.readlines()
        equipe= lire[0].strip()
        temps = [float(lire.strip()) for lire in lire[1:]]
        info_equipe[equipe] = temps
#Étape 2
while True:
    print('1) Afficher les statistiques')
    print('2) Afficher l\'équipe la plus homogène')
    print('3) Ajouter une faute à une équipe')
    print('4) Sauvegarder les statistiques')
    print('5) Sortir')
    choix_utilisateur = int(input("Choisisez l'action à faire: "))
    
#Étape 3

    if choix_utilisateur == 1:

        equipe_fast = ''
        temps_fast = float('inf')

        for team, times in info_equipe.items():
            temps_win = statistics.mean(times)

            if temps_win < temps_fast:
                equipe_fast = team
                temps_fast = temps_win

        print(f'Coureur gagnant fait parti de: {equipe_fast} et a un temps de: ({temps_fast:.2f} secondes)')
        print('Équipe en ordre croissant:')

        for team, times in sorted(info_equipe.items(), key=lambda x: statistics.mean(x[1])):
            temps_win = statistics.mean(times)
            print(f'{team} - La Moyenne est de: {temps_win:.1f}s')

#Étape 4
    
    elif choix_utilisateur == 2:

        meilleur_equipe = ''
        petit_ecart_type = float('inf')

        for team, times in info_equipe.items():
            ecart_type = math.sqrt(sum((x - statistics.mean(times))**2 for x in times) / (len(times) - 1))

            if ecart_type < petit_ecart_type:
                meilleur_equipe = team
                petit_ecart_type = ecart_type

        print(f'Équipe la plus homogène: {meilleur_equipe} ({petit_ecart_type:.2f})')

#Étape 5

    elif choix_utilisateur == 3:
        equipe = input('Équipe: ')
        joueur = input("Numéro de joueur qui a fait l'infraction: ")
        infraction = input('Infraction du joueur est: ')

        with open(f'fautes_{equipe}.txt', 'a') as f:
            f.write(f'{joueur} - {infraction}')
        
    elif choix_utilisateur == 4:
        with open('stats.txt', 'w') as f:
            f.write(f'Coureur gagnant: {equipe_fast} ({temps_fast:})')