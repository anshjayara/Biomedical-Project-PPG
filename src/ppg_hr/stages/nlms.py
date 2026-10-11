"""Stage 1 (Step 5): NLMS adaptive noise cancellation with the accelerometer as motion reference.

e(n) = d(n) - w.x(n);  w <- w + mu * e(n) * x(n) / (eps + |x(n)|^2)
Treated as an experiment: it is kept only if it lowers LOSO error.
"""


def nlms_filter(ppg, reference, mu, length, eps=1e-6):
    raise NotImplementedError
