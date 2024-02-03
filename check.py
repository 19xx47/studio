from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import streamlit as st
def scale_image(path):
    try:
        with Image.open(path) as img:
            w, h = img.size
            print(f'Opening {path} with size {w}x{h}')
            img = img.resize((2224, 1224))
            img.save(path.replace('.png', '_scaled.png'))
    except FileNotFoundError:
        print(f'File {path} not found')
g = 9.81

def velocity(symin, symax, Srobot, s):
    Sx = s + 2
    Symin = symin + 0.5
    Symax = symax + 0.5
    uy = math.sqrt(2 * g * (Symax - Srobot))
    print("Uy = ", uy)
    t = uy / g
    ux = Sx / t
    angle = math.atan(uy / ux)
    return ux, uy, angle,t


def plot_trajectory(symin, symax, Srobot, s):
    ux, uy, angle,t = velocity(symin, symax, Srobot, s)

    t_total = 2 * uy / g  # Total time of flight
    t_values = np.linspace(0, t_total, num=100)
    
    # Calculate the x and y coordinates at each time step
    x_values = ux * t_values
    y_values = Srobot + uy * t_values - 0.5 * g * t_values**2

    # Plot the trajectory
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values)
    plt.xlim(0, 2)
    plt.title('Projectile Motion Trajectory')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height (m)')
    plt.grid(True)
    
    # Mark the initial and final points
    plt.scatter(0, Srobot, color='red', label='Launch Point')
    plt.scatter(x_values[-1], y_values[-1], color='green', label='Landing Point')
    plt.legend()
    st.pyplot(plt)

    # Show the plot
    plt.show()

path = 'Screenshot 2567-02-03 at 12.15.53.png'
scale_image(path)