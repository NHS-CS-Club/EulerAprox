import math

x_initial = float(input('Enter starting x value: '))
x_final = float(input('Enter value for which x should be approximated: '))
def derivative(a,step):
  return (function(a+step)-function(a))/step

def function(x):
  return (x+5)**2
#f(x+a) = f'(a) * dx + f(x)
def eulers_method(x, y, approximation):
  if x < approximation:
    while x < approximation:
      y += (derivative(x,.00001) * .00001)
      x += .00001
    return round(y, 5)
  if x > approximation:
    while x > approximation:
      y -= (derivative(x,.00001) * .00001)
      x -= .00001
    return round(y, 5)


print('Approximation: ' + str(eulers_method(x_initial, function(x_initial), x_final)))
print('Actual output: ' + str(function(x_final)))


