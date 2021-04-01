# upsync-instabot

Automates instagram dms

NOTE: Does not handle error very well so follow carefully

Steps (Kinda annoying):

1. Install the relevant chromedriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
2. Move it to the PATH (on mac/linux you can do ```sudo cp ~/Downloads/chromedriver /usr/local/bin```
3. Make your messages in a spreadsheet. Make the first column the instagram handle (if this is wrong it kind of breaks) and the second column the message.
4. Download the spreadsheet as a CSV file
5. Run app.py in the following format -> ```python3 app.py <file-path>```. Replace <file-path> with the file path of the CSV file you just downloaded.
6. It will open a browser and start sending messages. Kinda slow so go do something else while it runs.
7. Hopefully your messages sent!


