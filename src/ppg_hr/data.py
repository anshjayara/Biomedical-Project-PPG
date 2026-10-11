"""Step 1-2: load PPG-DaLiA subjects and cut aligned 8 s windows (2 s shift)."""


def load_subject(subject_id):
    """Return wrist PPG (64 Hz), wrist ACC (32 Hz), activity labels and reference HR for one subject."""
    raise NotImplementedError


def make_windows(subject):
    """Cut PPG/ACC into aligned windows with one reference HR, activity label and mixed-label flag each."""
    raise NotImplementedError
