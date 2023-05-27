# Deezer To Mp3

Installation en [Français].

Installation in English.


# French

Ce projet est un simple script Python qui vous permet de télécharger des listes de lecture et des albums au format MP3 en utilisant leur identifiant unique. Il utilise l'API de Deezer pour rechercher et récupérer les fichiers audio correspondants.

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir les éléments suivants :

- Python 3 installé sur votre machine.
- Les paquets Python requis, qui peuvent être installés en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

Vous aurez également besoin de FFMPEG.exe dans le dossier DTM, que vous pouvez télécharger depuis [here](https://ffmpeg.org).

## Utilisation

1. Clonez ou téléchargez ce dépôt sur votre machine.

2. Naviguez vers le répertoire du projet :

```bash
cd DTM
```

3. Exécutez le script Python à l'aide de la commande suivante :

```bash
python main.py
```

Le script recherche toutes les musiques d'un album ou d'une liste de lecture donné(e) en fonction de l'identifiant fourni, puis recherche la musique correspondante sur Youtube et télécharge le fichier MP3 dans le répertoire de sortie spécifié.

## Notes supplémentaires

- Veillez à disposer d'une connexion internet active pour que le script puisse accéder à l'API du service de musique en ligne.
- Le script ne garantit pas la disponibilité ou la validité de l'identifiant musical fourni. Veillez à utiliser des identifiants musicaux corrects pour obtenir les résultats souhaités.
- N'oubliez pas de respecter les droits d'auteur et les conditions d'utilisation des fichiers musicaux téléchargés. Ce script est destiné à un usage personnel et ne doit pas être utilisé pour violer les droits d'auteur ou distribuer illégalement des fichiers musicaux.

## Auteurs

Ce script a été développé par Valox et est disponible sous la licence MIT. N'hésitez pas à contribuer, à signaler des problèmes ou à suggérer des améliorations en créant un problème ou en soumettant une demande d'extraction.

## Remerciements

Nous tenons à remercier les développeurs et les contributeurs de tous les paquets open-source utilisés dans ce projet. Votre travail est grandement apprécié.


# English

This project is a simple Python script that allows you to download playlist and album in MP3 format using its unique identifier. It utilizes the API of Deezer to search for and retrieve the corresponding audio files.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3 installed on your machine.
- Required Python packages, which can be installed by running the following command:

```bash
pip install -r requirements.txt
```

You will also need FFMPEG.exe in the DTM folder, which you can download from [here](https://ffmpeg.org).

## Usage

1. Clone or download this repository to your machine.

2. Navigate to the project directory:

```bash
cd DTM
```

3. Run the Python script using the following command:

```bash
python main.py
```

The script searches for all the music on a given album or playlist according to the ID supplied, then searches for the corresponding music on Youtube and downloads the MP3 file into the specified output directory.

## Additional Notes

- Ensure that you have an active internet connection for the script to access the online music service's API.
- The script does not guarantee the availability or validity of the provided music ID. Make sure to use correct music IDs to obtain the desired results.
- Remember to respect copyright and the terms of use for downloaded music files. This script is intended for personal use and should not be used to violate copyright or illegally distribute music files.

## Authors

This script was developed by Valox and is available under the MIT license. Feel free to contribute, report issues, or suggest improvements by creating an issue or submitting a pull request.

## Acknowledgments

We would like to thank the developers and contributors of all the open-source packages used in this project. Your work is greatly appreciated.
