#symin = ระยะต่ำสุดของพื้นถึงตะกล้า = ?
#symax = ระยะสูงสุดของพื้นถึงตะกล้า = ?
#s = ระยะความกว้างหุ่งถึงจุดปล่อยลูกสควอซ  = ?
#Srobot = ความสูงหุ่นยนนต์ = ?
import math
import streamlit as st
from check import velocity, plot_trajectory
import numpy as np
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
    print("angle_degrees = ", angle_degrees)

    # angle = math.atan(uy / ux)
#     print("Ux ความเร็วต้นในแนวแกน x= ", ux)
#     print("Uy ความเร็วต้นในแนวแกน y= ", uy)
#     print("Angle มุม= ", angle)
#     print("Symin ระยะต่ำสุดของพื้นถึงตะกล้า=", Symin, "Symax ระยะสูงสุดของพื้นถึงตะกล้า=", Symax, "Srobot ความสูงหุ่นยนนต์=", Srobot, "s ระยะความกว้างหุ่งถึงจุดปล่อยลูกสควอซ=", s, 
# "Sx ระยะรวมในแนวแกน x =", Sx, "t =", uy / g)
    # st.success(f"Ux ความเร็วต้นในแนวแกน x= {ux}")
    # st.success(f"Uy ความเร็วต้นในแนวแกน y = {uy}")
    # st.success(f"Angle มุม= {angle}")
    # st.success(f"t เวลา= {t}")
#     st.success(f"Symin ระยะต่ำสุดของพื้นถึงตะกล้า= {Symin}, Symax ระยะสูงสุดของพื้นถึงตะกล้า= {Symax}, Srobot ความสูงหุ่นยนนต์= {Srobot}, s ระยะความกว้างหุ่งถึงจุดปล่อยลูกสควอซ= {s}, 
# Sx ระยะรวมในแนวแกน= {Sx}, t = {t}")

    return ux, uy, angle_degrees, t

def conserveenergy(mass, dimension, symin, symax, Srobot, s):
    ux, uy, angle,t = velocity(symin, symax, Srobot, s)
    k = (0.5 * mass * (ux**2) + mass * g * dimension * math.sin(angle)) * 2 / dimension**2
    return k
def test():
    angle = velocity(0.5, 0.75, 0.465, 0.102)[2]
    angle_radians = np.radians(angle)
    print("Angle= ", np.tan(angle_radians))
    result = np.tan(angle_radians) * (0.102 + 2)
    print("Result of pass= ", result)
    return result

def main():
    st.title("Shoot a squash ball Calculator")

    mass = st.text_input("Mass of the ball (kg)", "0.224")
    dimension = st.text_input("Spring extension distance (m)", "0.1")
    symin = st.text_input("Symin ระยะต่ำสุดของพื้นถึงตะกล้า", "0.50")
    symax = st.text_input("Symax ระยะสูงสุดของพื้นถึงตะกล้า", "0.75")
    Srobot = st.text_input("Srobot ความสูงหุ่นยนนต์", "0.465")
    s = st.text_input("s ระยะความกว้างหุ่งถึงจุดปล่อยลูกสควอซ", "0.102")

    if st.button("Calculate"):
        try:
            mass = float(mass)
            dimension = float(dimension)
            symin = float(symin)
            symax = float(symax)
            Srobot = float(Srobot)
            s = float(s)
            plot_trajectory(symin, symax, Srobot, s)
            # st.image('Screenshot 2567-02-03 at 12.15.53_scaled.png', caption='Projectile Motion Trajectory', use_column_width=True)
            result_k = conserveenergy(mass, dimension, symin, symax, Srobot, s)
            ux, uy, angle_degrees, t = velocity(symin, symax, Srobot, s)
            st.success(f"Ux ความเร็วต้นในแนวแกน x= {ux}")
            st.success(f"Uy ความเร็วต้นในแนวแกน y = {uy}")
            st.success(f'Trajectory Angle: {angle_degrees:.2f} degrees')
            st.success(f"t เวลา= {t}")
            st.success(f"result_k: {result_k}")
            st.success(f"F(N): {result_k*0.1}")
            result_pass = test()
            st.success(f"result_pass: {result_pass}")
        except ValueError:
            st.error("Please enter valid numeric values.")

    # if st.button("Run Test"):
    #     result = test()
    #     st.success(f"Test Result: {result}")

if __name__ == "__main__":
    main()
print(conserveenergy(0.224, 0.1,0.5, 0.75, 0.465, 0.102))
print(test())
plot_trajectory(0.5, 0.75, 0.465, 0.102)