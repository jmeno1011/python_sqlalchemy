from imblearn.over_sampling import ADASYN, RandomOverSampler


def overSampling_ADASYN(X, y):
    ada = ADASYN(random_state=0)
    X_res, y_res = ada.fit_resample(X, y)
    return X_res, y_res


def overSampling_Random(X, y):
    ros = RandomOverSampler(random_state=0)
    X_res, y_res = ros.fit_resample(X, y)
    return X_res, y_res
