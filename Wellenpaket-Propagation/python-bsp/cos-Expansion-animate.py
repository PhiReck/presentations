import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import Chebyshev as T
from taylorChebLib import taylorCoeff, chebyCoeff

import copy

from matplotlib.lines import Line2D
from matplotlib.text import Text
import matplotlib.animation as animation

samplePoints = 200
x = np.linspace(-1, 1, samplePoints)  # Sample data.
cosFreq = 15

# chebyPoly = np.polynomial.chebyshev.Chebyshev()


fig, ax = plt.subplots(figsize=(15, 9), layout='constrained')
# ax.plot(x, np.cos(5*x), label='cos(5*x)')  # Plot some data on the Axes.
# ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# ax.plot(x, x**3, label='cubic')  # ... and some more.
# ax.set_xlabel('x')  # Add an x-label to the Axes.
# ax.set_ylabel('f(x)')  # Add a y-label to the Axes.
ax.set(xlim=[-1, 1], ylim=[-1.5, 2], xlabel='x', ylabel='f(x)')
ax.legend()

ax.set_title("Convergence: Chebyshev vs. Taylor", fontsize = 20)  # Add a title to the Axes.

# cos_full = np.full(100, 0.)
# onespace = np.full(100,1)
cosExpansionCheb = np.full(samplePoints, 0.)
cosExpansionTaylor = np.full(samplePoints, 0.)
# print(cos_taylor)
# cos_full += np.cos(5*x)

artists = []
functions_to_plot = []
functions_to_plot.append(np.cos(cosFreq*x))
ax.plot(x, functions_to_plot[0], 'k-', label='cos('+str(cosFreq)+'x)')



cosExpansionChebList = []
cosExpansionTaylList = []

maxOrder = 25
for n in range(maxOrder):
    newtermCheb = chebyCoeff(n, cosFreq).real * T.basis(n)(x)
    cosExpansionCheb += newtermCheb
    cosExpansionChebList.append(copy.deepcopy(cosExpansionCheb))

    newtermTaylor = taylorCoeff(n, cosFreq) * x**n
    cosExpansionTaylor += newtermTaylor
    cosExpansionTaylList.append(copy.deepcopy(cosExpansionTaylor))

    # container = ax.plot(x, cosExpansionTaylor, 'b-')#, label= 'Taylor n = '+ str(maxOrder))
    # artists.append(container)
    # container = ax.plot(x, cosExpansionCheb, 'r-')#, label= 'Tschebyscheff n = '+ str(n))
    # artists.append(container)
    # container = ax.plot(x, onespace*besselj(n, cosFreq), label= 'n = ' + str(n))
    # container = ax.plot(x, newterm, label= 'n = ' + str(n))#functions_to_plot[n], label=2*n)
    
# ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=400)
# ax.plot(x, cosExpansionCheb, 'r.', label= 'Tschebyscheff n = '+ str(maxOrder))
# ax.plot(x, cosExpansionTaylor, label= 'Taylor n = '+ str(maxOrder))


polDegreeLabel = ax._add_text(Text(x=-0.97, y=1.75, text="Polynom-Grad N = " + str(0), fontsize = 30))
chebLine,  = ax.plot(x, cosExpansionChebList[0], 'r-', label='Chebyshev')
taylorLine,  = ax.plot(x, cosExpansionTaylList[0], 'b-', label='Taylor')
# leg = ax.legend(fontsize = 30)
ax.legend(fontsize = 30, loc='upper right')
def animate(i):
    polDegreeLabel.set_text("Polynom-Grad N = " + str(i))
    chebLine.set_data(x, cosExpansionChebList[i])
    taylorLine.set_data(x, cosExpansionTaylList[i])
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