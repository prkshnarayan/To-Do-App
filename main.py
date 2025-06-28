import tkinter.messagebox
from tkinter import *
import random
from timeit import default_timer as timer

# List of random words
word_list = ['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure',
'bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords',
'caliph','cobweb','cockiness','croquet','crypt','curacao','cycle',
'daiquiri','dirndl','disavow','dizzying','duplex','dwarves',
'embezzle','equip','espionage','euouae','exodus',
'faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny',
'gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess',
'haiku','haphazard','hyphen',
'iatrogenic','icebox','injury','ivory','ivy',
'jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo',
'kayak','kazoo','keyhole','khaki','kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack',
'larynx','lengths','lucky','luxury','lymph',
'marquis','matrix','megahertz','microwave','mnemonic','mystify',
'naphtha','nightclub','nowadays','numbskull','nymph',
'onyx','ovary','oxidize','oxygen',
'pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','pshaw','psyche','puppy','puzzling',
'quartz','queue','quips','quixotic','quiz','quizzes','quorum',
'razzmatazz','rhubarb','rhythm','rickshaw',
'schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch','stronghold','stymied','subway','swivel','syndrome',
'thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths',
'unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism',
'walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern',
'xylophone',
'yachtsman','yippee','yoked','youthful','yummy',
'zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie']

# Theme colors and fonts
TITLE_FONT = "Arial"
TITLE = "#00ADB5"
WORD_FONT = "Times New Roman"
WORD = "#EEEEEE"
BACKGROUND = "#222831"

# Global variables
RANDOM_WORD = random.choice(word_list)
WORDS_TYPED = 0
START_TIME = None
TIME_LIMIT = 30  # seconds

def change_word():
    """Go to the next word"""
    global RANDOM_WORD
    RANDOM_WORD = random.choice(word_list)
    text_entry.delete(0, END)
    word_label.config(text=f"{RANDOM_WORD}", bg=BACKGROUND)

def callback(sv):
    """Check user input and calculate result"""
    global RANDOM_WORD, WORDS_TYPED, START_TIME

    typed_text = sv.get()

    # Start timer on first keystroke
    if START_TIME is None:
        START_TIME = timer()

    # Calculate elapsed time
    elapsed = timer() - START_TIME
    if elapsed >= TIME_LIMIT:
        wpm = (WORDS_TYPED / 5) / (elapsed / 60)
        tkinter.messagebox.showinfo("Results", f"Time's up!\nYour typing speed is {wpm:.2f} WPM.")
        root.destroy()
        return

    # If word is typed correctly
    if typed_text == RANDOM_WORD:
        WORDS_TYPED += len(RANDOM_WORD)
        change_word()
    elif typed_text:
        for i in range(len(typed_text)):
            if i >= len(RANDOM_WORD) or typed_text[i] != RANDOM_WORD[i]:
                word_label.config(bg="Red")
                break
        else:
            word_label.config(bg=BACKGROUND)

# Setup GUI
root = Tk()
root.title('Typing Test')
root.config(padx=25, pady=25, bg=BACKGROUND)
root.geometry("750x500")

# Title label
title_label = Label(text="Typing Test", font=(TITLE_FONT, 54, "bold"), fg=TITLE, bg=BACKGROUND)
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Word display label
word_label = Label(text=f"{RANDOM_WORD}", font=(WORD_FONT, 44), fg=WORD, bg=BACKGROUND)
word_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Entry field with real-time tracking
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
text_entry = Entry(root, width=15, font=(WORD_FONT, 24), textvariable=sv)
text_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
text_entry.focus()

# Run the app
root.mainloop()
