import numpy as np
import matplotlib.pyplot as plt

# BJT Ebers-Moll: Ic = Is * exp(Vbe / (n * Vt))
Is = 10e-15       # Saturation current (10 fA, typical for small-signal BJT)
n = 1.0           # Ideality factor
Vt = 0.026        # Thermal voltage at ~300K (26 mV)

Vbe = np.linspace(0.4, 0.75, 2000)
Ic = Is * np.exp(Vbe / (n * Vt)) * 1000  # convert to mA

fig, ax = plt.subplots(figsize=(8, 5), dpi=160)
ax.plot(Vbe, Ic, linewidth=2.5, color='black')
ax.set_title('BJT Transfer Characteristic: $I_C$ vs $V_{BE}$')
ax.set_xlabel('$V_{BE}$ (V)')
ax.set_ylabel('$I_C$ (mA)')
ax.set_xlim(0.4, 0.75)
ax.set_ylim(0, 20)
ax.grid(alpha=0.25)

# Mark a typical bias point
Vbe_bias = 0.70
Ic_bias = Is * np.exp(Vbe_bias / (n * Vt)) * 1000
ax.plot(Vbe_bias, Ic_bias, 'ro', markersize=8)
ax.annotate(f'Bias point\n$V_{{BE}}$={Vbe_bias} V, $I_C$={Ic_bias:.1f} mA',
            (Vbe_bias, Ic_bias),
            textcoords='offset points', xytext=(-120, 10), color='red',
            arrowprops=dict(arrowstyle='->', color='red'))

fig.tight_layout()
fig.savefig('src/images/BJT_Ic_Vbe.svg')
fig.savefig('src/images/BJT_Ic_Vbe.png')
print('Saved: src/images/BJT_Ic_Vbe.svg')
print('Saved: src/images/BJT_Ic_Vbe.png')
