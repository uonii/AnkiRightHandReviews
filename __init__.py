# Saul Femm
# Initial Commit - January 13th, 2018

from aqt import mw
from aqt.qt import *
import copy

def _answerCardNew(self, ease):
        """
        Modified copy of aqt.Reviewer._answerCard.

        Allows cards to be answered without first showing the back.
        """
        "Reschedule card and show next."
        if self.mw.state != "review":
            # showing resetRequired screen; ignore key
            return
#        if self.state != "answer":
#            return
        if self.mw.col.sched.answerButtons(self.card) < ease:
            return
        self.mw.col.sched.answerCard(self.card, ease)
        self._answeredIds.append(self.card.id)
        self.mw.autosave()
        self.nextCard()

# Copy main window's Reviewer member
r = copy.copy(mw.reviewer)

# Copy Reviewer's default shortcuts
r.shortcuts = mw.reviewer._shortcutKeys()

# Add our own shortcuts to the default ones
r.shortcuts += [
    ("j", lambda: r._answerCard(r, 1)),
    ("k", lambda: r._answerCard(r, 2)),
    ("l", lambda: r._answerCard(r, 3)),
    (";", lambda: r._answerCard(r, 4)),
]

# Return our shortcuts rather than the default ones.
r._shortcutKeys = lambda: r.shortcuts

# Use our modified _answerCard method to bypass showing the card's back.
r._answerCard = _answerCardNew

# Use our modified Reviewer rather than the default one.
mw.reviewer = r
