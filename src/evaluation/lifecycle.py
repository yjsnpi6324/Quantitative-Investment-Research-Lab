"""Model lifecycle decision skeleton."""


def lifecycle_decision(health_score, challenger_pass=False):
    if challenger_pass and health_score < 0.6:
        return "DOWNGRADE_REVIEW"
    if health_score < 0.5:
        return "WATCH"
    return "HEALTHY"
