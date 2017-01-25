#Heaviside step function

def heaviside(x):
  """Heaviside step function"""

  theta = None
  if x < 0:
    theta = 0.
  elif x == 0:
    theta = 0.5
  else:
    theta = 1.

  return theta

xvalues = []
h = 0.5
xmin, xmax = -4, 4
x = xmin
#while x <= xmax:
#  xvalues.append(x)
#  x += h

#for i in range(int((xmax - xmin)/h) + 1:
#  xvalues.append(i*h + xmin)

xvalues = (i*h + xmin for i in range (int((xmax - xmin)/h)+1))

# print(xvalues)

theta = []
for x in xvalues:
  theta.append(heaviside(x))

print(xvalues)
print(theta)
