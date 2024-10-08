# -*- coding: utf-8 -*-
#
#       utils.py
#
#       Copyright 2018 Henry Fuheng Wu <wufuheng@gmail.com>
#       Copyright 2012 David Klasinc <bigwhale@lubica.net>
#       Copyright 2010 Andrew <andrew@karmic-desktop>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import os
import math
import logging
import time
import datetime

logger = logging.getLogger("Utils")


def get_next_filename(sdir, prefix, ext):
    for _ in range(0, 99999):
        now = '{0:%Y-%m-%d_%H-%M-%S}'.format(datetime.datetime.now())
        fname = os.path.join(sdir, "{}_{}{}".format(prefix, now, ext))
        if os.path.isfile(fname):
            time.sleep(1)
            continue
        else:
            return fname

    return "Kazam_recording{0}".format(ext)


def in_circle(center_x, center_y, radius, x, y):
    dist = math.sqrt((center_x - x) ** 2 + (center_y - y) ** 2)
    return dist <= radius


def get_by_idx(lst, index):
    return filter(lambda s: s[0] == index, lst)
