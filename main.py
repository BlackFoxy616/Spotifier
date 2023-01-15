import logging,os,time,csv
from sub import *
from telegram import __version__ as TG_VER


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



async def dl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    link = update.message.text
    if link[4:].startswith("https") or link.startswith("http"):
          if "spotify" in link[4:]:
             ytlink = ytsq(link[4:])
             ytdl(ytlink[1])
             for name in os.listdir():
               if ytlink[0] in name: 
                await context.bot.sendAudio(update.effective_chat.id, audio=open(name, 'rb'))
                write(link[4:],name)
                rclone(name)
                #os.system("rm '"+name+"'")
          else:
                 info =  dytdl(link[4:])
                 for name in os.listdir():
                     if info[0] in name:
                      #await context.bot.sendVideo(update.effective_chat.id, video=open(name, 'rb'))
                      write(link[4:],name)
                      rclonev(name)
                     
             

    else:
           await update.message.reply_text("Link Not Vaild!!!!")







async def srh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
      query = update.message.text
      caption = ytsn(query[7:])[2]
      photo =ytsn(query[7:])[3]
      await context.bot.sendPhoto(update.effective_chat.id,photo=photo, caption=caption)
      ytdl(ytsn(query[7:])[1])
      for name in os.listdir():
         if ytsn(query[7:])[0] in name:
            await context.bot.sendAudio(update.effective_chat.id, audio=open(name, 'rb'),performer="Spidy")
            write(ytsn(query[7:])[1],name)
            rclone(name)





async def url(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        link = update.message.text[8:]
        print('Added Playlist...',link)
        pwrite(link)


async def uppl(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
     for link in pread():
        getplay(link[0])
     await update.message.reply_text('Updated Playlist..')
         
     



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    print(update.message.text)
    await update.message.reply_text("Please Use The Command's")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5703964169:AAEn_l-MSzjMwu9X9hPeyx0ZIjw4Qm0oIvY").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("dl", dl))
    application.add_handler(CommandHandler("search", srh))
    application.add_handler(CommandHandler("update", uppl))
    application.add_handler(CommandHandler("addurl", url))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
