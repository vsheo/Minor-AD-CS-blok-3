from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
→ Nodig om een Telegram bot te maken.

import cv2
→ Voor de webcam (foto maken).

import sounddevice as sd
from scipy.io.wavfile import write
→ Voor microfoon opname.

import mss
import mss.tools
→ Voor screenshots maken.

🔹 2. Bot instellingen
API_TOKEN = "..."
BOT_HANDLE = '@Mumu1222322Bot'
API_TOKEN = unieke sleutel van je bot (verbinding met Telegram).

BOT_HANDLE = naam van je bot.

Belangrijk: je token moet je eigenlijk geheim houden.

🔹 3. /help command
async def opties(...)
Wanneer iemand /help typt:
→ De bot stuurt een lijst met beschikbare commands terug.

🔹 4. /start command
async def banner(...)
Als iemand /start typt:
→ Stuurt de bot een ASCII-banner terug.

🔹 5. /cam command (webcam)
async def webcam(...)
Wat gebeurt hier:

Open webcam (cv2.VideoCapture(0))

Maak 1 foto

Sla op als captured_image.png

Stuur die foto naar Telegram

Sluit webcam

🔹 6. /mic command (microfoon)
async def microfoon(...)
Wat gebeurt hier:

Neemt 5 seconden audio op

Slaat het op als recording.wav

Stuurt het audiobestand naar Telegram


🔹 8. /ss command (screenshot)
async def screenshot(...)
Wat gebeurt hier:

Maakt screenshot van je scherm

Slaat op als screenshot.png

Stuurt afbeelding naar Telegram

🔹 9. Bot starten
if __name__ == '__main__':
Dit betekent:
→ Alleen uitvoeren als je het script direct start.

Dan:

app = Application.builder().token(API_TOKEN).build()
→ Maakt de bot.

Daarna:

app.add_handler(...)
→ Verbindt elk command aan zijn functie.

En:

app.run_polling()
→ De bot blijft constant checken of er nieuwe berichten zijn.

