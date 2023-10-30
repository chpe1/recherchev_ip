# IP Address Comparison Script

This Python script is designed to compare IP addresses in multiple CSV and TXT files and identify common IP addresses across them. It extracts IP addresses from these files and performs the comparison to find shared IP addresses.
One IP address per line.

## Usage

To use this script, provide the paths of one or more CSV or TXT files containing IP addresses as command-line arguments. The script will find and display the common IP addresses among the provided files.

Example:

```bash
$ python script.py file1.csv file2.txt
```

## Functions

- `csv_to_list(file)`: Extracts IP addresses from a CSV file and returns them as a set.
- `txt_to_list(file)`: Extracts IP addresses from a text (TXT) file and returns them as a set.
- `load_ip_addresses_from_file(file_path)`: Loads IP addresses from a CSV or TXT file and returns them as a set.
- `compare_all_files(*file_paths)`: Compares IP addresses of multiple files and returns IP addresses common to all files as a set
- `compare_common_ips_across_files(*file_paths)` : Compares the IP addresses of several files and returns common IP addresses as a set, indicating in which files they were found

## Author

- Author: chpe1
- Date: 30/10/2023

<hr/>

# Script de Comparaison d'Adresses IP

Ce script Python a été conçu pour comparer les adresses IP dans plusieurs fichiers CSV et/ou TXT et identifier les adresses IP communes entre eux. Il extrait les adresses IP de ces fichiers et effectue la comparaison pour trouver les adresses IP partagées.
Une adresse IP par ligne.

## Utilisation

Pour utiliser ce script, fournissez les chemins d'un ou plusieurs fichiers CSV ou TXT contenant des adresses IP en tant qu'arguments en ligne de commande. Le script trouvera et affichera les adresses IP communes parmi les fichiers fournis.

Exemple :

```bash
$ python script.py file1.csv file2.txt
```

## Fonctions

- `csv_to_list(file)`: Extrait les adresses IP d'un fichier CSV et les renvoie sous forme d'ensemble.
- `txt_to_list(file)`: Extrait les adresses IP d'un fichier texte (TXT) et les renvoie sous forme d'ensemble.
- `load_ip_addresses_from_file(file_path)`: Charge les adresses IP depuis un fichier CSV ou TXT et les renvoie sous forme d'ensemble.
- `compare_all_files(*file_paths)`: Compare les adresses IP de plusieurs fichiers et renvoie les adresses IP communes à tous les fichiers sous forme d'ensemble.
- `compare_common_ips_across_files(*file_paths)`: Compare les adresses IP de plusieurs fichiers et renvoie les adresses IP communes sous forme d'ensemble en indiquant dans quels fichiers elles ont été trouvées.

## Auteur

- Auteur : chpe1
- Date : 30/10/2023
