import numpy as np
import matplotlib.pyplot as plt

# Fundamental: sin(wt)
A1 = 1.0
# Second harmonic amplitude (adjust to show stronger/weaker asymmetry)
A2 = 0.2
# 90-degree phase shift on 2nd harmonic relative to sine reference
phi2 = np.pi / 2

# Use one period of the fundamental
t = np.linspace(0, 2 * np.pi, 2000)
# Inverting amplifier output: fundamental starts going negative (down) first
fundamental = -A1 * np.sin(t)
second_harmonic = A2 * np.sin(2 * t + phi2)
composite = fundamental + second_harmonic

fig, ax = plt.subplots(figsize=(10, 5), dpi=160)
ax.plot(t, fundamental, label='Fundamental: -sin(wt)', linewidth=2)
ax.plot(t, second_harmonic, label=f'2nd harmonic: {A2:.2f}*sin(2wt + 90 deg)', linewidth=2)
ax.plot(t, composite, label='Composite (inverting output)', linewidth=2.5, color='black')

ax.axhline(0, color='gray', linewidth=0.8)
ax.set_title('Inverting Output: Fundamental + 2nd Harmonic (90 deg phase shift)')
ax.set_xlabel('wt (rad)')
ax.set_ylabel('Amplitude')
ax.set_xlim(0, 2 * np.pi)
ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax.set_xticklabels(['0', 'pi/2', 'pi', '3pi/2', '2pi'])
ax.grid(alpha=0.25)
ax.legend(loc='upper right')

# Mark upper and lower peaks to make asymmetry obvious
imax = np.argmax(composite)
imin = np.argmin(composite)
ax.plot(t[imax], composite[imax], 'ro')
ax.plot(t[imin], composite[imin], 'bo')
ax.annotate(f'+peak = {composite[imax]:.3f}', (t[imax], composite[imax]),
            textcoords='offset points', xytext=(10, 10), color='red')
ax.annotate(f'-peak = {composite[imin]:.3f}', (t[imin], composite[imin]),
            textcoords='offset points', xytext=(10, -20), color='blue')

fig.tight_layout()
fig.savefig('src/images/second_harmonic_90deg.svg')
fig.savefig('src/images/second_harmonic_90deg.png')
print('Saved: src/images/second_harmonic_90deg.svg')
print('Saved: src/images/second_harmonic_90deg.png')
