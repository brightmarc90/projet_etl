-- Création de la table users
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    age INTEGER,
    email TEXT
);

-- Insertion des données
INSERT INTO users (nom, prenom, age, email) VALUES
    ('Doe', 'John', 30, 'john.doe@example.com'),
    ('Smith', 'Jane', 25, 'smith@example.com'),
    ('Johnson', 'Michael', 35, 'michael.johnson@example.com'),
    ('Brown', 'Emily', 28, 'emily.brown@example.com'),
    ('Jones', 'David', 45, 'david.jones@example.com'),
    ('Taylor', 'Alex', NULL, 'alex.taylor@example.com'),  -- Valeur manquante pour l'âge
    ('Williams', 'Jessica', 22, 'jessica.williams@example.com'),
    ('Anderson', 'Ryan', 29, NULL),  -- Valeur manquante pour l'adresse e-mail
    ('Martinez', NULL, 37, 'maria.martinez@example.com'),  -- Valeur manquante pour le prénom
    ('Miller', 'Chris', NULL, NULL),  -- Valeurs manquantes pour le prénom et l'adresse e-mail
    ('Wilson', 'Laura', 33, 'laura.wilson@example.com'),
    ('Thomas', NULL, 40, 'kevin.thomas@example.com'),  -- Valeur manquante pour le nom de famille
    ('Harris', 'Sarah', 26, NULL),  -- Valeur manquante pour l'adresse e-mail
    ('Lee', NULL, NULL, 'andrew.lee@example.com'),  -- Valeurs manquantes pour le prénom et le nom de famille
    ('Garcia', 'Jennifer', 34, 'jennifer.garcia@example.com');
