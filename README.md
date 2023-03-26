## PrankMeBot

*PrankMeBot* is a python based [*telegram*](https://telegram.org/) bot, which is meant for **pranking** people by spamming messages on the their 
telegram inbox. The idea for this project came to me during April Fool's day and utilizes several commonly used libraries, don't missue this program.
Have fun at your own *responsibility*!


### Language : [**Python**](https://python.org)

### Libraries Used : [telegram](https://python-telegram-bot.org/), [time](https://docs.python.org/3/library/time.html), [random](https://docs.python.org/3/library/random.html), [asyncio](https://docs.python.org/3/library/asyncio.html), [optparse](https://docs.python.org/3/library/optparse.html)

### Required Steps
- Before you use this program, you would need to install the required libraries as mentioned above and can be done using the following command:

```
pip3 install -r requirements.txt
```

- You would also need to obtain your *Bot Token* from BotFather and add it to the file **TOKEN.txt**. In order to get the token, follow the given steps:
  - Start a conversation with [*Bot-Father*](https://t.me/BotFather).
  - Create your new bot by typing the following text: **/newbot**
  - Follow the prompts provided by the bot and give it a name to your liking :)
  - You'll receive a token like so, which you can copy by double clicking on the token and then pasting it into the *TOKEN.txt* file.
  
 ``` 
Done! Congratulations on your new bot. You will find it at t.me/xxxxxBot. You can now add a description, about section and profile
picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support 
if you want a better username for it. Just make sure the bot is fully operational before you do this. Use this token to access the
HTTP API: 5449264661:xxxxxxxxxx-RkqiIpWRtuePV7NIMcU
Keep your token secure and store it safely, it can be used by anyone to control your bot.
For a description of the Bot API, see this page: https://core.telegram.org/bots/api
```

### Usage
```
python PrankeMeBot.py -c xxxxxxxxx -m Sample Message -s 25
```

### Documentation
It utilizes several libraries in order to acheive it's desired function. It utilizes the *optparse* library to parse the options provided by the user, the *time* library is used for setting intervals between each request. It also utilizes the *random* library to set time intervals ranging from 5 to 30 seconds **if** the time interval is *not provided* during execution, a word of caution don't set the time interval below *5* seconds. Last, but the most *important* library is *asyncio* which is used to send [*asynchronous requests*](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Synchronous_and_Asynchronous_Requests) to the Telegram API.
On execution it sends a request to the Telegram API and prints the information about the message sent and also about the receiving user.
In order to obtain the ID of the user on telegram, follow the following steps:
- Go to [*JsonDumpBot*](https://t.me/JsonDumpBot)
- Forward a message from the desired user to the bot.
- It will reply to your message with the information about the message forwaded, in JSON format. 
- The required ID can be found under *forward_from_chat* , like so:


```
   {...
    "forward_from_chat": {
          "id": xxxxxxxxx,
   ...}
```



This project is currently compatile only with Python 2, hope to add functionallity for Python 3 in the upcoming versions. The help menu can be obtained using the following command :
```
python PrankMeBot.py --help

Output:
Usage: PrankMeBot.py [options]

Options:
  -h, --help            show this help message and exit
  -c CHATID, --chatid=CHATID
                        [Required] Used to Enter Chat ID of the  receiving
                        user
  -m MESSAGE, --message=MESSAGE
                        [Required] Used to Enter the Message for the receiving
                        user
  -s SECS, --seconds=SECS
                        [Optional] zzUsed to Enter the Time Delay between the
                        Messages
If time is not specified, a random time interval
between 5 to 30 seconds would be selected between each request.
Example: python PrankeMeBot.py -c 000000000 -m Sample Message -s 25
```

### Credits
This project was based on the a repository by *@rcbonz*, check out his repository titled [Telegram-python-bot](https://github.com/rcbonz/Telegram-python-bot)

### Future Improvements
- HouseKeeping & Code Beautification
- Python3 Compatible, while maintaining cross-compatibility

