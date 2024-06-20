import os
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip
from pathlib import Path


def download_video(url, download_path="."):
    try:
        print(f"Baixando {url}...")
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        output_path = stream.download(output_path=download_path)
        print(f"Download completo: {yt.title}")
        return output_path
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")
        return None


def convert_to_mp3(video_path, output_path="."):
    try:
        audio_clip = AudioFileClip(video_path)
        audio_file = Path(output_path) / f"{Path(video_path).stem}.mp3"
        audio_clip.write_audiofile(audio_file, codec='libmp3lame')
        audio_clip.close()
        print(f"Conversão para MP3 completa: {audio_file}")
        os.remove(video_path)
        return audio_file
    except Exception as e:
        print(f"Erro na conversão para MP3: {e}")
        return None


if __name__ == "__main__":
    download_type = input(
        "Deseja baixar um vídeo ou uma playlist? (V/P): ").strip().lower()

    if download_type == "v":
        video_url = input("Digite o URL do vídeo que deseja baixar: ")
        convert_option = input(
            "Deseja converter o vídeo para MP3? (S/N): ").strip().lower()

        # Substitua com o caminho do diretório onde deseja salvar os vídeos
        download_path = "C:/Users/Rodolfo/Music"
        video_path = download_video(video_url, download_path)

        if video_path and convert_option == "s":
            convert_to_mp3(video_path, download_path)
        elif video_path:
            print(f"Vídeo baixado em: {video_path}")
        else:
            print("Erro ao baixar o vídeo.")

    elif download_type == "p":
        playlist_url = input("Digite o URL da playlist que deseja baixar: ")

        try:
            playlist = Playlist(playlist_url)
            # Verifica se a playlist tem vídeos
            if not playlist.video_urls:
                raise ValueError(
                    "A URL fornecida não contém uma playlist válida.")

            convert_option = input(
                "Deseja converter os vídeos para MP3? (S/N): ").strip().lower()

            # Substitua com o caminho do diretório onde deseja salvar os vídeos
            download_path = "C:/Users/Rodolfo/Music"

            for video_url in playlist.video_urls:
                video_path = download_video(video_url, download_path)

                if video_path and convert_option == "s":
                    convert_to_mp3(video_path, download_path)
                elif video_path:
                    print(f"Vídeo baixado em: {video_path}")
                else:
                    print(f"Erro ao baixar o vídeo: {video_url}")

        except Exception as e:
            print(
                f"Erro: {e}. Certifique-se de fornecer uma URL de playlist válida.")
    else:
        print("Opção de download inválida. Por favor, escolha entre 'vídeo' ou 'playlist'.")
