# Telegram-Search-and-Record
The code is a script that performs a keyword search on the text of all messages in Telegram chats and groups, using the Telethon library. The search keywords are read from a "keywords.txt" file. The search results are then written to a CSV file "search_results.csv", including the username, message text, date, and the keyword that triggered the search result. The code uses asynchronous programming to perform multiple operations concurrently, improving efficiency and performance. The script connects to the Telegram API using the provided API ID and hash, and iterates through all chats to search for the keywords. Any exceptions that occur during the execution of the script are handled and printed.

# Compleate Explaination

This Python script uses the Telethon library to search for specific keywords in messages across all Telegram channels that the user has joined. The script requires an API ID and API hash to authenticate the user's Telegram account with the Telegram API.

The script reads in a list of keywords from a text file, removes newline characters from the list of keywords, and opens a CSV file to write the search results. The script then gets all the chats that the user has joined and iterates through them. For each chat that is a channel, the script gets the 100 most recent messages in the chat and iterates through them to check if any of the keywords are in the message text. If a keyword is found, the script writes the username, message text, date, link, and keyword to the CSV file.

The script uses a progress bar from the tqdm library to show the progress of iterating through the chats. The script also handles any exceptions that occur while searching for the keywords and prints the traceback to the console.

To use this script, the user must first obtain an API ID and API hash by creating a new application in the Telegram API website. The user must also install the required Python libraries: Telethon, tqdm, and csv. The user must then create a text file called 'keywords.txt' containing a list of keywords to search for, with each keyword on a separate line. Finally, the user can run the script, and the search results will be written to a CSV file called 'search_results.csv'.
