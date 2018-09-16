def Sensitivity(TP, FN):
    return TP / (TP + FN)


def Specifity(TN, FP):
    return TN / (FP + TN)


def Positive_Predictive_Value(TP, FP):
    return TP / (TP + FP)


def Negative_Predictive_Value(TN, FN):
    return TN / (TN + FN)


def Accuracy(TP, TN, FP, FN):
    return (TP + TN) / (TP + TN + FP + FN)
