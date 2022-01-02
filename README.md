# TwitchConnect
A python desktop application that allows users to look up a select few statistics about a specified streamer.

This codebase was built using python-twitch-client (https://python-twitch-client.readthedocs.io/en/latest/helix.html) which is a Python wrapper for the Twitch API.
The GUI was created with the tkinter library (https://docs.python.org/3/library/tkinter.html). If you would like to use this program, please follow this guide to setup your developer application (https://dev.twitch.tv/docs/api/) for OAuth and client id/secret.

Some various other statistical methods are located in the twitchapi.py file that are not included in the GUI.

This desktop application was created with Python 3.9.6. Run the GUI by opening the window.py file.

# Main Menu
![image](https://user-images.githubusercontent.com/63007329/147889183-2737e6f9-d225-4f80-84dc-a67d58490879.png)

# Ninja Example
![image](https://user-images.githubusercontent.com/63007329/147889191-d23605d3-4ef1-47d9-b7af-44339759c8de.png)

- The hyperlinks are clickable and will load the link via your default browser.
- The go back button will take the user to the main menu
- The top 5 games update every time the main menu is refreshed
