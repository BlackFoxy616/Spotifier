from pyrogram import Client, filters

app = Client("my_account")

async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

@app.on_message(filters.command("start"))
async def start_command(client, event):
    new_message_id = event.id
    channel_id = event.chat.id
    await app.send_document(channel_id, "hello.py",caption="document caption", progress=progress)


app.run()  # Automatically start() and idle()