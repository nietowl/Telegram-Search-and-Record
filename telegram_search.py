from telethon import TelegramClient
from telethon.tl.types import Channel, Megagroup
from tqdm import tqdm
import csv
import asyncio

# Use your own api_id and api_hash
api_id = "Enetr your api_id"
api_hash = 'Enter your api_hash'

async def run():
    # Connect to Telegram using Telethon
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.start()

        # Open the keywords file
        with open('keywords.txt', 'r') as f:
            keywords = f.readlines()

        # Remove the newline characters from the keywords
        keywords = [k.strip() for k in keywords]

        # Open a CSV file to write the search results
        with open('search_results.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Message', 'Date', 'Link', 'Keyword'])

            # Get all the chats
            chats = await client.get_dialogs()

            # Use a progress bar to show the progress
            for chat in tqdm(chats):
                try:
                    if isinstance(chat.entity, Channel) or isinstance(chat.entity, Megagroup):
                        # Get all the messages in the chat
                        messages = await client.get_messages(chat, limit=100)

                        # Iterate through the messages
                        for message in messages:
                            # Check if any of the keywords are in the message text
                            for keyword in keywords:
                                if keyword in message.message:
                                    # Write the username, message text, date, link and keyword to the CSV file
                                    writer.writerow([message.from_id, message.message, message.date, f'https://t.me/{chat.entity.username}', keyword])
                except Exception as e:
                    # Handle any exceptions that occur
                    print(f"Error: {e}")


asyncio.run(run())
