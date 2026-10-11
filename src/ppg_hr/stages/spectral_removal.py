"""Stage 2 (Step 6): SpaMa-style removal of PPG spectral peaks that match accelerometer peaks."""


def candidate_peaks(ppg_window, acc_window, k_ppg, k_acc, delta_hz):
    """Return PPG peaks (Hz, power) left after deleting those within delta_hz of an ACC peak."""
    raise NotImplementedError
