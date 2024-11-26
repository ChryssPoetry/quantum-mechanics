#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App Title
st.title("🌀 Quantum Computing Simulator: Saving the Planet, One Qubit at a Time!")
st.subheader("Where Quantum Meets Energy Crisis Solutions. By Nwafor Franklin")

# Sidebar for Navigation
st.sidebar.title("Explore Sections")
section = st.sidebar.radio(
    "What do you want to learn today?",
    [
        "Introduction to Quantum Computing",
        "Qubits and Superposition",
        "Quantum Gates",
        "Quantum Random Walk",
        "Quantum Energy Crisis Solutions",
    ],
)

# Introduction Section
if section == "Introduction to Quantum Computing":
    st.header("💡 Introduction to Quantum Computing")
    st.write("""
    Welcome to the future! Classical computers are great, but quantum computers? 
    They're like classical computers on steroids — with a bit of magic.
    
    **What’s the Big Deal?**
    - Classical computers process data as 0s and 1s (binary).
    - Quantum computers use **qubits**, which can be both 0 and 1 at the same time (superposition)!
    
    Imagine deciding between pizza and tacos. Classical computers make you choose, 
    but quantum computers say: "Why not both?" 🍕🌮
    
    This app explains quantum concepts and explores how quantum computing can tackle the **energy crisis**.
    """)
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/6/6f/Qubit_superposition.svg",
        caption="Superposition: Schrödinger's bit is both alive and dead.",
    )

# Qubits and Superposition Section
if section == "Qubits and Superposition":
    st.header("🔮 Qubits and Superposition")
    st.write("""
    A **qubit** is like a coin that's spinning in the air — it’s neither heads nor tails, but both. 
    This is called **superposition**.
    """)
    alpha = st.slider("Choose α (the probability amplitude for |0⟩):", 0.0, 1.0, 0.6)
    beta = np.sqrt(1 - alpha**2)
    st.write(f"Probability of |0⟩: {alpha**2:.2f}")
    st.write(f"Probability of |1⟩: {beta**2:.2f}")

    fig, ax = plt.subplots()
    ax.bar(["|0⟩", "|1⟩"], [alpha**2, beta**2], color=["blue", "orange"])
    ax.set_title("Qubit State Probabilities")
    ax.set_ylabel("Probability")
    st.pyplot(fig)

# Quantum Gates Section
if section == "Quantum Gates":
    st.header("🚪 Quantum Gates: Your Qubit Manipulators")
    st.write("""
    Quantum gates are like magic spells for qubits. Here are some popular ones:
    - **X Gate**: Flips |0⟩ to |1⟩ (basically, the "coin flip" of quantum).
    - **H Gate**: Puts a qubit into superposition (aka the multitasker’s dream).
    - **Z Gate**: Adds a "phase flip," which is fancy physics talk for tweaking the qubit's angle.
    """)

    gate = st.selectbox("Choose a gate to apply:", ["None", "X Gate", "H Gate", "Z Gate"])
    state = np.array([1, 0])  # Start with |0⟩

    if gate == "X Gate":
        x_gate = np.array([[0, 1], [1, 0]])
        state = x_gate @ state
    elif gate == "H Gate":
        h_gate = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        state = h_gate @ state
    elif gate == "Z Gate":
        z_gate = np.array([[1, 0], [0, -1]])
        state = z_gate @ state

    st.write(f"New state probabilities: |0⟩ = {np.abs(state[0])**2:.2f}, |1⟩ = {np.abs(state[1])**2:.2f}")
    fig, ax = plt.subplots()
    ax.bar(["|0⟩", "|1⟩"], np.abs(state)**2, color=["blue", "orange"])
    ax.set_title("Qubit State Probabilities After Gate")
    st.pyplot(fig)

# Quantum Random Walk Section
if section == "Quantum Random Walk":
    st.header("🚶‍♂️ Quantum Random Walk")
    st.write("""
    In a **random walk**, you either go left or right. In a **quantum random walk**, you can go both left and right — 
    simultaneously. Because, you know, quantum.
    """)

    n_steps = st.slider("Number of steps:", 10, 100, 50)

    def quantum_random_walk(n_steps):
        max_position = n_steps
        probabilities = np.zeros((2 * max_position + 1,), dtype=complex)
        probabilities[max_position] = 1.0
        coin = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

        for _ in range(n_steps):
            new_probabilities = np.zeros_like(probabilities, dtype=complex)
            for position in range(len(probabilities)):
                if probabilities[position] != 0:
                    new_probabilities[position - 1] += probabilities[position] * coin[0, 0]
                    new_probabilities[position + 1] += probabilities[position] * coin[1, 1]
            probabilities = new_probabilities

        return np.abs(probabilities)**2

    quantum_probs = quantum_random_walk(n_steps)
    positions = np.arange(-n_steps, n_steps + 1)

    fig, ax = plt.subplots()
    ax.bar(positions, quantum_probs, color="orange")
    ax.set_title("Quantum Random Walk Probabilities")
    ax.set_xlabel("Position")
    ax.set_ylabel("Probability")
    st.pyplot(fig)

# Quantum Energy Crisis Solutions Section
if section == "Quantum Energy Crisis Solutions":
    st.header("🌍 Quantum Solutions for the Energy Crisis")
    st.write("""
    How can quantum computing help solve the energy crisis? Let’s break it down:
    
    1. **Optimize Energy Grids**:
       Quantum computers can simulate massive energy grids to reduce losses and improve efficiency.
    
    2. **Design Better Materials**:
       Need a super battery? Quantum computers can simulate molecular structures to design materials with higher energy storage.
    
    3. **Predict Energy Demand**:
       By analyzing data in quantum parallel, they can forecast energy usage patterns.
       
    4. **Solve Logistics Problems**:
       Efficient delivery of renewable energy, anyone? Quantum algorithms can optimize routes and resources.

    In short, quantum computing helps us waste less energy and build cooler (literally) tech.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Quantum_computing_physics.svg", caption="Quantum Mechanics Meets Energy Efficiency.")


# In[ ]:




