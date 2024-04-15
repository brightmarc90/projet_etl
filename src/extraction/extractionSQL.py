import sqlite3
import pandas as pd

def extractFromSQL(tb, db, columns, data):
    # Connexion à la base de données SQLite
    conn = sqlite3.connect(f"{db}.db")
    c = conn.cursor()

    # Supprimer la table si elle existe déjà
    c.execute(f"DROP TABLE IF EXISTS {tb}")

    # Création de la table avec les colonnes spécifiées
    create_table_query = f"CREATE TABLE {tb} (id INTEGER PRIMARY KEY,"
    create_table_query += ",".join([f"{col} TEXT" for col in columns])
    create_table_query += ")"
    c.execute(create_table_query)

    # Insertion des données dans la table
    placeholders = ",".join(["?" for _ in range(len(columns))])  # +1 pour l'ID
    insert_query = f'INSERT INTO {tb} VALUES (NULL, {placeholders})'
    c.executemany(insert_query, data)

    # Lecture des données dans un DataFrame
    select_query = f'SELECT * FROM {tb}'
    df = pd.read_sql_query(select_query, conn)

    # Affichage des premières lignes du DataFrame
    print(df.head())

    # Fermeture de la connexion
    conn.close()

# Définition des noms de colonnes et des données
columns = ['nom', 'prenom', 'age', 'email']
data = [
    ('Doe', 'John', 30, 'john.doe@example.com'),
    ('Smith', 'Jane', 25, 'smith@example.com'),
    ('Johnson', 'Michael', 35, 'michael.johnson@example.com'),
    ('Brown', 'Emily', 28, 'emily.brown@example.com'),
    ('Jones', 'David', 45, 'david.jones@example.com')
]


# Appel de la fonction pour extraire les données de la base de données SQLite
extractFromSQL('joueur', 'play', columns, data)
