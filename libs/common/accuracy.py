def sensitivity(TP, FN):
    return TP / (TP + FN)


def specifity(TN, FP):
    return TN / (FP + TN)


def positive_predictive_value(TP, FP):
    return TP / (TP + FP)


def negative_predictive_value(TN, FN):
    return TN / (TN + FN)


def accuracy(TP, TN, FP, FN):
    return (TP + TN) / (TP + TN + FP + FN)
