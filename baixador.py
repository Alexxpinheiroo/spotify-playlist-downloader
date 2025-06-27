import os
import subprocess
import sys
import urllib.request
import zipfile
import shutil

def instalar_pacote(pacote):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

def instalar_spotdl():
    print("📦 Instalando spotdl...")
    instalar_pacote("spotdl")

def instalar_ffmpeg_windows():
    ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    ffmpeg_zip = "ffmpeg.zip"
    pasta_destino = os.path.join(os.getcwd(), "ffmpeg")

    if shutil.which("ffmpeg"):
        print("✅ FFmpeg já está instalado.")
        return

    print("⬇️ Baixando FFmpeg...")
    urllib.request.urlretrieve(ffmpeg_url, ffmpeg_zip)

    print("📂 Extraindo FFmpeg...")
    with zipfile.ZipFile(ffmpeg_zip, 'r') as zip_ref:
        zip_ref.extractall("ffmpeg_temp")

    extraida = os.listdir("ffmpeg_temp")[0]
    caminho_bin = os.path.abspath(os.path.join("ffmpeg_temp", extraida, "bin"))
    os.makedirs(pasta_destino, exist_ok=True)

    for arquivo in os.listdir(caminho_bin):
        shutil.copy(os.path.join(caminho_bin, arquivo), pasta_destino)

    # Adiciona ao PATH temporariamente (somente para esta sessão)
    os.environ["PATH"] += os.pathsep + pasta_destino

    print("🛠️ FFmpeg instalado e adicionado ao PATH.")

    os.remove(ffmpeg_zip)
    shutil.rmtree("ffmpeg_temp")

def baixar_playlist():
    print("\n🎵 Baixador de Playlists Spotify [Alta Qualidade]")
    link = input("🔗 Cole o link da sua playlist do Spotify: ").strip()

    if not link.startswith("https://open.spotify.com/playlist/"):
        print("❌ Link inválido.")
        return

    pasta_destino = "Spotify_Playlist"
    os.makedirs(pasta_destino, exist_ok=True)

    comando = f'spotdl download "{link}" --output "{pasta_destino}/%(artist)s - %(title)s.%(ext)s"'

    print(f"\n📥 Iniciando download na pasta '{pasta_destino}'...\n")
    
    try:
        subprocess.run(comando, shell=True, check=True)
        print("\n✅ Download concluído com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erro ao baixar: {e}")

if __name__ == "__main__":
    print("🚀 Iniciando instalação e configuração do ambiente...")

    instalar_spotdl()
    instalar_ffmpeg_windows()
    baixar_playlist()
