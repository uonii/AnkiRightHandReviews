# Saul Femm
# Initial Commit - January 13th, 2018

from aqt import mw
from aqt.reviewer import Reviewer

class RightHandReviewer(Reviewer):
    def __init__(self, mw):
        super().__init__(mw)

        # Copy Reviewer's default shortcuts.
        self.shortcuts = self._shortcutKeys()

        # Add our own shortcuts to the default ones.
        self.shortcuts += [
            ("j", lambda: self._answerCard(1)),
            ("k", lambda: self._answerCard(2)),
            ("l", lambda: self._answerCard(3)),
            (";", lambda: self._answerCard(4)),
        ]

        # Replace default methods with our own.
        self._shortcutKeys = self._shortcutKeysNew
        self._answerCard = self._answerCardNew

    def _shortcutKeysNew(self):
        """ Return our shortcuts rather than the default ones. """
        return self.shortcuts

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

# Use our modified Reviewer rather than the default one.
mw.reviewer = RightHandReviewer(mw)
