#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import cycle

import numpy as N
import matplotlib.pyplot as P
try:
    import seaborn
    seaborn.set_style("whitegrid")
except ImportError:
    pass

def schechter_L(l, alpha=-1.):

    return l**alpha * N.exp(-l)

def schechter_M(m, alpha=-1.):

    # 0.4 ln(10) = 0.92...
    return 0.92103403719761845 * 10**(-0.4*m*(alpha + 1)) * N.exp(-10**(-0.4*m))

print N, type(N)

l = N.logspace(-2, 1)                     # L / L*
m = N.linspace(-3, 3)                     # M - M*

fig = P.figure()
axL = fig.add_subplot(1, 2, 1,
                      xlabel="log(L / L*)",
                      ylabel=u"log(Φ(L) / Φ* × L*)",
                      title="Fonction de Schechter")
axM = fig.add_subplot(1, 2, 2,
                      xlabel="M - M*",
                      ylabel=u"log(Φ(M) / Φ*)")

linecycler = cycle(["--", "-", ":", "-."])
for a in (-1.5, -1, -0.5):
    ls = next(linecycler)
    line, = axL.plot(N.log10(l), N.log10(schechter_L(l, alpha=a)),
                     ls=ls, label=u"α = %.1f" % a)
    axM.plot(m, N.log10(schechter_M(m, alpha=a)),
             c=line.get_color(), ls=ls)

axL.legend(loc='upper right')
axM.invert_xaxis()
fig.tight_layout()

P.show()

