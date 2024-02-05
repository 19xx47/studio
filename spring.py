import matplotlib.pyplot as plt
import numpy as np

# Constants
num_coils = 10  # Number of coils in the spring
radius = 0.15  # Radius of the coils
height_per_coil = 0.1  # Height between adjacent coils

# Generate data points for the coil spring
theta = np.linspace(0, 2 * np.pi * num_coils, 1000)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.linspace(0, height_per_coil * num_coils, 1000)

# Plot the coil spring in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Coil Spring', color='blue')

# Customize the plot
ax.set_title('3D Coil Spring Visualization')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.grid(True)

plt.show()
