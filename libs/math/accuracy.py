class Accuracy:

    @staticmethod
    def Sensitivity(TP, FN):
        return TP/ (TP + FN)

    @staticmethod
    def Specifity (TN, FP):
        return TN / (FP + TN)

    @staticmethod
    def Positive_Predictive_Value(TP, FP):
        return TP / (TP + FP)

    @staticmethod
    def Negative_Predictive_Value(TN, FN):
        return TN / (TN + FN)

    @staticmethod
    def Accuracy (TP, TN, FP, FN):
        return (TP + TN ) / (TP + TN + FP + FN)

    