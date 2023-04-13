from pytube import YouTube

# URL de la vidéo YouTube à télécharger
url = "https://www.youtube.com/watch?v=VIDEO_ID"

# Créer une instance de la classe YouTube avec l'URL de la vidéo
yt = YouTube(url)

# Afficher les informations de la vidéo
print("Titre : ", yt.title)
print("Auteur : ", yt.author)
print("Durée : ", yt.length, "secondes")
print("Description : ", yt.description)

# Télécharger la meilleure qualité vidéo disponible
yt.streams.get_highest_resolution().download()

print("Téléchargement terminé!")
