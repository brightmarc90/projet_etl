import pandas as pd
from sqlalchemy import create_engine

def extractFromSQL():
    # Remplacez YOUR_DATABASE_URL par l'URL de connexion à votre base de données
    engine = create_engine('../data/sql/user_agents.sql')
    # Remplacez YOUR_QUERY par votre requête SQL
    query = "SELECT * FROM user_agents"

    # Lire les données dans un DataFrame
    df = pd.read_sql_query(query, engine)

    # Afficher les premières lignes du DataFrame
    print(df.head())