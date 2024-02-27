import math
import streamlit
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
angle =0 
gavity = 9.81
Hight_robot = 0.40*math.sin(angle)
Vy_max =0
Sx = 2
def find_prev_velocity_y(high_fromfloor):
    uy = math.sqrt(2 * gavity * (high_fromfloor - Hight_robot))
    return uy
def find_time(uy):
    t = uy / gavity
    return t
    
def find_prev_velocity_x(Sx, t):
    ux = Sx / t
    return ux

def find_angle(ux, uy):
    angle = math.atan(uy / ux)
    angle_degrees = math.degrees(angle)
    return angle_degrees

# def find_kinetic_energy(mass, dimension, symin, symax, Srobot, s, Spring_Length):
def scale_image(path):
    try:
        with Image.open(path) as img:
            w, h = img.size
            print(f'Opening {path} with size {w}x{h}')
            img = img.resize((754, 1224))
            img.save(path.replace('.png', '_scaled.png'))
    except FileNotFoundError:
        print(f'File {path} not found')

def plot_trajectory(ux, uy, angle_degrees,t,Srobot):
    # ux, uy, angle_degrees,t = velocity(symin, symax, Srobot, s)

    t_total = 2 * uy / gavity # Total time of flight
    t_values = np.linspace(0, t_total, num=100)
    
    # Calculate the x and y coordinates at each time step
    x_values = ux * t_values
    y_values = Srobot + uy * t_values - 0.5 * gavity * t_values**2

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