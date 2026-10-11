"""Step 10: leave-one-subject-out evaluation, metrics and cumulative ablation."""


def mae(hr_est, hr_ref):
    raise NotImplementedError


def bland_altman(hr_est, hr_ref):
    """Return mean difference and limits of agreement (mean +/- 1.96 SD)."""
    raise NotImplementedError


def run_loso(pipeline, subjects):
    """Tune on 14 subjects, test on the held-out one, for every subject."""
    raise NotImplementedError
