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
            img = img.resize((754, 1224))
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
    angle = np.arctan2(uy, ux)
    angle_degrees = np.degrees(angle)

    # angle = math.atan(uy / ux)
    return ux, uy, angle_degrees,t


def plot_trajectory(symin, symax, Srobot, s):
    ux, uy, angle_degrees,t = velocity(symin, symax, Srobot, s)

    t_total = 2 * uy / g  # Total time of flight
    t_values = np.linspace(0, t_total, num=100)
    
    # Calculate the x and y coordinates at each time step
    x_values = ux * t_values
    y_values = Srobot + uy * t_values - 0.5 * g * t_values**2

    background_image = plt.imread('Screenshot 2567-02-03 at 12.15.53_scaled.png')  # Replace with the actual path to your image
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(background_image, extent=[0, 2.5, 0, 0.5]) 
    ax.plot(x_values, y_values)
    ax.set_xlim(0, 2)
    ax.set_title('Projectile Motion Trajectory')
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')
    ax.grid(True)
    
    # Mark the initial and final points
    ax.scatter(0, Srobot, color='red', label='Launch Point')
    ax.scatter(x_values[-1], y_values[-1], color='green', label='Landing Point')
    ax.legend()
    
    st.pyplot(fig)

    # plt.show()

path = 'Screenshot 2567-02-03 at 12.15.53.png'
scale_image(path)