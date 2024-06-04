import tkinter as tk
from pytube import YouTube

def download_video():
    link = link_entry.get()
    try:
        youtube = YouTube(link)
        video = youtube.streams.get_highest_resolution()
        video.download()
        status_label.config(text="Download do vídeo concluído com sucesso!", fg="green")
    except Exception as e:
        status_label.config(text="Erro ao baixar o vídeo: " + str(e), fg="red")

def download_music():
    link = link_entry.get()
    try:
        youtube = YouTube(link)
        audio = youtube.streams.get_audio_only()
        audio.download()
        status_label.config(text="Download da música concluído com sucesso!", fg="green")
    except Exception as e:
        status_label.config(text="Erro ao baixar a música: " + str(e), fg="red")

# Configuração da janela
window = tk.Tk()
window.title("Downloader")
window.geometry("400x200")
window.configure(bg="black")

# Coração como detalhe visual
heart_label = tk.Label(window, text="❤", font=("Arial", 20), fg="red", bg="black")
heart_label.pack(pady=10)

# Rótulo e campo de entrada para o link
link_label = tk.Label(window, text="Link:", fg="white", bg="black")
link_label.pack()
link_entry = tk.Entry(window, width=40)
link_entry.pack()

# Botões para baixar vídeo e música
video_button = tk.Button(window, text="Baixar Vídeo", command=download_video, bg="red", fg="white")
video_button.pack(pady=10)
music_button = tk.Button(window, text="Baixar Música", command=download_music, bg="red", fg="white")
music_button.pack()

# Rótulo para exibir o status do download
status_label = tk.Label(window, text="", fg="white", bg="black")
status_label.pack()

# Iniciar a janela
window.mainloop()
