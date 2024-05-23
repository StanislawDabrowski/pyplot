import matplotlib.pyplot as plt
import cmath



def f(x):
    return 2*x**(-2)+13+(-3)*x**2+7*x**3
def g(x):
    return x*x

def hr(x):
    return pow(cmath.e, x*1j).real

def hi(x):
    return pow(cmath.e, x*1j).imag


def display_plot(f):
    x = []
    y = []
    begining = float(input("podaj poczatek zakresu wykresu: "))
    end = float(input("podaj koniec zakresu wykresu: "))
    accuracy = float(input("podaj dokladnosc wylresu: "))
    i = begining
    while i<end:
        x.append(i)
        y.append(f(i))
        i+=accuracy
        
    plt.plot(x, y)
    plt.show()
    
display_plot(hr)
display_plot(hi)
