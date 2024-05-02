# Wordle Bot

<p align="center">

</p>

Discord Bot for playing wordle. You can either add my bot (which will be generally running 24/7 outside of bug fixes) or add your own. 



## How to play

Wordle utilizes slash commands in discord to function. There are a few commands that you can use to play wordle.

* `/start`: Begins a Wordle game for the server in one of three modes:
  * `collab`, where you work together on a Wordle game
  * `custom`, where one person can provide a custom word for others to guess
  * `battle`, a multiplayer mode where multiple people compete on the same world at once.
* `/guess`: Make a guess for Wordle. Words must be real words.  
* `/letters`: Get a list of letters that you haven't guessed yet or are in the word.
* `/review`: Get a list of all your previous guesses.
* `/end`: Ends the game regardless of where it is at.

Battle Mode Specific Commands:

* `/join`: Joins an open battle party. Hosts do not need this, as they are automatically in the party.
* `/leave`: Leaves the currently joined battle party. Hosts cannot use this. 
* `/ready`: Ready up for the battle, closing the party and starting the game.

## Using my wordle bot (easy)

To add my bot, you can add it to your own discord server using [this link](https://discord.com/oauth2/authorize?client_id=1235714042585288834&permissions=8&scope=bot+applications.commands). It's running on a server 24/7 and periodically will be reset in case things break. Please file bug reports so I can fix them!

One thing to note is that the owner of the server will always see all private channels (this is a discord feature unfortunately), so this means the owner of the server should mute all notifications from the server temporarily to prevent guessees from being spoiled. 

## Setting up your own bot on discord 

You can also set up your own bot to run this script by creating a discord application and running this script with your bot token. Follow these steps for that:

1. Follow the steps [here](https://docs.pycord.dev/en/master/discord.html) to create your own bot. 
2. Grab your token from the discord application page and store it in a file called ```settings.py``` (mine is untracaked). For your own purposes, your file should look like this. 
  ```python
  MYTOKEN = ...
  ```
3. Clone this repo and setup with 
  ```bash
  git clone ...
  cd wordle-bot 
  conda env create -f env.yml 
  conda activate disc
  python run_bot.py
  ```

Note to use the following to install the correct version of pycord. 

```bash
pip install py-cord
```

## Future Features (currently in work)
* Statistics and tracking. Keep track of how well you do on average, and how many games you've played.
* Hints. When stuck, the bot will remove some of the letters that aren't in the final word for you. 

## Some screenshots
![testbot console](https://github.com/VAAADIM123/Discord-Wordi-Bot/assets/96568482/f04ab38d-3f86-447e-990f-6ddac71f747c)
![image](https://github.com/VAAADIM123/Discord-Wordi-Bot/assets/96568482/5111b5e6-6eb4-4567-9c8a-e168e8350c36)

