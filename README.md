# Clash Royale Automation Bot

## Table of Contents
1. [Introdution](#introduction)
2. [Features](#features)
3. [Dependencies](#dependencies)
4. [Installation](#installation)
5. [How to Use](#how-to-use)
6. [Credits](#credits)

## Introduction
This is a Clash Royale Automation script that can play, exit matches, and queue into matches (Use at your own risk, this bot breaks Supercell TOS). The scripts now target macOS with an iPhone mirrored to your Mac (QuickTime Player device window or the new macOS “iPhone Mirroring” window).

## Features
- Plays Clash Royale without user input
- Code is highly customizable, user can create functions for any card
- Has a preset golem nightwitch deck to test out
- Collects and opens chests

## Dependencies
* Python
   * Version: 3.12.4
   * Description: Python is the programming language used to develop this script.
* macOS Screen + Input Access
   * Description: Mirror your iPhone screen to macOS (QuickTime Player device window or macOS “iPhone Mirroring”). Keep the mirrored window centered on your primary monitor and **do not resize it while the bot runs**.
* OpenCV
   * Version: 4.10.0.84
   * Image Recognition to detect cards.
* MSS
   * Version: 9.0.1
   * Screenshot Module
* NumPy
   * Version: 1.26.3
   * Array computation
* PyAutoGUI
   * Version: 0.9.54
   * Cross-platform mouse control used on macOS.
* Pillow
   * Version: 10.4.0
   * Required by PyAutoGUI image/screenshot helpers.
* Keyboard
   * Version: 0.13.5
   * Press 'q' to shutdown script.

## Installation (macOS + iPhone mirroring)
1. Install Git (macOS)
   ```sh
   xcode-select --install
   git --version
   ```
2. Clone the repository:
   ```sh
   git clone https://github.com/JustinT301/golembot1.0.git
   cd golembot1.0
   ```
3. Install Python dependencies:
   ```sh
   python3 -m pip install -r requirements.txt
   ```
4. Grant permissions:
   * System Settings → Privacy & Security → Screen Recording: allow Terminal (or your editor) so the bot can read the mirrored window.
   * System Settings → Privacy & Security → Accessibility: allow Terminal (or your editor) so the bot can control the mouse.
   * The `keyboard` library may need Accessibility access too; if it cannot listen for `q`, run with sudo after granting access.

5. Prepare iPhone mirroring:
   * Connect your iPhone with a cable and open **QuickTime Player → New Movie Recording → select your iPhone as the camera**, or use the macOS “iPhone Mirroring” app.
   * Place the mirrored window on your primary display and keep its size fixed. The provided coordinates assume the window is roughly centered; adjust in `cards.py` and `cr_ui.py` if you position/size it differently.

6. Run the Clash Royale Automation bot code:
   ```sh
   python3 play.py
   ```
## How to Use
1. Mirror your iPhone to macOS (QuickTime Player device window or macOS “iPhone Mirroring”). Keep the window centered on your main display and do not resize it after calibrating coordinates.
2. Calibrate coordinates:
   * Run `python3 coordinates.py` to read live pixel positions while hovering the mouse over HUD elements.
   * Update the regions in `cr_ui.py` (`battle_button_region`, `ok_button_region`, `elixir10_region`) and `cards.py` (`deck_area`, drop coordinates inside each method) to match your mirrored window placement.
3. There is a preset golem deck (golem, nightwitch, edrag, babydrag, lumberjack, knight, bats, skeletons/evo skellies). If you need other cards, drop their images into `golemdeck/` and follow the patterns in `cards.py`.
4. Start the bot:
   ```sh
   python3 play.py
   ```
   Press `q` to exit.

## Credits
* Developed by:
   * Justin Turbyfill
* Edited by:
   * Rakshith Jayakarthikeyan
     
* Date: August 15th, 2024
