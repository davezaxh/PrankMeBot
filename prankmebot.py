import telegram, time, random
import asyncio, optparse

# Option Parsing
parser = optparse.OptionParser()
optparse.OptionParser.format_epilog = lambda self, formatter: self.epilog
parser = optparse.OptionParser(epilog="If time is not specified, a random time interval \nbetween 5 to 30 seconds would be selected between each request.\nExample: python PrankeMeBot.py -c xxxxxxxxx -m Test Message -s 25")
parser.add_option("-c", "--chatid", dest="chatid", help="[Required] Used to Enter Chat ID of the  receiving user")
parser.add_option("-m", "--message", dest="message", help="[Required] Used to Enter the Message for the receiving user")
parser.add_option("-s", "--seconds", dest="secs", help="[Optional] Used to Enter the Time Delay between the Messages")
(options,arguments) = parser.parse_args()

# Asynchronous function to send telegram messages
async def prank(secs):
    token = open("TOKEN.txt", "r").read()
    def sendTelegMes(message, token, chat_id):
            sent = False
            retry_c = 0
            while sent == False:
                try:
                    bot = telegram.Bot(token=token, request=telegram.utils.request.Request(connect_timeout=20, read_timeout=20))
                    sent = bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN, timeout=20)
                except Exception as err:
                    if retry_c > 4:
                        print('[-] Telegram attempts exceeded!\n[-] Message not sent.')
                        break
                    elif str(err) == 'Unauthorized':
                        print('[-] Invalid Telegram bot token!\n[-] Message not sent.')
                        break
                    elif str(err) == 'Timed out':
                        retry_c += 1
                        print(f'[-] Telegram timeout count: {str(retry_c)}')
                        pass
                    elif str(err) == 'Chat not found':
                        print('[-] Invalid Telegram Chat ID!\n[-] Message not sent.')
                        break
                    else:
                        print(f'[-] Unexpected error: {str(err)}!\n[-] Message not sent.')
                        break
                else:
                    print("[+] Telegram message sent successfully!.")
                    print("[+] Message Information:")
                    print("Text: "+str(sent["text"]))
                    print("Date & Time: "+str(sent["date"]))
                    print("Message ID: "+str(sent["message_id"]))
                    print("Username: "+str(sent["chat"]["username"]))
                    print("Name: "+str(sent["chat"]["first_name"]))
                    print("Message ID: "+str(sent["chat"]["id"]))

    print("\n[+] Sending message...")
    sendTelegMes(options.message, token, options.chatid)
    print("[+] Done!")
    print(f"[+] Time till next message: {secs} secs")
    time.sleep(secs)

try:
    while True:
        if __name__ == "__main__":
            loop = asyncio.get_event_loop()
            if not options.chatid:
                print("[+] Please specify the ID of the user!")
                break
            else:
                if not options.message:
                    print("[+] Please specify the message to be sent!")
                    break
                else:
                    if not options.secs:
                        secs = random.randint(5,25)
                        loop.run_until_complete(prank(int(secs)))
                    else:
                        secs = options.secs
                        loop.run_until_complete(prank(int(secs)))
except KeyboardInterrupt:
    print("[-] CTRL + C Detected....\n[-] Quiting...")


