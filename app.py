#symin = ระยะต่ำสุดของพื้นถึงตะกล้า = ?
#symax = ระยะสูงสุดของพื้นถึงตะกล้า = ?
#s = ระยะความกว้างหุ่งถึงจุดปล่อยลูกสควอซ  = ?
#Srobot = ความสูงหุ่นยนนต์ = ?
import math
import streamlit as st
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
    print("Ux = ", ux)
    print("Uy = ", uy)
    print("Angle = ", angle)
    print("Symin =", Symin, "Symax =", Symax, "Srobot =", Srobot, "s =", s, "Sx =", Sx, "t =", uy / g)
    st.success(f"Ux = {ux}")
    st.success(f"Uy = {uy}")
    st.success(f"Angle = {angle}")
    st.success(f"Symin = {Symin}, Symax = {Symax}, Srobot = {Srobot}, s = {s}, Sx = {Sx}, t = {t}")

    return ux, uy, angle

def conserveenergy(mass, dimension, symin, symax, Srobot, s):
    ux, uy, angle = velocity(symin, symax, Srobot, s)
    k = (0.5 * mass * (ux**2) + mass * g * dimension * math.sin(angle)) * 2 / dimension**2
    return k
def test():
    angle = math.tan(velocity(0.1, 0.25, 0.465, 0.102)[2])
    result = angle * (0.102 + 2)
    print("Result of pass= ", result)
    return result

def main():
    st.title("Robotics Physics Calculator")

    mass = st.text_input("Mass of the robot (kg)", "0.224")
    dimension = st.text_input("Dimension of the robot (m)", "0.1")
    symin = st.text_input("symin", "0.1")
    symax = st.text_input("symax", "0.25")
    Srobot = st.text_input("Srobot", "0.465")
    s = st.text_input("s", "0.102")

    if st.button("Calculate"):
        try:
            mass = float(mass)
            dimension = float(dimension)
            symin = float(symin)
            symax = float(symax)
            Srobot = float(Srobot)
            s = float(s)
            
            result_k = conserveenergy(mass, dimension, symin, symax, Srobot, s)
            st.success(f"result_k: {result_k}")
            st.success(f"F(N): {result_k*0.1}")
            result_pass = test()
            st.success(f"result_pass: {result_pass}")
        except ValueError:
            st.error("Please enter valid numeric values.")

    if st.button("Run Test"):
        result = test()
        st.success(f"Test Result: {result}")

if __name__ == "__main__":
    main()
print(conserveenergy(0.224, 0.1,0.1, 0.25, 0.465, 0.102))
print(test())
