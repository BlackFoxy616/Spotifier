import logging,os,time,csv

from telegram import __version__ as TG_VER
filec = open("links.csv","a+")
cwrite = csv.writer(filec)
cread = csv.reader(filec)

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")




async def d2l(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    fullcmd = update.message.text
    link = fullcmd.split()[1]
    if link.startswith("https") or link.startswith("http"):
        os.system("spotdl " + link)
        await update.message.reply_text("File been Downloaded!!!!")
        for name in os.listdir():
              if name.endswith(".mp3"):
                 rcl = "rclone --config './rclone.conf' move '"+name+"' Mirror:/Music/ "
                 os.system(rcl)
                 cwrite.writerow([link,name])
               
                  

    else:
       await update.message.reply_text("Link Not Vaild!!!!")




async def dl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    fullcmd = update.message.text
    link = fullcmd.split()[1]
    if link.startswith("https") or link.startswith("http"):
        os.system("spotdl download" + link)
        await update.message.reply_text("File been Downloaded!!!!")
        for name in os.listdir():
              if name.endswith(".mp3"): 
                if 
                await context.bot.sendDocument(update.effective_chat.id, document=open(name, 'rb'))
    else:
       await update.message.reply_text("Link Not Vaild!!!!")





async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    print(update.message.text)
    await update.message.reply_text("Fuck Off")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('The file is downloading')
    await context.bot.sendDocument(update.effective_chat.id, document=open('1.jpg', 'rb'))
 

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5703964169:AAEn_l-MSzjMwu9X9hPeyx0ZIjw4Qm0oIvY").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("dl", dl))
    application.add_handler(CommandHandler("send", download))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
