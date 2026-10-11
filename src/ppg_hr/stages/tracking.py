"""Stage 3 (Step 7): HR tracking with prediction, closest-peak selection, jump limiting and reset."""


class HRTracker:
    def __init__(self, history=6, max_jump=10, widen_after=3, reset_diff=10, reset_consecutive=3):
        raise NotImplementedError

    def update(self, candidates):
        """Pick the candidate closest to the prediction and return the tracked HR and the rule that fired."""
        raise NotImplementedError
