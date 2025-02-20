import telebot
import yt_dlp
import os
import subprocess

# Replace with your bot token from BotFather
BOT_TOKEN = "7699898366:AAF_TrWgkEx00HV5TF3eeamYSV4818XQWQA"

bot = telebot.TeleBot(BOT_TOKEN)

# Create downloads folder
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Function to download Instagram Reels
def download_instagram_reel(url):
    try:
        ydl_opts = {
            'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',
            'format': 'mp4',  # Force MP4 format
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        print("Downloaded file:", file_path)
        return file_path
    except Exception as e:
        print("Download error:", e)
        return None

# Function to compress videos if they exceed 50MB
def compress_video(input_path):
    output_path = f"{DOWNLOAD_DIR}/compressed.mp4"
    
    try:
        cmd = f"ffmpeg -i \"{input_path}\" -vcodec libx264 -crf 28 \"{output_path}\" -y"
        subprocess.run(cmd, shell=True, check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        print("Compression error:", e)
        return input_path  # Return original if compression fails

# Handling /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me an Instagram Reels link to download.")

# Handling Instagram Reels links
@bot.message_handler(func=lambda message: "instagram.com/reel/" in message.text)
def handle_reel_download(message):
    url = message.text
    bot.reply_to(message, "Downloading... Please wait.")

    file_path = download_instagram_reel(url)
    if not file_path:
        bot.reply_to(message, "Failed to download the video. Please try again.")
        return

    # Check file size and compress if necessary
    if os.path.exists(file_path) and os.path.getsize(file_path) > 50 * 1024 * 1024:
        bot.reply_to(message, "Video is too large. Compressing...")
        file_path = compress_video(file_path)

    # Send as video, fallback to document if Telegram fails to process it
    try:
        with open(file_path, 'rb') as video:
            bot.send_video(message.chat.id, video)
    except Exception:
        with open(file_path, 'rb') as video:
            bot.send_document(message.chat.id, video)

    # Delete file after sending to save space
    os.remove(file_path)

# Start the bot
bot.polling()
