# Data

This folder is git-ignored. Download **PPG-DaLiA** (Reiss et al., 2019) from the
UCI Machine Learning Repository and extract it here so the layout is:

```
data/PPG_FieldStudy/S1/S1.pkl
data/PPG_FieldStudy/S2/S2.pkl
...
data/PPG_FieldStudy/S15/S15.pkl
```

Signals used: wrist PPG (BVP, 64 Hz), wrist 3-axis accelerometer (32 Hz),
activity labels, and the ECG-derived reference HR (one value per 8 s window, 2 s shift).

Notes:
- Subject S6: only the first 90 minutes are valid.
- Exact pickle field names should be confirmed against the dataset readme.
