"""Step 3: band-pass the continuous signals, split AC/DC/noise, z-normalise windows."""


def bandpass(signal, fs, band, order=4):
    """Zero-phase Butterworth band-pass (offline)."""
    raise NotImplementedError


def ac_dc_noise(signal, fs):
    """Split PPG into AC (0.75-4 Hz), DC (0.1 Hz low-pass) and noise (10 Hz high-pass) components."""
    raise NotImplementedError


def znorm(window):
    """Subtract the window mean and divide by its standard deviation."""
    raise NotImplementedError
