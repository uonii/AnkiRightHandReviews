# Austin Hasten
# Initial Commit - January 13th, 2018

from aqt import mw
from aqt.reviewer import Reviewer

class RightHandReviewer(Reviewer):
    # Keep Python from complaining that self.shortcuts doesn't exist. 
    shortcuts = []

    def __init__(self, mw):
        super().__init__(mw)

        # Reviewer's default shortcuts, plus our own.
        self.shortcuts = super()._shortcutKeys() + [
            ("j", lambda: self._answerCard(1)),
            ("k", lambda: self._answerCard(2)),
            ("l", lambda: self._answerCard(3)),
            (";", lambda: self._answerCard(4)),
        ]

    def _shortcutKeys(self):
        """ Return our shortcuts rather than the default ones. """
        return self.shortcuts

    def _answerCard(self, ease):
        """
        Modified copy of aqt.Reviewer._answerCard.

        Allows cards to be answered without first showing the back.
        Also selects the nearest difficulty level to the users selection.
        """
        "Reschedule card and show next."
        if self.mw.state != "review":
            # showing resetRequired screen; ignore key
            return
#        if self.state != "answer":
#            return
#        if self.mw.col.sched.answerButtons(self.card) < ease:
#            return
        ease = min(ease, self.mw.col.sched.answerButtons(self.card))
        self.mw.col.sched.answerCard(self.card, ease)
        self._answeredIds.append(self.card.id)
        self.mw.autosave()
        self.nextCard()

# Use our modified Reviewer rather than the default one.
mw.reviewer = RightHandReviewer(mw)
