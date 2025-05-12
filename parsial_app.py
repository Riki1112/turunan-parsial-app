    import streamlit as st
    import sympy as sp

    # Input fungsi dan titik evaluasi
    st.title("Aplikasi Turunan Parsial")
    
    # Input fungsi dari pengguna
    fungsi_input = st.text_input("Masukkan fungsi f(x, y):", "x**2 + y**2")
    x0 = st.number_input("Masukkan nilai x0:", value=0.0)
    y0 = st.number_input("Masukkan nilai y0:", value=0.0)

    # Variabel simbolik
    x, y = sp.symbols('x y')
    f = eval(fungsi_input)

    # Menghitung turunan parsial
    dfdx = sp.diff(f, x)
    dfdy = sp.diff(f, y)
    
    # Menghitung nilai turunan parsial pada titik tertentu
    dfdx_evaluasi = dfdx.evalf(subs={x: x0, y: y0})
    dfdy_evaluasi = dfdy.evalf(subs={x: x0, y: y0})

    # Menampilkan hasil
    st.write(f"Turunan parsial terhadap x: {dfdx} = {dfdx_evaluasi}")
    st.write(f"Turunan parsial terhadap y: {dfdy} = {dfdy_evaluasi}")

    # Grafik permukaan (Opsional)
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    x_range = np.linspace(-5, 5, 100)
    y_range = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = eval(fungsi_input.replace('x', 'X').replace('y', 'Y'))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    st.pyplot(fig)
    
