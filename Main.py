from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pytube import YouTube

# Replace with your bot token
BOT_TOKEN = "7939391364:AAFqi5QuudQtJGoBTYbnTHgqUu_Kd6UF5EY"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Send me a YouTube video link, and I'll download it for you!")

def download_video(update: Update, context: CallbackContext):
    url = update.message.text
    
    try:
        # Validate and download video
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()  # Get the highest resolution
        file_path = stream.download()

        # Send the video to the user
        update.message.reply_text("Downloading video...")
        with open(file_path, 'rb') as video:
            update.message.reply_video(video)

    except Exception as e:
        update.message.reply_text(f"Error: {e}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, download_video))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
