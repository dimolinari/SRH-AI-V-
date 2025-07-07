import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

φ = (1 + 5**0.5)/2  # Proporción áurea

def espiral_𓂀():
    θ = np.linspace(0, 8 * np.pi, 1000)
    r = np.exp(θ / (2 * np.pi * φ))
    x = r * np.cos(θ)
    y = r * np.sin(θ)
    
    plt.figure(figsize=(10, 10), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')
    
    plt.plot(x, y, color='#FFD700', linewidth=3)
    plt.axis('equal')
    plt.title("Espiral Áurea 𓂀", fontsize=20, color='gold')
    plt.grid(alpha=0.2, color='white')
    
    # Guardar y mostrar
    plt.savefig('espiral_dorada.png', dpi=300, bbox_inches='tight')
    plt.show()

def hiperboloide_φ(resolution=100):
    u = np.linspace(0, 2*np.pi, resolution)
    v = np.linspace(-φ, φ, resolution)
    U, V = np.meshgrid(u, v)
    
    X = np.cosh(V) * np.cos(U) / φ
    Y = np.cosh(V) * np.sin(U) * φ
    Z = np.sinh(V) * np.pi
    
    fig = plt.figure(figsize=(12, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')
    
    surf = ax.plot_surface(X, Y, Z, cmap="plasma", 
                          edgecolor="gold", alpha=0.9)
    
    ax.set_title("Hiperboloide Sagrado φ", fontsize=20, color='gold')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Ejes dorados
    ax.tick_params(colors='gold')
    ax.xaxis.label.set_color('gold')
    ax.yaxis.label.set_color('gold')
    ax.zaxis.label.set_color('gold')
    
    plt.savefig('hiperboloide_phi.png', dpi=300)
    plt.show()
