# Her importerer jeg modulen sqlite3 og csv. Det er sånn at jeg kan bruke 
#sqlite3 til å lage en database og csv til å lese en csv fil.
import sqlite3
import csv

# Denne første funksjonen oppretter en database. Hvis databasen allerede eksisterer så kobler den til den.
def create_database():
    conn = sqlite3.connect('Joost_Database.db')  # Her så oppretter jeg en 
    #tilkobling til en SQLite-database med filnavnet 'min_database.db'.
    cursor = conn.cursor()  # Her oppretter jeg en cursor for å utføre SQL-opgaver. 
    #En "cursor" brukes til å utføre SQL-kommandoer og hente data fra databasen.

    # Her så har jeg oprettet en tabell siden den ikke eksisterer.
    # Koden utfører en SQL-kommando som oppretter en tabell med navnet "Person" i en database,
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Person (
            PersonID INTEGER PRIMARY KEY,
            Fornavn TEXT NOT NULL,
            Etternavn TEXT NOT NULL,
            Epost TEXT,
            Telefonnummer TEXT,
            Postnummer TEXT
        );
    ''')

    conn.commit()  # Her bekrefter jeg endirngene som har blitt gjort i databasen.
    conn.close()  # Og her lukker jeg tilkoblingen til databasen.

# Nå er det på tide å legge til en person i databasen, da lager jeg en 
#Funksjon for å legge til en person i databasen
def legg_til_person(fornavn, etternavn, epost, telefonnummer, postnummer):
    conn = sqlite3.connect('Joost_Database.db') 
    cursor = conn.cursor()  

    # Sett inn en ny rad i tabellen med personens informasjon
    cursor.execute('''
        INSERT INTO Person (Fornavn, Etternavn, Epost, Telefonnummer, Postnummer)
        VALUES (?, ?, ?, ?, ?);''', 
        #Insert into person er SQL-setningen for å sette inn data i tabellen "Person". Denne setningen spesifiserer 
    #hvilke kolonner som skal fylles, nemlig "Fornavn", "Etternavn", "Epost", "Telefonnummer" og "Postnummer".

    # På values skal det egentlig settes inn verdiene som er til kollonene over. Men siden jeg skal sette inn
        # csv fil med innholdet senere, så bruker jeg spørsmålstegn som placeholders for å si at senere skal det komme verdier.
    (fornavn, etternavn, epost, telefonnummer, postnummer))



    conn.commit()  # Her bekrefter jeg endirngene som har blitt gjort i databasen.
    conn.close()  # Og her lukker jeg tilkoblingen til databasen.

# dette er en funksjon som blir brukt for å laste opp data fra en CSV-fil til databasen
def last_opp_csv(filnavn):
    conn = sqlite3.connect('Joost_Database.db')  # Her skal den kobles til databasen til Joosst_Database.db
    cursor = conn.cursor()  

    # Det som skal skje her er at den skal åpne CSV-filen og lese rad for rad, 
    # Så skal den legge til en ny perosn for hver rad i
    with open(filnavn, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            legg_til_person(*row)

    conn.commit()  # Bekreft endringene
    conn.close()  # Lukk tilkoblingen til databasen

# Dette er funksjonen som blir brukt for å hente alle personer fra databasen
def hent_alle_personer():
    conn = sqlite3.connect('Joost_Database.db')  # Her kobles sqlite til databasen
    cursor = conn.cursor()  

    # Her hentes alle rader med personer fra tabellen
    cursor.execute('SELECT * FROM Person;')
    result = cursor.fetchall() # denne koden bare henter alle resultatene fra den siste utførte 
    #spørringen og lagrer dem i variabelen result.

    conn.close()  # Lukk tilkoblingen til databasen
    return result  # Denne returnerer resultatet fra spørringen

# Hoveddelen av koden
if __name__ == '__main__':
    create_database()  # Her oppretter jeg databsen, siden jeg ikke har en fra før
    legg_til_person('Ola', 'Nordmann', 'ola@email.com', '12345678', '1234')  # Lagt til Ola Nordmann manuelt
    last_opp_csv('randoms.csv')  # Dette her laster opp dataen fra csv filen, og over til databasen.
    hent_alle_personer()  # Her blir alle personene hentet fra databasen og printet ut.
