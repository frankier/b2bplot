import numpy as np
from matplotlib.ticker import MultipleLocator


def b2bplot(
    ax,
    args1,
    args2,
    xlabel,
    ylabel,
    orientation,
    minor_ticks=1,
    add_mean=False
):
    data1, label1 = args1
    data2, label2 = args2
    hN = ax.hist(data1, bins=max(data1), orientation=orientation, rwidth=0.8, label=label1)
    hS = ax.hist(data2, bins=max(data2), orientation=orientation, rwidth=0.8, label=label2)

    for p in hS[2]:
        p.set_width(-p.get_width())

    xmin = min([min(w.get_width() for w in hS[2]),
                min([w.get_width() for w in hN[2]])])
    xmin = np.floor(xmin)
    xmax = max([max(w.get_width() for w in hS[2]),
                max([w.get_width() for w in hN[2]])])
    xmax = np.ceil(xmax)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim(0)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    xt = ax.get_xticks()
    s = ['%.0f' % abs(i) for i in xt]
    ax.set_xticklabels(s)
    ax.axvline(0.0)

    ax.xaxis.set_minor_locator(MultipleLocator(minor_ticks))
    ax.yaxis.set_minor_locator(MultipleLocator(minor_ticks))

    def mean_line(data, left=False):
        min_xlim, max_xlim = ax.get_xlim()
        half = - min_xlim / (max_xlim - min_xlim)
        limit_args = dict(xmax=half) if left else dict(xmin=half)
        ax.axhline(data.mean(),  color='k', linestyle='dashed', linewidth=1, **limit_args)
        text_x = min_xlim if left else max_xlim
        ax.text(text_x + (minor_ticks if left else -max_xlim * 0.2 - minor_ticks * 2), data.mean() + 1 + minor_ticks, '{:.1f}'.format(data.mean()))

    if add_mean:
        mean_line(data1)
        mean_line(data2, left=True)


