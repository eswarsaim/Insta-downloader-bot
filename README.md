🤖 Instagram Video Downloader Telegram Bot

A Python-based **Telegram Bot** that allows users to **download Instagram Reels** simply by sending the reel link to the bot.
If the video size exceeds **50MB**, it automatically compresses the video before sending it back to the user.

---

📌 Features

* Download **Instagram Reels** by just sharing the reel link
* Automatic **video compression** if file size > 50MB
* Sends the video directly in the Telegram chat
* Fallback: If Telegram fails to process, video is sent as a **document**
* Automatically deletes downloaded files after sending (saves storage)

---

🛠️ Technologies Used

* **Python 3**
* [pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI) – for Telegram Bot integration
* [yt-dlp](https://github.com/yt-dlp/yt-dlp) – for downloading Instagram Reels
* [FFmpeg](https://ffmpeg.org/) – for video compression

---

📂 Project Structure

```
instagram-downloader-bot/
│
├── bot.py            # Main bot script
├── downloads/        # Temporary download folder
└── README.md         # Project documentation
```

---

🚀 Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/instagram-downloader-bot.git
   cd instagram-downloader-bot
   ```

2. **Install dependencies**

   ```bash
   pip install pyTelegramBotAPI yt-dlp
   ```

3. **Install FFmpeg** (required for compression)

   * [Download FFmpeg](https://ffmpeg.org/download.html) and add it to your system PATH

4. **Add your Bot Token**

   * Open `bot.py`
   * Replace the `BOT_TOKEN` with your token from **BotFather**

   ```python
   BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
   ```

5. **Run the bot**

   ```bash
   python bot.py
   ```

---

📸 Usage

1. Start the bot on Telegram with `/start`.
2. Send any **Instagram Reel link** (e.g., `https://www.instagram.com/reel/xyz/`).
3. The bot will download the video and send it back to you.

---

📈 Future Improvements

* Support for Instagram **posts, stories, IGTV**
* Progress bar / download status messages
* Option to choose **video quality**
* Deploy on **Heroku / Docker / VPS** for 24/7 availability

---

🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repo
2. Create a feature branch (`feature-xyz`)
3. Commit changes
4. Submit a pull request

---

📜 License

This project is licensed under the **MIT License** – free to use and modify.
