# Obqd

Obqd is a program, written in Python, used to automatically reserve lunch every week

## Function

Here I will explain how the program currently works:

First, the program creates a new driver for the browser selected in the settings.

It then logs in the account given by the user and goes to the menus for the week.

It proceeds to go to each day of the week individually and select a menu according to the users' preferences.

Then it submits and finishes the program.

## Settings

The program provides a lot of ways to customise its function.

All of the settings can be found in the settings folder of the installation directory.

### Menu

This setting can be modified in the menu.json file.

It's a json object that tells the program how many of each item to order.

So for example, if you want 2 desserts, you will set the dessert property to 2 instead of 1.

```json
{
    "tarator": 1,
    "salad": 0,
    "main": 1,
    "grill": 0,
    "dessert": 1,
    "bread": 2
}
```

### Preferences

This setting can be modified in the preferences.txt file.

It's like an array where you need to move the meals you like best higher.

And you can tell the program to entirely remove meals by putting an X at the end of the line.

For example, if I prefer "Боб с наденица" to "Мусака", I will move it up higher.
And if I don't want to ever see "Вегетарианска мусака" in the menu, I will mark it with an X.

```txt
Боб с наденица
Мусака
Вегетарианска мусака X
```

### Settings

This setting can be modified in the settings.json file.

It has only 2 options. Which browser to use and if it should use grill for backup.

The program currently supports Chrome and Firefox and we don't plan on updating it,
so you better use these 2 browsers.

If the program tries to order you a main meal, but both of the meals are marked with an X,
it will go to the 'grill_backup' setting.
What it does, is that it replaces the main meal with that amount of grill.

So if you have the setting at 3, it will order 3 grill in the case that both main meals are marked with X.

```json
{
    "browser": "chrome",
    "grill_backup": 3
}
```

## Account

When you first start the program, it will require you to enter your email and password for the account
you're planning to use.

Once you enter them, they will be saved in a file called account.json.

## Usage

### Release

Go to the [latest release]("https://github.com/GGGeorgiev20/obqd/releases/latest")
and download it.

Extract the contents of the zip folder.

Navigate to the installation directory and run the file in the terminal:
```bash
./obqd.exe
```

### Your version

In case you want to modify the program and use it the way you like it,
you will first need to clone the repository:

```bash
git clone https://github.com/GGGeorgiev20/obqd.git
```

Then you need to install the requirements:

```bash
pip install -r requirements.txt
```

Modify the program and then run it:

```bash
python main.py
```

And you're good to go!

## Authors

- [NVDespotov20](https://github.com/NVDespotov20)
- [GGGeorgiev](https://github.com/GGGeorgiev20)