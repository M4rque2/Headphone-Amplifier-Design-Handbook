# Chapter 4

Hybrid amplifiers can be classified by device arrangement across stages, such as tube-gain/solid-state-power and solid-state-gain/tube-power designs. In practice, they usually sound either tube-like or solid-state-like, rather than a blend of both.

## Rudistor RP7
The Rudistor RP7 is a boutique hybrid headphone amplifier by Italian designer Rudi Stor. Community discussions often describe the RP7 as an impressive and highly engaging amplifier, with a warm-leaning presentation and strong pairing with classic high-impedance headphones such as the HD600, HD650, K501, and K601. At the same time, some users have complained about build quality, quality consistency, undocumented component changes between units, and high pricing.

Sadly, after the COVID-19 pandemic around 2020, Mr. Rudi lost contact with the Hi-Fi community.

![Rudistor RP7](images/Rudistor_RP7.svg)

The schematic, like the SinglePower amplifiers introduced in the previous chapter, is a textbook-simple circuit. Its measured performance is acceptable, at around 0.01% distortion as the manufacturer claims, yet it sounds absolutely lovely. It is one of my personal favourites. 

Using tubes at an extraordinarily low voltage (42V) is a bold choice, and tube choice is critical. Few tubes work well in such conditions; the 12AU7 is one of them. The resistor drops about half of the voltage, so the tube actually works at about 15V-25V. Even so, it delivers enough current, and distortion and noise are low enough for headphone use.

### Why simple amplifiers sound better
You have probably heard Nelson Pass say, "Simple sounds better."{{#cite norton1991simplesoundsbetter}}. In this section, I use the Rudistor RP7 as an example to explain why this is true both theoretically and experimentally.

### The Triode Law
A triode is fundamentally a space-charge device. Electrons emitted by the hot cathode form a charge cloud between cathode and plate. The control grid modulates how easily electrons flow through this cloud to the anode. The space-charge-limited current follows the Child-Langmuir law, which a triode modifies by allowing the grid to change the effective accelerating voltage.

Drop the output stage and feedback loop, now we have simple common cathod amplifier stage.

![Rudistor RP7 Gain Stage](images/Rudistor_RP7_Gain_Stage.svg)

For practical triode analysis, the most useful model is:

$$ I_a = K\left(U_{gk}+\frac{U_{ak}}{\mu}\right)^{3/2} $$

where:
- $I_a$ is the anode current
- $U_{gk}$ is the grid-to-cathode voltage
- $U_{ak}$ is the anode-to-cathode voltage
- $K$ is a tube-dependent constant
- $\mu$ is the amplification factor

This $3/2$-power law is the **essential nonlinearity** of the triode. It is not a straight line, which means distortion is inevitable if you push a signal through it.

### Why Second Harmonic Dominates

To find the distortion spectrum, we expand the anode current in a Taylor series around the bias point:

$$
i_a = a_1 u_g + a_2 u_g^2 + a_3 u_g^3 + a_4 u_g^4 + \cdots
$$

where $u_g$ is the small-signal grid voltage. Taking derivatives of the $3/2$-power law:

$$
a_1 = \frac{\partial I_a}{\partial U_{gk}}\Big|_Q = \frac{3}{2}K U_{\text{eff},0}^{1/2}
$$

$$
a_2 = \frac{1}{2}\frac{\partial^2 I_a}{\partial U_{gk}^2}\Big|_Q = \frac{3}{8}K U_{\text{eff},0}^{-1/2}
$$

$$
a_3 = \frac{1}{6}\frac{\partial^3 I_a}{\partial U_{gk}^3}\Big|_Q = -\frac{1}{16}K U_{\text{eff},0}^{-3/2}
$$

where $U_{\text{eff},0}$ is the effective bias voltage.

Notice the pattern: each coefficient decays in a specific way with bias voltage. The ratio of coefficients is:

$$
\frac{a_2}{a_1} = \frac{1}{4U_{\text{eff},0}}, \qquad \frac{a_3}{a_1} = -\frac{1}{24U_{\text{eff},0}^2}
$$

For a sinusoidal input $u_g(t)=\hat{u}\sin\omega t$:

- The **quadratic term** produces: $a_2 u_g^2 = \frac{a_2\hat{u}^2}{2}\left(1-\cos 2\omega t\right)$
  
  This generates a second harmonic with amplitude $I_2 \approx \frac{a_2\hat{u}^2}{2}$.

- The **cubic term** produces: $a_3 u_g^3 = \frac{a_3\hat{u}^3}{4}\left(3\sin\omega t - \sin 3\omega t\right)$
  
  This generates a third harmonic with amplitude $I_3 \approx \frac{|a_3|\hat{u}^3}{4}$.

The ratio of third to second harmonic is:

$$
\frac{I_3}{I_2} = \frac{|a_3|\hat{u}}{2a_2} \approx \frac{\hat{u}}{12U_{\text{eff},0}}
$$

If the signal amplitude $\hat{u}$ is much smaller than the bias voltage $U_{\text{eff},0}$ (true for audio amplifiers), then $I_3 \ll I_2$.

Higher harmonics are suppressed even more strongly because each successive derivative is multiplied by another power of $U_{\text{eff},0}$ in the denominator.

The figure below is from simulation, my real-world measurements show essentially the same FFT spectrum.

![Rudistor RP7 FFT SPECTRUM](images/Rudistor_RP7_FFT_SPECTRUM.svg)

### Why This Sounds Better

The triode law naturally produces **even-harmonic distortion dominated by the second harmonic**. This is not a flaw; it is the signature of the triode physics.

Even-order harmonics (second, fourth, etc.) tend to be **musically consonant** with the fundamental. Odd-order harmonics (third, fifth, etc.) often sound harsher and introduce intermodulation artifacts.

Simple circuits like the Rudistor RP7 have:
1. Low overall distortion (0.01% measured).
2. Dominated by even-order (second harmonic) content.
3. Minimal odd-order harmonics because the $3/2$-power law suppresses them naturally.

This combination creates a sound that is **subjectively pleasing and smooth**, even though it is not "distortion-free" in the engineering sense. The distortion character is determined by the tube physics, not by sloppy design.

This is why simple triode amplifiers, when biased properly, often sound better than complex solid-state designs with lower measured distortion but different harmonic content.
