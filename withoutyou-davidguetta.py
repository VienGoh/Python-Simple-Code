import time
from colorama import init, Fore, Style

# Inisialisasi colorama
init(autoreset=True)

# Lirik lagu dengan timing (dalam detik)
lyrics_with_timing = [
    (0.0, "I can't win, I can't reign"),
    (3.9, "I will never win this game"),
    (7.1, "Without you, without you"),
    (14.5, "I am lost, I am vain"),
    (18.0, "I will never be the same"),
    (22.0, "Without you, without you"),
    (29.5, "I won't run, I won't fly"),
    (33.0, "I will never make it by"),
    (37.0, "Without you, without you"),
    (44.5, "I can't rest, I can't fight"),
    (48.5, "All I need is you and I"),
    (52.2, "Without you, without you"),
    # Tambahkan baris lirik lainnya dengan timing yang tepat
]

def print_lyrics():
    start_time = time.time()
    last_lyric = ""
    
    print(Fore.CYAN + "Lirik 'Without You' oleh David Guetta:")
    print(Fore.YELLOW + "(Mulai memutar lagu sekarang)")
    print(Fore.GREEN + "---------------------------------------")

    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    color_index = 0

    while True:
        current_time = time.time() - start_time
        current_lyric = ""

        for timing, lyric in lyrics_with_timing:
            if current_time >= timing:
                current_lyric = lyric
            else:
                break

        if current_lyric != last_lyric:
            print(f"{Fore.WHITE}{current_time:.2f}: {colors[color_index]}{current_lyric}")
            last_lyric = current_lyric
            color_index = (color_index + 1) % len(colors)

        if current_time > lyrics_with_timing[-1][0] + 5:  # Berhenti 5 detik setelah lirik terakhir
            break

        time.sleep(0.1)  # Cek setiap 0.1 detik

print_lyrics()
