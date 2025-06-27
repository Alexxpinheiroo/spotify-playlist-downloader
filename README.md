# spotify-playlist-downloader
Script Python para baixar playlists inteiras do Spotify em formato MP3 de alta qualidade usando spotdl e FFmpeg. Automatiza a configuração do ambiente e o download das músicas com metadados e capa do álbum.

# Spotify Playlist Downloader

Um script em Python para baixar playlists inteiras do Spotify em alta qualidade (MP3 320kbps) usando o [spotdl](https://github.com/spotDL/spotify-downloader) e FFmpeg.

---

## Funcionalidades

- Baixa todas as músicas de uma playlist do Spotify com um único comando.
- Baixa arquivos em alta qualidade, com metadados completos (artista, título, álbum, capa).
- Automatiza a instalação do spotdl e do FFmpeg (Windows).
- Organiza os arquivos baixados em uma pasta dedicada.
- Fácil de usar, basta informar o link da playlist.

---

## Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes Python)
- FFmpeg (o script automatiza a instalação no Windows, mas em outros sistemas pode ser necessário instalar manualmente)

---

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/spotify-playlist-downloader.git
   cd spotify-playlist-downloader
