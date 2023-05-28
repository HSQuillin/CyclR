import tkinter as tk
from tkinter import filedialog
import random
from datetime import datetime
import os

# Version 1.0.1 - CyclR

# Arrays
genres = ["Rock", "Metal", "Jazz", "Rap", "Pop", "EDM", "Country", "Reggae", "Funk", "Disco", "Blues", "Ambient"]
instruments = ["Acoustic Guitar", "Organ", "Piano", "Bass Guitar", "Harpsichord", "Electric Guitar", "Trombone", "Synth Bass", "Synthpad", "Trumpet", "Flute", "Saxophone", "Violin", "Cello", "Banjo", "Harmonica", "Recorder", "Oboe", "Harp"]
tempos = range(60, 181)
time_signatures = ["2/4", "3/4", "4/4", "6/8", "9/8", "12/8"]
music_styles = [
    "The Beatles", "Michael Jackson", "Led Zeppelin", "Queen", "Bob Dylan", "Pink Floyd", "David Bowie", "Elvis Presley", "The Rolling Stones",
    "Nirvana", "Prince", "Madonna", "The Beach Boys", "Bob Marley", "U2", "Johnny Cash", "The Who", "AC/DC",
    "Jimi Hendrix", "The Eagles", "Bruce Springsteen", "Radiohead", "Stevie Wonder", "Metallica", "Elton John", "The Clash", "Pearl Jam",
    "Oasis", "Marvin Gaye", "Guns N' Roses", "The Smiths", "Fleetwood Mac", "Kendrick Lamar", "The Cure", "Aretha Franklin", "Bee Gees",
    "Frank Sinatra", "Outkast", "Pink", "Coldplay", "Eminem", "Beastie Boys", "R.E.M.", "Black Sabbath", "Jay-Z",
    "Queen Latifah", "Whitney Houston", "Red Hot Chili Peppers", "Radiohead", "Kanye West", "Simon & Garfunkel", "John Lennon", "Justin Timberlake", "Taylor Swift",
    "The Doors", "Bon Jovi", "Aerosmith", "Paul McCartney", "Eric Clapton", "Billy Joel", "Tina Turner", "Destiny's Child", "The Police",
    "Sade", "Mariah Carey", "The Bee Gees", "Blur", "Arctic Monkeys", "The Velvet Underground", "ABBA", "Johnny Cash", "Ed Sheeran",
    "Frank Ocean", "Foo Fighters", "Fleet Foxes", "Miles Davis", "Daft Punk", "Gorillaz", "Mumford & Sons", "Vampire Weekend", "The Weeknd",
    "Radiohead", "The Strokes", "Green Day", "The White Stripes", "Beastie Boys", "Kendrick Lamar", "Lana Del Rey", "Florence + The Machine", "Jack White",
    "Arcade Fire", "Adele", "Billie Eilish", "Childish Gambino", "Lorde", "Hozier", "Imagine Dragons", "Twenty One Pilots", "Sam Smith",
    "Panic! At The Disco"]
scales = ["C Major", "D Major", "E Major", "F Major", "G Major", "A Major", "B Major",
          "C# Major", "D# Major", "F# Major", "G# Major", "A# Major",
          "C Minor", "D Minor", "E Minor", "F Minor", "G Minor", "A Minor", "B Minor",
          "C# Minor", "D# Minor", "F# Minor", "G# Minor", "A# Minor"]

colors = {"genre": "#13262F", "instrument": "#583E23", "tempo": "#132E12", "time_signature": "#592424", "style": "#2E122D", "scale": "#FF4F79"}

def generate_genre():
    generate_genre_button.config(state=tk.DISABLED)
    generate_instrument_button.config(state=tk.DISABLED)
    generate_tempo_button.config(state=tk.DISABLED)
    generate_time_signature_button.config(state=tk.DISABLED)
    generate_style_button.config(state=tk.DISABLED)
    generate_scale_button.config(state=tk.DISABLED)

    for _ in range(25):
        genre = random.choice(genres)
        genre_label.config(text=genre, fg="white")
        genre_label.update()
        root.after(200)

    genre = random.choice(genres)
    genre_label.config(text=genre, fg="white", bg=colors["genre"])
    generate_genre_button.config(state=tk.NORMAL)
    generate_instrument_button.config(state=tk.NORMAL)

def generate_instrument():
    generate_instrument_button.config(state=tk.DISABLED)
    generate_tempo_button.config(state=tk.DISABLED)
    generate_time_signature_button.config(state=tk.DISABLED)
    generate_style_button.config(state=tk.DISABLED)
    generate_scale_button.config(state=tk.DISABLED)

    for _ in range(25):
        instrument = random.choice(instruments)
        instrument_label.config(text=instrument, fg="white", bg=colors["instrument"])
        instrument_label.update()
        root.after(200)

    instrument = random.choice(instruments)
    instrument_label.config(text=instrument, fg="white", bg=colors["instrument"])
    generate_instrument_button.config(state=tk.NORMAL)
    generate_tempo_button.config(state=tk.NORMAL)

def generate_tempo():
    generate_tempo_button.config(state=tk.DISABLED)
    generate_time_signature_button.config(state=tk.DISABLED)
    generate_style_button.config(state=tk.DISABLED)
    generate_scale_button.config(state=tk.DISABLED)

    for _ in range(25):
        tempo = random.choice(tempos)
        tempo_label.config(text=str(tempo) + " BPM", fg="white", bg=colors["tempo"])
        tempo_label.update()
        root.after(200)

    tempo = random.choice(tempos)
    tempo_label.config(text=str(tempo) + " BPM", fg="white", bg=colors["tempo"])
    generate_tempo_button.config(state=tk.NORMAL)
    generate_time_signature_button.config(state=tk.NORMAL)

def generate_time_signature():
    generate_time_signature_button.config(state=tk.DISABLED)
    generate_style_button.config(state=tk.DISABLED)
    generate_scale_button.config(state=tk.DISABLED)

    for _ in range(25):
        if random.random() < 0.5:
            time_signature = "4/4"
        else:
            time_signature = random.choice(time_signatures)
        time_signature_label.config(text=time_signature, fg="white", bg=colors["time_signature"])
        time_signature_label.update()
        root.after(200)

    if random.random() < 0.5:
        time_signature = "4/4"
    else:
        time_signature = random.choice(time_signatures)
    time_signature_label.config(text=time_signature, fg="white", bg=colors["time_signature"])
    generate_time_signature_button.config(state=tk.NORMAL)
    generate_style_button.config(state=tk.NORMAL)

def generate_style():
    generate_style_button.config(state=tk.DISABLED)
    generate_scale_button.config(state=tk.DISABLED)

    for _ in range(25):
        style = random.choice(music_styles)
        style_label.config(text=style, fg="white", bg=colors["style"])
        style_label.update()
        root.after(200)

    style = random.choice(music_styles)
    style_label.config(text=style, fg="white", bg=colors["style"])
    generate_style_button.config(state=tk.NORMAL)
    generate_scale_button.config(state=tk.NORMAL)

def generate_scale():
    generate_scale_button.config(state=tk.DISABLED)

    for _ in range(25):
        scale = random.choice(scales)
        scale_label.config(text=scale, fg="black", bg=colors["scale"])
        scale_label.update()
        root.after(200)

    scale = random.choice(scales)
    scale_label.config(text=scale, fg="black", bg=colors["scale"])
    generate_scale_button.config(state=tk.NORMAL)

def save_generation():
    genre = genre_label.cget("text")
    instrument = instrument_label.cget("text")
    tempo = tempo_label.cget("text")
    time_signature = time_signature_label.cget("text")
    style = style_label.cget("text")
    scale = scale_label.cget("text")

    default_file_name = f"CyclR - {datetime.now().strftime('%Y%m%d')} {genre}.txt"
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")], initialfile=default_file_name)
    if file_path:
        with open(file_path, "w") as file:
            file.write("Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            file.write(f"Genre: {genre}\n")
            file.write(f"Instrument: {instrument}\n")
            file.write(f"Tempo: {tempo}\n")
            file.write(f"Time Signature: {time_signature}\n")
            file.write(f"Style: {style}\n")
            file.write(f"Scale: {scale}\n")
        file_name = os.path.basename(file_path)
        print(f"Generation saved successfully: {file_name}")

root = tk.Tk()
root.title("CyclR - Music Creativity Generator")
root.geometry("500x600")

header_label = tk.Label(root, text="CyclR", font=("Arial", 40))
header_label.pack(pady=10)
def cycle_header_color():
    header_color = random.choice(list(colors.values()))
    header_label.configure(fg=header_color)
    root.after(1000, cycle_header_color)

cycle_header_color()

genre_label = tk.Label(root, text="Genre", font=("Arial", 20))
genre_label.config(fg="white", bg=colors["genre"])
genre_label.pack(pady=10)

generate_genre_button = tk.Button(root, text="Generate Genre", command=generate_genre)
generate_genre_button.config(bg=colors["genre"], fg="white")
generate_genre_button.pack()

instrument_label = tk.Label(root, text="Instrument", font=("Arial", 20))
instrument_label.config(fg="white", bg=colors["instrument"])
instrument_label.pack(pady=10)

generate_instrument_button = tk.Button(root, text="Generate Instrument", command=generate_instrument, state=tk.DISABLED)
generate_instrument_button.config(bg=colors["instrument"], fg="white")
generate_instrument_button.pack()

tempo_label = tk.Label(root, text="Tempo", font=("Arial", 20))
tempo_label.config(fg="white", bg=colors["tempo"])
tempo_label.pack(pady=10)

generate_tempo_button = tk.Button(root, text="Generate Tempo", command=generate_tempo, state=tk.DISABLED)
generate_tempo_button.config(bg=colors["tempo"], fg="white")
generate_tempo_button.pack()

time_signature_label = tk.Label(root, text="Time Signature", font=("Arial", 20))
time_signature_label.config(fg="white", bg=colors["time_signature"])
time_signature_label.pack(pady=10)

generate_time_signature_button = tk.Button(root, text="Generate Time Signature", command=generate_time_signature, state=tk.DISABLED)
generate_time_signature_button.config(bg=colors["time_signature"], fg="white")
generate_time_signature_button.pack()

style_label = tk.Label(root, text="Style", font=("Arial", 20))
style_label.config(fg="white", bg=colors["style"])
style_label.pack(pady=10)

generate_style_button = tk.Button(root, text="Generate Style", command=generate_style, state=tk.DISABLED)
generate_style_button.config(bg=colors["style"], fg="white")
generate_style_button.pack()

scale_label = tk.Label(root, text="Scale", font=("Arial", 20))
scale_label.config(fg="white", bg=colors["scale"])
scale_label.pack(pady=10)

generate_scale_button = tk.Button(root, text="Generate Scale", command=generate_scale, state=tk.DISABLED)
generate_scale_button.config(bg=colors["scale"], fg="white")
generate_scale_button.pack()

save_button = tk.Button(root, text="Save Generation", command=save_generation)
save_button.pack(pady=10)

root.mainloop()
