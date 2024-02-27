#symin = ระยะต่ำสุดของพื้นถึงตะกล้า = ?
#symax = ระยะสูงสุดของพื้นถึงตะกล้า = ?
#s = ระยะความกว้างหุ่งถึงจุดปล่อยลูกสควอซ  = ?
#Srobot = ความสูงหุ่นยนนต์ = ?
import math
import streamlit as st
from check import velocity, plot_trajectory
import numpy as np
from main import find_prev_velocity_y, find_time, find_prev_velocity_x, find_angle, plot_trajectory
g = 9.81
def velocity(symin, symax, Srobot, s):
    Sx = s
    Symin = symin 
    Symax = symax 
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

def conserveenergy(mass, dimension, symin, symax, Srobot, s, Spring_Length):
    ux, uy, angle,t = velocity(symin, symax, Srobot, s)
    print("________________________")
    print ("ux= ", ux, "uy= ", uy, "angle= ", angle, "t= ", t, "mass= ", mass, "dimension= ", dimension, "Spring_Length= ", Spring_Length)
    k = (0.5 * mass * (ux**2) + mass * g * Spring_Length * math.sin(angle)) * 2 / dimension**2
    return k
def test(Hight_robot):
    angle = velocity(0.5, 0.75, 0.465, 0.102)[2]
    print("Angle= ", angle)
    angle_radians = np.radians(angle)
    # print("Angle in radians= ", np.tan(angle))
    # print("Anglegg= ", np.tan(angle_radians))
    # print("Srobot= ", Srobot+1,angle_radians)
    result = (Hight_robot + 1) *np.tan(angle_radians)
    print("Result of pass= ", result)
    return result

def main():
    st.title("Shoot a squash ball Calculator")

    mass = st.text_input("Mass of the ball (kg)", "0.224")
    dimension = st.text_input("Spring extension distance (m)", "0.1")
    high_fromfloor_min = st.text_input("ระยะต่ำสุดของพื้นถึงตะกล้า", "0.75")
    high_fromfloor = st.text_input("ระยะของพื้นถึงตะกล้า", "1")
    high_fromfloor_max = st.text_input("ระยะสูงสุดของพื้นถึงตะกล้า", "0.75")
    # Srobot = st.text_input("Srobot ความสูงหุ่นยนนต์", "0.465")
    Sx = st.text_input("s ระยะจากจุดปล่อยลูกสควอซ", "0.2")
    Spring_Length = st.text_input("Spring_Length ความยาวของสปริง", "0.15")

    if st.button("Calculate"):
        try:
            mass = float(mass)
            dimension = float(dimension)
            high_fromfloor_min = float(high_fromfloor_min)
            high_fromfloor_max = float(high_fromfloor_max)
            high_fromfloor = float(high_fromfloor)
            Spring_Length = float(Spring_Length)
            Sx = float(Sx)
            # plot_trajectory(high_fromfloor)
            # st.image('Screenshot 2567-02-03 at 12.15.53_scaled.png', caption='Projectile Motion Trajectory', use_column_width=True)
            # result_k = conserveenergy(mass, dimension, symin, symax, Srobot, s, Spring_Length)
            uy= find_prev_velocity_y(high_fromfloor)
            t = find_time(uy)
            ux = find_prev_velocity_x(Sx, t)
            angle_degrees = find_angle(ux, uy)
            st.success(f"Ux ความเร็วต้นในแนวแกน x= {ux}")
            st.success(f"Uy ความเร็วต้นในแนวแกน y = {uy}")
            st.success(f'Trajectory Angle: {angle_degrees:.2f} degrees')
            st.success(f"t เวลา= {t}")
            # st.success(f"result_k: {result_k}")
            # st.success(f"F(N): {result_k*0.1}")
            Hight_robot = 0.40*math.sin(angle_degrees)
            result_pass = test(Hight_robot)
            st.success(f"result_pass_obstacle: {result_pass}")
            plot_trajectory(ux, uy, angle_degrees,t,Hight_robot)
        except ValueError:
            st.error("Please enter valid numeric values.")

    # if st.button("Run Test"):
    #     result = test()
    #     st.success(f"Test Result: {result}")

if __name__ == "__main__":
    main()
print(conserveenergy(0.224, 0.1,0.5, 0.75, 0.465, 0.102, 0.15))
# print(test())
# print(test(0.465))
