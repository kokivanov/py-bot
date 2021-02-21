
# Testing python bot

## [EN]

### Features

| **Feature**               | **Status**         |
| ------------------------- | ------------------ |
| Config class              | **In progress...** |
| Sending nudes             | :white_check_mark: |
| Clear command             | :white_check_mark: |
| Pong-message and reaction | :white_check_mark: |
| Random command            | :white_check_mark: |
| Ping check                | :white_check_mark: |

---

### Commands

*NOTE:*

> Arguments given in this table in triangle brackets (like that: `<a>`) means that they are unnecessary, on the other hand arguments specified in sqare brackets (like that: `[a]`) **must** be specified

| Command                                   | Description                                                                                  | Arguments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Usage example (with default prefix)                                             |
| ----------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| ping                                      | Pong! Reruns bot's ping. No arguments required.                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `a-ping`                                                                        |
| random                                    | Generates random number in range, less than or from `<a>` to `<b>` depending on arguments.   | `random` `<a> <b>`, where **a** - minimum if specified along with **b**, or maximum if specified alone, **b** - maximum, generates number between **0 and 10 by default** if no arguments                                                                                                                                                                                                                                                                                                                                                                                                                         | `a-random 12 13`                                                                |
| dice, roll                                | Generates specified (2 if no arguments) amount of numbers in range from 1 to 6 (inclusively) | `dice <a> <b>`, where **a** - amount of numbers (dices), will count sum if more than 4 dices, **b** - is maximum possible value at every dice, will **roll 2 dices with maximum number of 6 by default** if no arguments                                                                                                                                                                                                                                                                                                                                                                                          | `a-dice 6 12`                                                                   |
| clear, purge                              | **Requires administrator permissions**, deletes last specified amount messages               | `clear <a>`, where **a** - amount of messages to delete, will **delete 10 messages by default** if no arguments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `a-purge 125`                                                                   |
| say, sudo                                 | **Requires administrator permissions**, repeats message specified amount of times            | `say <a> [msg]`, where **a** - amount of messages to send, **b** - message content (must be specified in **"** or **'** for more correct work)                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `a-say 3 "Your awesome message"` or `a-sudo "Your another awesome message!" 5`  |
| sendnudes, r34, porn, jerk, hentai, media | Sends post from Reddit or Danbooru depending on settings and arguments                       | `a-r34 <flag, request> <flag, request> <flag, request>` - can accept **flag** or **request** in any order, where **flag** is option that makes your requset more concrete (available flags: **-s** - safe search, no nsfw; **-d** - look at Danbooru.com, notice that in this case you have to provide search request as same as you would at Danbooru.com site; **-r** - look for your request at Reddit among subreddits; **-a** - look for your request at Reddit among redditors), **request** - option that represents what you want to look for. **Will look in standard list by default if no arguments.** | `a-r34 filo`, `a-hentai genshin_impact -d`, `a-media -s`, `a-r34 -a dkozinn -s` |

---

## To do

- [ ] Leveling
- [ ] RP
  - [ ] fishing
  - [ ] dungeons
  - [ ] monsters
  - [ ] classes
  - [ ] abilities (mb custom)
  - [ ] fighting
  - [ ] inventory
- [ ] Useful utils
  - [ ] Kick, ban, tempban, tempmute, mute
  - [X] Clear
  - [ ] Logs
  - [ ] Chat filter
  - [ ] Rolereact
  - [ ] Reminders
  - [ ] Announces
- [ ] Entertainment
  - [ ] Different reactions for each one command
  - [ ] Images
  - [ ] Memes
  - [ ] Videos
  - [ ] Gifs
  - [ ] Count days till...
- [ ] Gaming
  - [ ] Overwatch
  - [ ] Osu
  - [ ] Hearthstone
  - [ ] League of legends
  - [ ] CS:GO
  - [ ] GTA
- [ ] Calendar
- [ ] Custom settings for each server
- [ ] UI/UX
  - [ ] Help page
  - [ ] Dashboard
  - [ ] Adminpannel
- [X] **Sending nudes**
