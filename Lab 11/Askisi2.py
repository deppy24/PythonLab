'''Να δημιουργήσετε ένα dataframe για μια λίστα αγορών. Στην πρώτη στήλη θα έχει την περιγραφή του είδους,
 στην δεύτερη την ποσότητα αγοράς και στην τρίτη την τιμή. Θα περιέχει πέντε είδη. Στην συνέχεια προσθέστε
   μια τέταρτη στήλη με το κόστος του κάθε είδους (ποσότητα x τιμή).
'''

import pandas as pd 
import numpy as np 

data={
    'Περιγραφή':['Γραφειο','Kαρεκλα','Αγαλμα','Φωτιστικο','Μολυβοθηκη'],
    'Ποσότητα' :[1,2,5,1,1],
    'Τιμή($)'  :[100,200,10,80,15]}
df = pd.DataFrame(data)
print(df)
df['Συνολικό Κόστος']= df['Ποσότητα']*df['Τιμή($)']

print(f"\n\n{df}")

#3 Υπολογισμός συνολικού κόστους Εύρεση ακριβότερου και φθηνότερου είδους
sum_cost = df['Συνολικό Κόστος'].sum()
print(f"Συνολικό κόστος: {sum_cost}€")
most_cost = df.loc[df['Συνολικό Κόστος'].idxmax()]
min_cost = df.loc[df['Συνολικό Κόστος'].idxmin()]
print(f"Ακριβότερο είδος: {most_cost['Περιγραφή']} με κόστος {most_cost['Συνολικό Κόστος']}€")
print(f"Φθηνότερο είδος: {min_cost['Περιγραφή']} με κόστος {min_cost['Συνολικό Κόστος']}€")


#4 Εμφάνιση ειδών με ποσότητα >= 2 && Εμφάνιση ειδών που αρχίζουν από 'Α'
print(f"\nΕίδη με ποσότητα >= 2:{df[df['Ποσότητα'] >= 2]}")
print(f"\nΕίδη που αρχίζουν από 'Α':{df[df['Περιγραφή'].str.startswith('Α')]}")


#5 Αποθήκευση του DataFrame σε αρχείο Excel
df.to_excel('Λίστα_αγορών.xlsx', index=False)