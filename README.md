# DiscordDMFormatter

DiscordDMFormatter is a Python script designed to clean and format Discord chat logs for easier reading and analysis. It's a perfect tool for those who want to archive their Discord conversations in a more readable and manageable format.

## Features

- Removes emojis from the text.
- Ignores system messages such as "Started a call", "Pinned a message", and link messages.
- Counts and reports the number of removed links, pinned messages, and call messages.
- Outputs the cleaned and formatted chat logs to a text file.

## Usage

To use DiscordDMFormatter, you first need to export your Discord chat logs AS A TXT. This can be done using the [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) tool.

Once you have your chat logs, simply run the DiscordDMFormatter script with the chat log file as input:

```bash
python DiscordDMFormatter.py chat_logs.txt
```
The script will create a new file, formatted_chat_logs.txt, containing the cleaned and formatted chat logs.

## Code Snippet 

Here's a brief look at the main logic of the DiscordDMFormatter:
```python
import re
import unicodedata

def remove_emojis(text):
    return ''.join(c for c in text if not unicodedata.category(c).startswith('So'))

with open('chat_logs.txt', 'r', encoding='utf-8') as f:
    logs = f.read()

# ... rest of the code ...

with open('formatted_chat_logs.txt', 'w', encoding='utf-8') as f:
    f.write(formatted_logs)
```

## Contribution

Feel free to fork this project, submit issues, or pull requests. Any contributions are warmly welcomed!

## License 

DiscordDMFormatter is open-source software licensed under the MIT license.

