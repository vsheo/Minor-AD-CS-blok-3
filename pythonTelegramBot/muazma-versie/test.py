import cv2
import sounddevice as sd
from scipy.io.wavfile import write
# Webcam
# https://www.geeksforgeeks.org/python/how-to-capture-a-image-from-webcam-in-python/
# https://opencv.org/reading-and-writing-videos-using-opencv/ 
# https://pynput.readthedocs.io/en/latest/keyboard.html
# https://docs.python-telegram-bot.org/en/v21.5/telegram.ext.commandhandler.html
# Viresh https://github.com/vsheo/Minor-AD-CS-blok-3/blob/main/pythonTelegramBot/atoms.py
# Viresh https://github.com/vsheo/Minor-AD-CS-blok-3/blob/main/pythonTelegramBot/atoms.py

# Initialize webcam (0 = default camera)
cam = cv2.VideoCapture(0)

# Capture one frame
ret, frame = cam.read()

if ret:
    cv2.imshow("Captured", frame)         
    cv2.imwrite("captured_image.png", frame)       
    cv2.destroyWindow("Captured")       
else:
    print("Failed to capture image.")

cam.release()

#Microfoon
async def microphone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fs = 44100  # Sample rate
    seconds = 5  # Opname duur

    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write("recording.wav", fs, recording)

    await context.bot.send_audio(
        chat_id=update.effective_chat.id,
        audio=open("recording.wav", "rb"))