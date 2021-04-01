# upsync-instabot

Automates instagram dms

NOTE: Does not handle error very well so follow carefully

Steps (Kinda annoying):

1. Install the relevant chromedriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
2. Install selenium (```pip3 install selenium``` on mac pretty sure)
3. Move it to the PATH (on mac/linux you can do ```sudo cp ~/Downloads/chromedriver /usr/local/bin```
4. Make your messages in a spreadsheet. Make the first column the instagram handle (if this is wrong it kind of breaks) and the second column the message.
5. Download the spreadsheet as a CSV file
6. Pull app.py and replace <username> and <password> with your insta user and pass where indicated.
7. Run app.py in the following format -> ```python3 app.py <file-path>```. Replace <file-path> with the file path of the CSV file you just downloaded.
8. It will open a browser and start sending messages. Kinda slow so go do something else while it runs.
9. Hopefully your messages sent!


