import imaplib
import email
import asyncio
import pickle

def load_and_update_language_choice():
    try:
        with open('lang.pkl', 'rb') as f:
            lang_data = pickle.load(f)
    except FileNotFoundError:
        print("Language file (lang.pkl) not found!")
        exit()

    if lang_data['choice'] == 'null':
        selected_lang = input(f"{lang_data['en']['language_prompt']}\nSeçiminiz / Your Choice: ").strip()

        if selected_lang == '1':
            lang_data['choice'] = 'tr'
            print('Dil başarıyla seçildi!')
        elif selected_lang == '2':
            lang_data['choice'] = 'en'
            print('Language successfully selected!')
        else:
            print("Invalid choice, defaulting to English.")
            lang_data['choice'] = 'en'

        with open('lang.pkl', 'wb') as f:
            pickle.dump(lang_data, f)

    return lang_data[lang_data['choice']]

lang = load_and_update_language_choice()

async def connect_to_email(imap_server, email_address, password):
    loop = asyncio.get_event_loop()
    imap = await loop.run_in_executor(None, lambda: imaplib.IMAP4_SSL(imap_server))
    await loop.run_in_executor(None, lambda: imap.login(email_address, password))
    return imap

async def search_emails(imap, folder, criteria):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, lambda: imap.select(folder))
    _, msgnums = await loop.run_in_executor(None, lambda: imap.search(None, criteria))
    return msgnums[0].split()

async def fetch_email_body(imap, msgnum):
    loop = asyncio.get_event_loop()
    _, data = await loop.run_in_executor(None, lambda: imap.fetch(msgnum, "(RFC822)"))
    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if "text/plain" in content_type or "text/html" in content_type:
                        return part.get_payload(decode=True).decode()
            else:
                return msg.get_payload(decode=True).decode()
    return None

async def print_last_email(imap_server, email_address, password):
    imap = await connect_to_email(imap_server, email_address, password)
    
    folders = ["Junk", "Inbox"]
    last_email_body = None
    
    for folder in folders:
        msgnums = await search_emails(imap, folder, 'FROM "no-reply@news.yemeksepeti.com"')
        
        if msgnums:
            last_msgnum = msgnums[-1]  # Son e-postayı al
            body = await fetch_email_body(imap, last_msgnum)
            if body:
                last_email_body = body
    
    imap.close()
    imap.logout()
    
    if last_email_body:
        print(f"{lang['lastmail'].replace('acc',email_address)}")
        print(last_email_body)
        print("-" * 50)

async def main():
    imap_server = "outlook.office365.com"
    
    with open("mails.txt", "r") as file:
        lines = file.readlines()
    
    tasks = []
    for line in lines:
        email_address, password = line.strip().split(":")
        tasks.append(print_last_email(imap_server, email_address, password))
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
