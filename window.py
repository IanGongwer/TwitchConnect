import twitchapi
import webbrowser
import tkinter as tk

def createStatsWindow():

    # Initalize user input and labels
    username = str(entry1.get())
    errorblank = tk.Label(root, text="Username is blank")
    error = tk.Label(root, text="User does not exist")

    # Creates the stats window
    if entry1.get() != "" and twitchapi.get_id(username) != "User does not exist":
        # Shows the stats menu and hides the main menu
        canvas1.pack_forget()
        stats = tk.Canvas(root, width = 400, height = 300)
        stats.pack()

        # Title Text
        nametext = tk.Label(root, text=username.capitalize() + "'s Stats")
        stats.create_window(200, 80, window=nametext)

        # Twitch Id
        id = tk.Label(root, text="Twitch Id: " + twitchapi.get_id(username))
        stats.create_window(200, 100, window=id)

        # Most Popular Clip
        cliptext = tk.Label(root, text="Most Popular Clip: ")
        stats.create_window(140, 120, window=cliptext)
        clip = tk.Label(root, text=twitchapi.get_clips(username, 1)[0][:20] + "...", foreground="blue")
        clip.bind("<Button-1>", lambda e:webbrowser.open(twitchapi.get_clips(username, 1)[0]))
        stats.create_window(245, 120, window=clip)

        # Most Recent Video
        videotext = tk.Label(root, text="Most Recent Video: ")
        stats.create_window(138, 140, window=videotext)

        if twitchapi.get_videos(username, 1) != None:
            video = tk.Label(root, text=twitchapi.get_videos(username, 1)[0][:20] + "...", foreground="blue")
            video.bind("<Button-1>", lambda e:webbrowser.open(twitchapi.get_videos(username, 1)[0]))
            stats.create_window(250, 140, window=video)
        else:
            video = tk.Label(root, text="No recent video")
            stats.create_window(233, 140, window=video)

        #Go Back Button
        goback = tk.Button(text='Go Back', command=lambda:[mainWindow(), stats.destroy()])
        stats.create_window(40, 280, window=goback)

    # Error handling for blank input
    if entry1.get() == "":
        canvas1.create_window(80, 210, window=errorblank)

    # Error handling for nonexistent user
    if entry1.get() != "" and twitchapi.get_id(username) == "User does not exist":
        canvas1.create_window(80, 210, window=error)

# Re-shows the main menu and hides the stats menu
def mainWindow():
    canvas1.pack()

# Creation of main window with title
root= tk.Tk()
root.title("TwitchConnect")

# Makes windows 400x300
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

# Creates the label and button on screen
entrytext = tk.Label(root, text="Enter in a twitch username:")
canvas1.create_window(80, 120, window=entrytext)
entry1 = tk.Entry(root) 
canvas1.create_window(80, 140, window=entry1)
button1 = tk.Button(text='Search User', command=createStatsWindow)
canvas1.create_window(80, 180, window=button1)

# Creates the top 5 games sidebar
top_games = twitchapi.get_top_games(5)
gametext = tk.Label(root, text="Top 5 Games Currently")
canvas1.create_window(325, 100, window=gametext)
game1 = tk.Label(root, text=top_games[0])
canvas1.create_window(325, 120, window=game1)
game2 = tk.Label(root, text=top_games[1])
canvas1.create_window(325, 140, window=game2)
game3 = tk.Label(root, text=top_games[2])
canvas1.create_window(325, 160, window=game3)
game4 = tk.Label(root, text=top_games[3])
canvas1.create_window(325, 180, window=game4)
game5 = tk.Label(root, text=top_games[4])
canvas1.create_window(325, 200, window=game5)

# Disables window resizing and opens the window
root.resizable(False, False)
root.mainloop()