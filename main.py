import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Resampling-Filter festlegen (für Kompatibilität zwischen Pillow-Versionen)
if hasattr(Image, 'Resampling'):
    resample_filter = Image.Resampling.LANCZOS
else:
    resample_filter = Image.ANTIALIAS

# Suche nach .conf-Dateien im aktuellen Verzeichnis
conf_files = [f for f in os.listdir() if f.endswith(".conf")]
if not conf_files:
    print("Keine .conf-Dateien im aktuellen Verzeichnis gefunden.")
    exit(1)

print("Mehrere .conf-Dateien gefunden:")
for idx, file in enumerate(conf_files, start=1):
    print(f"[{idx}] {file}")
print("[0] Alle Dateien verarbeiten")

choice = input("Bitte gib die Nummer der gewünschten Datei ein oder 0 für alle: ")

# Falls alle Dateien verarbeitet werden sollen
if choice == "0":
    selected_files = conf_files
else:
    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(conf_files):
            print("Ungültige Eingabe.")
            exit(1)
        selected_files = [conf_files[idx]]
    except (ValueError, IndexError):
        print("Ungültige Eingabe.")
        exit(1)

# Funktion zur Erstellung des QR-Codes und der Bildverarbeitung
def create_qr_code_with_logo(config_file):
    print(f"Verarbeite: {config_file}")

    # Lese die Konfigurationsdaten ein
    with open(config_file, "r", encoding="utf-8") as f:
        config_data = f.read()

    # Erzeuge den QR-Code mit hohem Fehlerkorrektur-Level
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(config_data)
    qr.make(fit=True)
    # Erstelle ein RGBA-Bild: schwarze Datenpunkte, weißer Hintergrund
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    qr_w, qr_h = qr_img.size

    # Lade und skaliere das Logo
    logo_filename = "logo.png"
    if os.path.exists(logo_filename):
        logo = Image.open(logo_filename)
        if logo.mode != "RGBA":
            logo = logo.convert("RGBA")
        # Das Logo soll 1/4 der QR-Code-Breite einnehmen
        factor = 4
        logo_width = qr_w // factor
        orig_logo_w, orig_logo_h = logo.size
        aspect_ratio = orig_logo_h / orig_logo_w
        logo_height = int(logo_width * aspect_ratio)
        logo = logo.resize((logo_width, logo_height), resample_filter)
    else:
        logo = None
        logo_width = logo_height = 0

    # Text vorbereiten (Dateiname ohne Erweiterung) – wird in Weiß dargestellt
    text = os.path.splitext(os.path.basename(config_file))[0]
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 24)

    # Erstelle ein Dummy-Bild, um die Textgröße zu messen
    dummy_img = Image.new("RGB", (100, 100))
    draw_dummy = ImageDraw.Draw(dummy_img)
    bbox = draw_dummy.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Abstände definieren
    margin_between_qr_and_text = 70
    margin_between_text_and_logo = 20

    # Berechne die Dimensionen des finalen Bildes
    new_img_width = max(qr_w, logo_width, text_width)
    new_img_height = (
        qr_h
        + margin_between_qr_and_text
        + text_height
        + margin_between_text_and_logo
        + logo_height
    )

    # Erstelle das finale Bild im RGBA-Modus – zunächst mit weißem Hintergrund
    final_img = Image.new("RGBA", (new_img_width, new_img_height), (255, 255, 255, 255))

    # Füge den QR-Code oben zentriert ein
    qr_x = (new_img_width - qr_w) // 2
    final_img.paste(qr_img, (qr_x, 0), qr_img)

    # Fülle den unteren Bereich (ab QR-Code) mit grün
    draw = ImageDraw.Draw(final_img)
    green_area_top = qr_h
    green_area_bottom = new_img_height
    draw.rectangle([0, green_area_top, new_img_width, green_area_bottom], fill="#171a17")  # Dunkelgrün

    # Schreibe den Dateinamen in weiß oberhalb des Logos, zentriert
    text_x = (new_img_width - text_width) // 2
    text_y = qr_h + margin_between_qr_and_text
    draw.text((text_x, text_y), text, fill="#ffffff", font=font)  # Weißer Text

    # Füge das Logo unterhalb des Textes ein, zentriert
    if logo is not None:
        logo_x = (new_img_width - logo_width) // 2
        logo_y = text_y + text_height + margin_between_text_and_logo
        final_img.paste(logo, (logo_x, logo_y), logo)

    # Konvertiere in den RGB-Modus und speichere das Bild
    final_img = final_img.convert("RGB")
    output_file = os.path.splitext(config_file)[0] + ".png"
    final_img.save(output_file)
    print(f"QR-Code im unteren Bereich wurde erfolgreich unter '{output_file}' gespeichert.")

# Verarbeite alle ausgewählten Dateien
for config_file in selected_files:
    create_qr_code_with_logo(config_file)
