def bootstrap_replicate_1d(data, func):
    """ Generate bootstrap replicate of 1D data.
    :param data: bootstrap sample
    :param func: summary statistic function
    :return: bootstrap replicate
    """

    bs_sample = np.random.choice(data, len(data))

    return func(bs_sample)
