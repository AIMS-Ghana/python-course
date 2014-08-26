from pylab import *

from square_geom import *

v_square_area = np.vectorize(square_area)
v_square_perimeter = np.vectorize(square_perimeter)

S = np.linspace(0,10)

A = v_square_area(S)
P = v_square_perimeter(S)

plot(S, A, '-r', label="Area")
plot(S, P, ':b', label="Perimeter")

xlabel('side length')
ylabel('geo values')
title('Square Geo Properties')
legend(loc='upper right')

show()