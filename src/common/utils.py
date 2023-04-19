from math import floor, ceil

from src.common.constants import VEC

inttup = lambda tup: tuple(map(floor, tup))
floorvec = lambda vec: VEC(floor(vec.x), floor(vec.y))
ceilvec = lambda vec: VEC(ceil(vec.x), ceil(vec.y))