import numpy as np

def mapFeature(x1, x2, degree=6):

    if x1.ndim > 0:
        out = [np.ones(x1.shape[0])]
    else:
        out = [np.ones(1)]

    for i in range(1, degree + 1):
        for j in range(i + 1):
            out.append((x1 ** (i - j)) * (x2 ** j))

    if x1.ndim > 0:
        return np.stack(out, axis=1)
    else:
        return np.array(out)