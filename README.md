<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0a0a,60:0d1f0d,100:1a4a1a&height=200&section=header&text=Sorry%20Discord&fontSize=70&fontColor=4ade80&fontAlignY=55&animation=fadeIn" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.7+-3572A5?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows%20Only-555555?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/Exypson/SorryDiscord)
[![Discord](https://img.shields.io/badge/Discord-Game%20Spoofer-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com)
[![License](https://img.shields.io/badge/License-GPL%20v3-c0392b?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](./LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0-4ade80?style=for-the-badge&logo=semanticrelease&logoColor=white)](https://github.com/Exypson/SorryDiscord/releases)

[Get Started](#installation) &nbsp;·&nbsp; [How it works](#how-it-works) &nbsp;·&nbsp; [Steam Mode](#steam-quest-mode) &nbsp;·&nbsp; [Usage](#usage) &nbsp;·&nbsp; [Structure](#project-structure) &nbsp;·&nbsp; [Legal](#legal-notice)

</div>

<br/>

## What is this

**Sorry Discord** is a lightweight Windows utility that tricks Discord into thinking you're playing quest games—without actually downloading them. It queries Discord's official public API to find the exact executable filename the quest looks for, makes a copy of a dummy binary, renames it, and runs it silently in the background. When Discord checks your system's active task list, it finds the matching process name and counts your quest progress.

It does not touch your Discord client files, inject DLLs into memory, or spam servers with fake web requests. It simply runs a lightweight program with the expected process name, which is all Discord looks at.

> **Educational purposes only.** This project was built to explore how Discord's game detection works under the hood and demonstrate basic process spoofing concepts. Please use this responsibly and follow Discord's Terms of Service.

<br/>

## Steam Quest Mode

Certain quests have an extra layer of verification. For these titles, Discord doesn't just check your running processes—it also looks for proof that Steam has registered or started downloading the game. Basic process renaming fails here, but Steam Quest Mode solves this problem.

### How it works

Just type the game's title into the built-in search. The program grabs the game's configuration details from the public SteamCMD database (such as its installation directory, executable path, and depot numbers) and pulls your logged-in Steam ID directly from the Windows Registry. Next, it writes a mock `appmanifest_<appid>.acf` file inside your real `steamapps/` folder with genuine download flags (`StateFlags 1026`, your `LastOwner` ID, staged depots, and byte counts). Then, it drops the dummy executable right into `steamapps/common/<game>/`. When Discord inspects the folder, it sees both the Steam download manifest and the running process, fulfilling the quest requirements. Everything gets removed cleanly when the timer ends.

**Supported:**
`Any title needing a Steam manifest` &nbsp; `Fully automated AppID retrieval` &nbsp; `Automatically detects your personal Steam ID` &nbsp; `Distinguishes between demos and base games` &nbsp; `Automatic file cleanup when finished`

> **Quick Tip:** If a quest asks for a demo version, be sure to type `"Toxic Commando Demo"` instead of just `"Toxic Commando"`. Each version has its own distinct AppID, and Discord requires the exact match to register progress.

<br/>

## Features

**Automatic Game Lookup** retrieves Discord's up-to-date detectable titles directly from their servers. The built-in search supports common shorthands and acronyms like CSGO, LoL, or PUBG, launching tasks quietly in the background.

**Self-Contained Timer & Embedded Settings** generates renamed binaries that launch straight into a clean countdown GUI if opened, carrying their timer limits and cleanup settings right inside the executable payload without opening messy terminal windows.

**Automatic Cleanup (`AUTO_DELETE`)** kicks off a background script once the countdown timer hits zero to delete the cloned executables, helper scripts, generated Steam manifests, and any empty folders left behind.

**Parallel Questing (Multi-Game)** lets you run several dummy games at the same time to finish multiple orb quests together. Pick a game, return to the menu, pick the next one, and let Discord detect all of them concurrently in a single 15-minute sitting.

**Built-in Fallback Mirror** automatically switches over to an archived GitHub mirror if Discord's live API goes down or blocks requests, ensuring uninterrupted access.

**Manual Override Mode** lets you enter any custom executable name by hand if you need to simulate a game that isn't listed in the database.

**Polished Terminal Interface** includes clear ANSI color-coding and animated status spinners so you always know what the script is doing.

## Requirements

Python 3.7 or newer, Windows operating system. An active internet connection to download the game lists. Discord needs to be running in the background, since the spoofer works by letting Discord scan your active processes.

<br/>

## Installation

```bash
git clone https://github.com/Exypson/SorryDiscord.git
cd SorryDiscord
pip install -r requirements.txt
```

## Usage

```bash
python sorrydiscord.py
```

Or via the package entry point:

```bash
python -m sorrydiscord
```

### Menu options

`1` Search Discord database by name or abbreviation

`2` Manual mode, enter a custom executable name

`3` Steam special quest mode

`4` Credits and project info

`5` Exit

### Completing all quests in 15 minutes

Open the application and choose your first target game. Once the process is active in the background, hit Enter to return to the main menu. Pick another game and repeat the steps for any other quests you have. You do not need to open multiple command prompts—every fake process runs side by side, and Discord tracks all of them at once. Wait for the 15-minute timer to wrap up, then exit.

<br/>

## Configuration

User-friendly options can be found in `settings.py` at the project's root folder. This file is read when the app boots up and overrides the defaults in `sorrydiscord/config.py`. You can adjust things like output directories and timer lengths there. The version number is tied directly to Git release tags and is handled automatically, so changing it manually is not recommended.

<br/>

## Auto-updater

Whenever a new version tag is pushed to GitHub, GitHub Actions runs PyInstaller to compile an all-in-one Windows `.exe` and uploads it to GitHub Releases. When you start the tool, it checks whether a newer build is available online. If it finds an update, it downloads the fresh binary, swaps it into place, and restarts on its own—meaning you don't even need Python installed to use the standalone build.

<br/>

## Legal Notice

**Educational purposes only. No commercial use.**

This software is shared purely for educational research into Windows process management and how Discord's game detection algorithms function. Commercial distribution, sale, or monetization of any kind is strictly prohibited.

You are entirely responsible for adhering to applicable local laws and Discord's Terms of Service. The developer does not encourage misuse and is not liable for any account actions, penalties, or damages resulting from using this software. This project comes with no warranties. Use it at your own discretion.

Misusing this software may violate Discord's Terms of Service.

<br/>

## License

GPL v3. Attribution is required. Any forks or modified versions must remain open-source under GPL v3, and the source code must be made available. Commercial use is not allowed. Check the [LICENSE](./LICENSE) file for full legal terms.
