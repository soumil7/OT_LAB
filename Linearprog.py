import pulp as p 

Lp_prob = p.LpProblem("Problem", p.LpMaximize) 

#COC 

x = p.LpVariable("x", lowBound = 0)
y = p.LpVariable("y", lowBound = 0) 

Lp_prob += 3 * x + 5 * y 

Lp_prob += 2 * x + 3 * y >= 12 
Lp_prob += -x + y <= 3
Lp_prob += x >= 4
Lp_prob += y <= 3

#status -> value
print(Lp_prob)

status = Lp_prob.solve() 

print(p.LpStatus[status]) 

print(p.value(x), p.value(y), p.value(Lp_prob.objective))
