# coding: utf-8


FILTER_DOUBLES = filter_doubles = lambda lst: list(set(lst))


def LOCATE(source, dist, itm):
    return dist[source.index(itm)] if itm in source else None


def FIND(source, dist, itm):
    return [dist[i] for i in [i for i in range(len(source)) if source[i] == itm]]
