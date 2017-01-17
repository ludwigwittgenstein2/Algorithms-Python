from math import ceil

c = [-40, -50, -10]
A = [[-4, -1, -10], [-3,-2,-1],[0,-4,-5]]
b = [-10,-12,-20]

x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)

from scipy.optimize import linprog

res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds, x2_bounds))

print 'Kg of packet A is : ', ceil(res.x[0])
print 'Kg of packet B is : ', ceil(res.x[1])
print 'Kg of packet C is : ', ceil(res.x[2])