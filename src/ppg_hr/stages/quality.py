"""Stage 4 (Step 8): signal quality indicators and gating."""


def power_ratio(ppg_window, fs, cardiac_band=(0.5, 2.5), total_band=(0.5, 5.0)):
    """Welch power in the cardiac band divided by power in the total band [4]."""
    raise NotImplementedError


def perfusion_index(ac, dc):
    """PI = AC_rms / DC_mean x 100 [6]."""
    raise NotImplementedError


def ac_snr_db(ac, noise):
    """AC SNR = 20 log10(AC_rms / noise_rms) [6]."""
    raise NotImplementedError
