import re
import unicodedata

def remove_emojis(text):
    return ''.join(c for c in text if not unicodedata.category(c).startswith('So'))

with open('chat_logs.txt', 'r', encoding='utf-8') as f:
    logs = f.read()

messages = re.split(r'\[\d{2}/\d{2}/\d{4} \d{1,2}:\d{2} (AM|PM)\]', logs)

formatted_messages = []

link_count = 0
pinned_count = 0
call_count = 0
for message in messages[1:]:  #skip first line
    lines = message.strip().split('\n')
    speaker = lines[0]
    text_lines = lines[1:]
    speaker = re.sub(r' \(pinned\)', '', speaker)
    cleaned_text_lines = []

    skip_message = False

    for line in text_lines:
        if "Started a call" in line:
            skip_message = True
            call_count += 1
        elif "http" in line or "https" in line:
            skip_message = True
            link_count += 1
        elif "Pinned a message" in line:
            skip_message = True
            pinned_count += 1
        if re.search(r'={62,}', line):
            skip_message = True
        if skip_message:
            break

        line = remove_emojis(line)

        cleaned_text_lines.append(line)

    if skip_message or not any(line.strip() for line in cleaned_text_lines):
        continue

    text = '\n'.join(cleaned_text_lines)

    formatted_messages.append(f'{speaker}: {text}')

formatted_logs = '\n'.join(formatted_messages)

formatted_logs += f'\n\n\nLinks removed: {link_count}\nPinned messages removed: {pinned_count}\nCall messages removed: {call_count}'

with open('formatted_chat_logs.txt', 'w', encoding='utf-8') as f:
    f.write(formatted_logs)
