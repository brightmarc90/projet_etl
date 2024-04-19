
# Projet ETL

![# Projet ETL](./projet-elt.jpg)

## Description 

Nous avons été mandaté par notre client pour développer un projet ETL (Extract, Transform, Load) en python pour manipuler à partir de différents types de formats CSV, XML, JSON, et l'accès aux données via une API ou une base de données MySQL.

## Fonctionnalités 

1. Extraction de données à partir de fichiers CSV, XML, JSON, une API ou une base de données MySQL.

2. Transformation de données selon les besoins spécifiques du projet.

3. Chargement de données transformées dans une base de données MySQL ou dans un fichier de sortie au format spécifié.

### Configuration requise
 
- Python3

## Bibliothèques Python :

- pip pandas,
- requests,
- mysql-connector-python

## Structure du projet

```
/dataset: Dossier regroupant différents types de fichiers de données
/loaded_files: Dossier récupérant les fichiers traités
/src: Code source du projet.
|___ /data: Dossier de données quelconque
|___ /extraction: Module s'occupant de l'extraction de données
|___ /helpers: Module de fonctions réutisables pour les calculs, les filtres et biens plus ...
|___ /loading: Module s'occupant du chargement des données une fois traiter en format de DataFrame
|___ /transformation: Module de fonctions s'occupant du traitement des données , nettoyage des données erronnées et manquantes , etc ...

```


## Fichiers Principaux

- **README.md**: Documentation principale du projet.
- **requirements.txt**: Liste des dépendances du projet.
- **LICENSE**: Licence du projet.


## Installation et lancement du Projet 


### Installation : 

1. Clonez ce dépôt sur votre machine

    ```git clone https://github.com/brightmarc90/projet_etl.git```

### Configuration :

2. Assurez-vous d'installer les bibliothèques Python et dépendances requises en exécutant ces lignes de commandes:

    ```pip install -r requirements.txt```



### Pour exécuter le projet 

Ouvrez une console dans le dossier projet_etl et entrez les commandes suivantes:

1. Exécutez le script principal en utilisant la commande suivante pour vous placez dans le dossier src :

    ```cd src```

2. Exécutez le script principal en utilisant la commande suivante :

    ```python main.py```