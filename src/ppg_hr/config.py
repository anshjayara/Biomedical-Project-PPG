"""Constants shared by every stage. Values and their sources are explained in docs/project_plan.md."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "PPG_FieldStudy"
SUBJECTS = [f"S{i}" for i in range(1, 16)]

# Sampling rates (Hz) [1]
FS_PPG = 64
FS_ACC = 32
FS_ECG = 700

# Windowing (Step 2) [1], [2]
WINDOW_S = 8
SHIFT_S = 2

# Zero-padded FFT lengths: both give 64/4096 = 32/2048 ~ 0.0156 Hz (~0.94 BPM) per bin
NFFT_PPG = 4096
NFFT_ACC = 2048

# Pre-processing (Step 3)
BANDPASS_HZ = (0.5, 4.0)
FILTER_ORDER = 4
DC_LOWPASS_HZ = 0.1  # [6]
NOISE_HIGHPASS_HZ = 10.0  # [6]
AC_BAND_HZ = (0.75, 4.0)  # for perfusion index / AC SNR [6]

# HR search band (Step 4): 40-200 BPM covers the dataset's 41-187 BPM
HR_SEARCH_BPM = (40, 200)

# Tracking (Step 7); jump and reset thresholds are starting values, tuned per LOSO fold
TRACK_HISTORY = 6  # [1]
MAX_JUMP_BPM = 10  # [2]
NO_PEAK_WIDEN_AFTER = 3  # [2]
RESET_DIFF_BPM = 10  # [1]
RESET_CONSECUTIVE = 3  # [1]

# Quality gating (Step 8) [4]; threshold is a starting value, re-tuned on training subjects
PR_TOTAL_BAND_HZ = (0.5, 5.0)
PR_CARDIAC_BAND_HZ = (0.5, 2.5)
PR_THRESHOLD = 0.592
