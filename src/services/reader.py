import pandas as pd
import glob
import xml.etree.ElementTree as ET

class Reader:
    @staticmethod
    def readerCsv():
        # Le chemin de tous les fichiers qui ont une extension en CSV
        file_paths = glob.glob('data/**/*.csv', recursive=True)
        # Initialiser une liste pour stocker les DataFrames de chaque fichier CSV
        dfs = []
        # Lire tous les fichiers qui ont une extension en CSV et stocker les DataFrames
        for file_path in file_paths:
            df = pd.read_csv(file_path)
            dfs.append(df)
        # Retourner la liste de DataFrames
        return dfs

    @staticmethod
    def readerJson():
        # Le chemin de tous les fichiers qui ont une extension en JSON
        file_paths = glob.glob('data/**/*.json', recursive=True)
        # Initialiser une liste pour stocker les DataFrames de chaque fichier JSON
        dfs = []
        # Lire tous les fichiers qui ont une extension en JSON et stocker les DataFrames
        for file_path in file_paths:
            df = pd.read_json(file_path)
            dfs.append(df)
        # Retourner la liste de DataFrames
        return dfs

    @staticmethod
    def readerXml():
        # Le chemin de tous les fichiers qui ont une extension en XML
        file_paths = glob.glob('data/**/*.xml', recursive=True)

        # Initialiser une liste pour stocker les DataFrames de chaque fichier XML
        dfs = []

        # Parcourir chaque fichier XML
        for file_path in file_paths:
            print(f'Lecture du fichier XML : {file_path}')
            
            # Parse le fichier XML
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Initialiser des listes pour stocker les données
            names = []
            ages = []
            genders = []

            # Parcourir les éléments <person> et extraire les données
            for person in root.findall('person'):
                # Vérifier si l'élément <name> est présent
                name_element = person.find('name')
                if name_element is not None:
                    name = name_element.text
                else:
                    name = None

                # Vérifier si l'élément <age> est présent
                age_element = person.find('age')
                if age_element is not None:
                    age = age_element.text
                else:
                    age = None

                # Vérifier si l'élément <gender> est présent
                gender_element = person.find('gender')
                if gender_element is not None:
                    gender = gender_element.text
                else:
                    gender = None
                
                # Ajouter les données extraites aux listes
                names.append(name)
                ages.append(age)
                genders.append(gender)

            # Créer un DataFrame Pandas à partir des listes
            df = pd.DataFrame({
                'Name': names,
                'Age': ages,
                'Gender': genders
            })

            # Ajouter le DataFrame à la liste
            dfs.append(df)

        # Retourner la liste de DataFrames
        return dfs

# Exemple d'utilisation
json_dfs = Reader.readerJson()
for df in json_dfs:
    print(df.head())

csv_dfs = Reader.readerCsv()
for df in csv_dfs:
    print(df.head())
    
xml_dfs = Reader.readerXml()
for df in xml_dfs:
    print(df.head())
