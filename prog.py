import csv

with open('couleurs_preferees.csv') as fichier_csv:
   reader = csv.reader(fichier_csv, delimiter=',')
   for ligne in reader:
      print(ligne)