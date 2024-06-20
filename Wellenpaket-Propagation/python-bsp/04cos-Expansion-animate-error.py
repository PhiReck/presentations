import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Chebyshev as T
from taylorChebLib import taylorCoeff, chebyCoeff

import copy

from matplotlib.lines import Line2D
from matplotlib.text import Text
import matplotlib.animation as animation

samplePoints = 200
x = np.linspace(-1.3, 1.3, samplePoints)  # Sample data.
cosFreq = 15

fig, (ax1,ax2) = plt.subplots(2,1,figsize=(15, 10), layout='constrained')
ax1.set(xlim=[-1.3, 1.3], ylim=[-1.5, 2])
ax1.set_xlabel('x', fontsize = 20)
ax1.set_ylabel('f(x)', fontsize = 20)
ax1.tick_params(labelsize = 20)
ax1.legend()
ax2.set(xlim=[-1.3, 1.3], ylim=[1e-17, 1], yscale = 'log')
ax2.legend()
ax2.set_xlabel('x', fontsize = 20)
ax2.set_ylabel('Error', fontsize = 20)
ax2.tick_params(labelsize = 20)

ax1.set_title("Convergence: Chebyshev vs. Taylor", fontsize = 20)  # Add a title to the Axes.

cosExpansionCheb = np.full(samplePoints, 0.)
cosExpansionTaylor = np.full(samplePoints, 0.)

y = np.cos(cosFreq*x)
ax1.plot(x, y, 'k-', label='cos('+str(cosFreq)+'x)')


cosExpansionChebList = []
cosExpansionTaylList = []
errorChebList = []
errorTaylList = []

maxOrder = 50
for n in range(maxOrder):
    newtermCheb = chebyCoeff(n, cosFreq).real * T.basis(n)(x)
    cosExpansionCheb += newtermCheb
    cosExpansionChebList.append(copy.deepcopy(cosExpansionCheb))
    errorChebList.append(abs(y-cosExpansionCheb))

    newtermTaylor = taylorCoeff(n, cosFreq) * x**n
    cosExpansionTaylor += newtermTaylor
    cosExpansionTaylList.append(copy.deepcopy(cosExpansionTaylor))
    errorTaylList.append(abs(y-cosExpansionTaylor))


polDegreeLabel = ax1._add_text(Text(x=-0.97, y=1.55, text="Polynom-Grad N = " + str(0), fontsize = 30))
chebLine,  = ax1.plot(x, cosExpansionChebList[0], 'r-', label='Chebyshev')
taylorLine,  = ax1.plot(x, cosExpansionTaylList[0], 'b-', label='Taylor')
ax1.legend(fontsize = 30, loc='upper right')

chebError,  = ax2.plot(x, errorChebList[0], 'r-', label='Fehler Chebyshev')
taylorError,  = ax2.plot(x, errorTaylList[0], 'b-', label='Fehler Taylor')

def animate(i):
    polDegreeLabel.set_text("Polynom-Grad N = " + str(i))
    chebLine.set_data(x, cosExpansionChebList[i])
    taylorLine.set_data(x, cosExpansionTaylList[i])
    chebError.set_data(x, errorChebList[i])
    taylorError.set_data(x, errorTaylList[i])
    return chebLine#, taylorLine

ani = animation.FuncAnimation(
    fig,
    animate,
    interval=650,
    blit=False,  # blitting can't be used with Figure artists
    frames=range(maxOrder),
    # repeat_delay=100,
)

ani.pause()

def toggle_pause(self, *args, **kwargs):
    toggle_pause.counter += 1
    if toggle_pause.counter % 2 == 1:
        ani.resume()
    else:
        ani.pause()

toggle_pause.counter = 0


fig.canvas.mpl_connect('button_press_event', toggle_pause)


plt.show()