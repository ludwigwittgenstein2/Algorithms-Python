

c = [-8.25, -7.5]
A = [[0.5, 0.75], [0.5, 0.25]]
b = [165,93]

x0_bounds = (0, None)
x1_bounds = (0, None)

from scipy.optimize import linprog

res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds))

print 'Mix 1 produced are : ', int(res.x[0])

print 'Mix 2 produced are : ', int(res.x[1])