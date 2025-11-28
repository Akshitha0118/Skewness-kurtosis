import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

st.set_page_config(page_title="ECG Skewness & Kurtosis Visualizer", layout="wide")
st.title("📌 ECG Skewness & Kurtosis — Positive | Negative | Zero")

st.write(
    "This dashboard visualizes 3 different signals:\n"
    "**Positive Skewness**, **Negative Skewness**, and **Zero Skewness** "
    "to reflect the characteristics shown in the reference figure."
)

# Time axis
t = np.linspace(0, 10, 2000)

# ----------- Generate 3 signals -----------
# Positive skew & high kurtosis
ecg_pos = 2000 + 200 * np.sin(2 * np.pi * 1.2 * t) + 350 * (np.sin(2 * np.pi * 45 * t) > 0.97)
s_pos = skew(ecg_pos)
k_pos = kurtosis(ecg_pos)

# Negative skew & low kurtosis
ecg_neg = 2100 + 80 * np.sin(2 * np.pi * 0.5 * t) - np.abs(np.random.normal(0, 50, len(t)))
s_neg = skew(ecg_neg)
k_neg = kurtosis(ecg_neg)

# Zero skew & moderate kurtosis
ecg_zero = 2300 + 120 * np.sin(2 * np.pi * 0.8 * t) + np.random.normal(0, 40, len(t))
s_zero = skew(ecg_zero)
k_zero = kurtosis(ecg_zero)

# ----------- Plotting section -----------
st.write("### 📈 Waveform Plots Based on Skewness & Kurtosis")

# Positive Skewness
fig1, ax1 = plt.subplots(figsize=(8, 3))
ax1.plot(t, ecg_pos)
ax1.set_title(f"Positive Skewness | Sk = {s_pos:.2f} , K = {k_pos:.2f}")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("ECG Amplitude")
ax1.grid(True)
st.pyplot(fig1)

# Negative Skewness
fig2, ax2 = plt.subplots(figsize=(8, 3))
ax2.plot(t, ecg_neg)
ax2.set_title(f"Negative Skewness | Sk = {s_neg:.2f} , K = {k_neg:.2f}")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("ECG Amplitude")
ax2.grid(True)
st.pyplot(fig2)

# Zero Skewness
fig3, ax3 = plt.subplots(figsize=(8, 3))
ax3.plot(t, ecg_zero)
ax3.set_title(f"Zero Skewness | Sk = {s_zero:.2f} , K = {k_zero:.2f}")
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("ECG Amplitude")
ax3.grid(True)
st.pyplot(fig3)

st.success("📌 Displaying the effect of skewness and kurtosis on ECG waveforms .")

