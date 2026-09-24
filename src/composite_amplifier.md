# Chapter 1

Like a story that begins with its ending, we will start this book with the ultimate answer. We will first look at the absolute pinnacle of contemporary audio engineering, the state-of-the-art and best-measuring circuits of the 2020s. If your only goal is to know the "Best Headphone Amplifier" right now, this chapter is all you need. After this, we will travel back in time to explore the older, classic designs that led us here.

Topping calls its design "NFCA" (Nested Feedback Composite Amplifier), SMSL calls it "PLFC" (Precision Linear Feedback Circuit), they are basically the same thing. I'll use the audio community's more familiar name: the composite amplifier for the rest of this chapter.

The idea of a composite amplifier is simple: cascade two amplifiers so their open-loop gains multiply, enabling deeper feedback. As a result, distortion, bandwidth, noise, and output impedance can all improve. 

The chanllege is to keep the feedback loop stable, because each amplifier has its own dominant pole, and each pole adds 90 degrees phase lag. If the total phase lag approaches 180 degrees while loop gain is still above 0 dB, the circuit can oscillate. Therefore, poles and zeros must be configured carefully to keep a composite amplifier stable.

## Topping A90

The Topping A90 was launched in May 2020 at US$499. It joined a measurement-driven wave of headphone amplifiers whose notable milestones included NwAvGuy’s Objective2 in 2011, the Massdrop THX AAA 789 and JDS Labs Atom in 2018, and the SMSL SP200 in 2019. These products made low noise, low distortion, and competitive pricing central to their appeal. The A90 became a landmark within this movement by combining exceptionally low noise and distortion with high output power and balanced connectivity at a relatively accessible price.

![Topping A90](images/Topping_A90.jpg)

The topology is shown below.

![Topping A90 Schematic](images/Topping_A90.svg)

The A90 combines an precision op-amp(OPA1612) drives two fast high-current op-amp(TPA6120A2) in parallel as output stage. 

The output stage set at unity voltage gain and can be treated as a fast buffer. TI specifies a typical small-signal bandwidth of 100 MHz for the THS6012 at unity gain, with a 1 kΩ feedback resistor, at 25 Ω load. If the global feedback loop crosses unity gain well below the output stage’s bandwidth, the output stage contributes relatively little additional phase lag at crossover, making the composite amplifier easier to stabilize.

![THS6012 output stage Gain Phase](images/THS6012_Gain_Phase.svg)

OPA1612's GBW is 40Mhz, well below the 100Mhz bandwidth of the output stage, it should theoretically makes the amp stable. C67 and C70 provide additional high-frequency compensate, improve phase margin and make stability less sensitive to loading and parasitic effects. 

If we approximate the TPA6120A2 output stage as an ideal unity-gain wire, the circuit can be simplified as:

![OPA1612 drive stage](images/Topping_A90_OPA1612.svg)

In this simplified circuit, \\(C_2\\) is in parallel with \\(R_3\\). This combination is in series with \\(C_1\\), and the whole branch is in parallel with \\(R_2\\). The feedback impedance is therefore

\\[
Z_f(s)=R_2\parallel
\left[
\frac{1}{sC_1}
+\left(R_3\parallel\frac{1}{sC_2}\right)
\right].
\\]

Here, \\(s=\sigma+j\omega\\) is the complex frequency variable used in the Laplace transform. For sinusoidal frequency-response analysis, set \\(\omega=2\pi f\\) , \\(j=\sqrt{-1}\\), and \\(\parallel\\) denotes impedances connected in parallel.

The simulated gain phase plot of OPA1612:

![OPA1612 drive stage Gain Phase](images/OPA1612_Gain_Phase.svg)

Let a slower drive stage controls a faster output stage, is one of the common approachs to make a compsite amplifier. The Topping A90 is this kind of composite amplifier. 

Imagine steering a boat that responds slowly. If you make another correction before the boat has reacted to the first, you can overcorrect and start zigzagging. Making corrections more slowly helps keep it on course. A boat that responds quickly is easier to steer. Similarly, an amplifier is easier to keep stable when its output stage responds much faster than the feedback loop tries to correct it.

A more detailed techinical explanation can be found in "Composite Amplifiers: High Output Drive Capability with Precision" by Jino Loquinario from ADI {{#cite jino2019compositeampadi}}.
<!-- 
Some audiophiles may be bothered since it is pseudo-balanced, the inverting output is generated from non-inverting output, Bryston BHA-1 and many other Hi-Fi amplifiers have implemented such topology too.
-->
The successor model, A90 Discrete, keeps the same core topology: a voltage-feedback op-amp driving a fast current-feedback op-amp, both implemented in discrete components.

## Turbocharged Audio Amplifier

In the Topping A90, the second amplifier is set at unity gain, so its local negative feedback mainly corrects its own distortion. The two amplifier's gain is not multiplied, If you want the second stage's gain to participate in global feedback, a classic example is the LM1875-based "Turbocharged Audio Amplifier" proposed by Kitchin et al. {{#cite kitchin1992turbocharged}}. It was designed as a power amplifier, but it can also work with headphones because the composite design effectively improves the LM1875's noise floor.

![Turbocharged Audio Amplifier](images/Turbocharged_LM1875.svg)

More open-loop gain allows deeper negative feedback, reducing the distortion of the amplifier from 0.02% (LM1875 alone) to 0.005% (AD711 + LM1875 composite).

![Turbocharged Phase Leading Network](images/LM1875_Phase_Lead_Network.svg)

A phase-lead network is another approach to build a composite amplifier. 

In this exmample, R1, R2, and C1 form a phase-lead network, it helps improve phase margin, otherwise the amplifier will oscillate. As the transfer curve shows, it creates a zero at \\(f_z = \frac{1}{2\pi R_1 C_1}\\), about 400 kHz, and a higher-frequency pole at \\(f_p = \frac{1}{2\pi (R_1 \parallel R_2) C_1}\\), about 20 MHz. This provides enough phase margin at the 0 dB gain crossover. Finally the close-loop gain and phase shown as below:

![Turbocharged Amplifier Bode Analysis](images/Turbocharged_Bode.svg)

## Omicron Headphone Amplifier

In the "Turbocharged Audio Amplifier", about 30 dB of gain is sacrificed in the phase-leading network as the price of phase compensation. If you want more gain available for global feedback, the Omicron amplifier by Alexcp from diyaudio is built this way. It implements a dual-pole compensate.

![Omicron Headphone Amplifier](images/Omicron_Headphone_Amplifier.svg)

It is a sophisticated amplifier consisting of two gain stages and a Class A output stage.

![Omicron Amplifier Bode Analysis](images/Omicron_Bode.svg)

From the Bode plot, we can see a peak in the gain curve at about 17 kHz, and the phase changes sharply around this frequency and drops below -180 degrees at higher frequencies, indicating a strong tendency toward oscillation. The phase recovers at about 1 MHz. Finally, some phase margin is preserved at the 0 dB gain crossover. Therefore, D3-D6 form a protection circuit that helps the amplifier recover from clipping.

If the complete schematic gives you a headache, here is a simplified version:

![Omicron Headphone Amplifier](images/Omicron_Simplified.svg)

C1, C2, R3, and R4 form a frequency-dependent local negative-feedback network around U2A. At low frequencies, the capacitors have high impedances, the gain of the composite is approximately the product of the open-loop gains of U2B and U2A. This provides a large amount of gain for the global feedback loop to reduce distortion and output-stage errors.

As frequency increases, the capacitors pass more of the output signal back to U2A's inverting input. Let \\(A_A(s)\\) be U2A's open-loop gain and \\(\beta_c(s)\\) the transfer function from its output to its inverting input. Its gain with local feedback is

\\[
G_A(s)=\frac{A_A(s)}{1+A_A(s)\beta_c(s)}
\\]

Ignoring op-amp input loading and assuming a low output impedance, nodal analysis of the RC ladder gives

\\[
\beta_c(s)=\frac{bs^2}{1+as+bs^2}
\\]

\\[
a=R_3C_1+R_4(C_1+C_2) \qquad b=R_3R_4C_1C_2
\\]

Where \\(\lvert A_A\beta_c\rvert\gg1\\), U2A's gain is approximately the inverse of the feedback-network transfer function:

\\[
G_A(s)\approx\frac{1}{\beta_c(s)}=\frac{1+as+bs^2}{bs^2}
\\]

Below the two numerator corner frequencies, this approximation behaves as a double integrator and falls at approximately -40 dB/decade. The numerator introduces two zeros, which progressively flatten this slope to -20 dB/decade and then toward 0 dB/decade. In the frequency range where the capacitors act approximately as short circuits and U2A still has sufficient open-loop gain, U2A approaches a unity-gain buffer, so the composite's frequency response is mainly governed by U2B. 

The zeros provide phase lead relative to the double-integrator region and help restore phase margin before the global loop's unity-gain crossover.

For the values shown

\\[
R_3=2.2\ \mathrm{k\Omega} \qquad R_4=300\ \Omega
\\]

\\[
C_1=330\ \mathrm{pF} \qquad C_2=1.5\ \mathrm{nF}
\\]

we obtain

\\[
a=1.275\times10^{-6}\ \mathrm{s} \qquad b=3.267\times10^{-13}\ \mathrm{s^2}
\\]

Factoring \\(1+as+bs^2=(1+s\tau_1)(1+s\tau_2)\\) gives

\\[
\tau_{1,2}=\frac{a\pm\sqrt{a^2-4b}}{2}
\\]

\\[
f_{z1}=\frac{1}{2\pi\tau_1}\approx173\ \mathrm{kHz} \qquad f_{z2}=\frac{1}{2\pi\tau_2}\approx448\ \mathrm{kHz}
\\]

These are the poles of the passive feedback network and the zeros of the idealized locally closed-loop gain. Because the two RC sections load each other, their frequencies cannot be calculated independently as \\(1/(2\pi R_3C_1)\\) and \\(1/(2\pi R_4C_2)\\).

## THX AAA 789
![THX AAA 789 Front](images/THX_AAA_789_Front.jpg)

The Massdrop × THX AAA 789 was launched in 2018 at US$349.99. Developed jointly by Massdrop and THX and sold through Massdrop, it became a landmark by combining high output power with exceptionally low distortion at an accessible price. THX specified up to 6 W per channel into 32 ohms through its bridged output, and THD as low as 0.00001% at 100 mW into 300 ohms. It provided a prominent showcase for THX’s Achromatic Audio Amplifier technology, which uses feed-forward error correction to reduce distortion. The same technology family also appeared in Benchmark’s HPA4, SMSL’s SP200 and SP400, and products from FiiO.

Feed-forward error correction technology has a long history to tell. Harold S. Black, working at Bell Telephone Laboratories in the late 1920s, developed both negative-feedback and feed-forward error-correction concepts. In a feed-forward system, the error produced by a main amplifier is extracted, amplified separately, and then injected into the output with opposite polarity so that the distortion is cancelled rather than reduced. 

QUAD adapted this principle to audio power amplification in the 1970s. Peter Walker and Michael Albinson introduced the term current dumping for an architecture in which a small, highly linear amplifier controls the output voltage while a much more powerful Class-B output stage supplies most of the load current. This approach became the basis of the QUAD 405 amplifier. 

THX patented a feed-forward error-correction concept that avoids the balancing inductor used in the QUAD approach. The Schematic of THX patent is shown as below, it is probably also the schematic of THX AAA 789 headphone amplifier:

![THX AAA Schematics](images/THX_AAA_789_concept.svg)

The original design use OPA1602 and OPA564, but I don't have the models of both, so I use the combination of Topping A90, which makes these two topology comparable. The concept is complicated, to understand that, we have to start from the beginning.

### Current Dumping Concept

![Current Dumping Parallel](images/Current_Dumping_Parallel.svg)

If we parallel a precision op-amp as error-correction amp and a high-current op-amp as power amp, with different output resistors, the output current will be allocated by the raio of R1/R3, in our case 1/100.

If the power amp contribute some error/distorion, the error-correction amp can help fix it, but it needs a way to sense that error. We need to understand wheatstone bridge first. In a balanced wheatstone bridge, whatever voltage signal applied, the voltage of Point A and B will be identical.

#### Wheatstone Bridge

![Wheatstone Bridge](images/Wheatstone_Bridge.svg)

If we use point A as output, use point B as feedback, this is a wheatstone style current dumping amplifier. 

![THX AAA Circuit in wheatstone bridge](images/THX_AAA_Wheatstone_Bridge.svg)

#### Wien Bridge

If we use a inductor to replace R1, and a capacitor to replace R2, the bridge is still balance, though the dividing ratio will change over frequency. It is called Maxwell Wien bridge, and Quad 405 used such bridge.

![Maxwell Wien Bridge](images/Wien_Bridge.svg)

Unlike a Wheatstone bridge made only from resistors, a Maxwell-Wien bridge contains reactive components, so we describe each bridge arm by its impedance \\(Z(s)\\), rather than by a resistance alone. For sinusoidal analysis, \\(s=j\omega\\), where \\(\omega=2\pi f\\).

The impedances of an ideal inductor and capacitor are

\\[
Z_L=sL \qquad Z_C=\frac{1}{sC}
\\]

The bridge-balance condition itself does not change.

\\[
Z_1Z_2=Z_3Z_4
\\]

\\(R_1\\) is replaced by an inductor and \\(R_2\\) by a capacitor, while \\(R_3\\) and \\(R_4\\) remain resistive. Therefore,

\\[
Z_1=sL \qquad
Z_2=\frac{1}{sC} \qquad
Z_3=R_3 \qquad
Z_4=R_4
\\]

Substituting these impedances into the balance condition gives

\\[
(sL)\left(\frac{1}{sC}\right)=R_3R_4
\\]

The \\(s\\) terms cancel, leaving

\\[
\frac{L}{C}=R_3R_4
\\]

In our example

\\[
R_3=22\ \Omega \qquad R_4=1\ \mathrm{k\Omega}
\\]

then

\\[
R_3R_4=22\times1000=22\,000\ \Omega^2 
\\]

Choosing standard component values

\\[
L=3.3\ \mu\mathrm{H} \qquad C=150\ \mathrm{pF}
\\]

gives

\\[
\frac{L}{C}
=\frac{3.3\times10^{-6}}{150\times10^{-12}}
=22\,000\ \Omega^2
\\]

so the bridge is ideally balanced. The two voltage-division ratios change together, keeping the voltage difference between points A and B at zero under the bridge-balance condition. 

L1 as output indcutor isolates load capacitance, C1 as feedback compensate capacitor stables the error correction amplifier, this is a very convenient way to build a speaker amplifier. 

However accurate bridge balance is critical to distortion cancellation in a current-dumping amplifier. Matching inductor, capacitor and resistors are much harder than matching 4 resistors alone, consider their tolerance and parasitic effects.

#### THX Patent's Bridge

In headphone amplifier desing, if we want to keep the compensate capacitor while drop the inductor. THX giving a new bridge style in its patent: US8004355B2, Low dissipation amplifier. 

![THX AAA Patent Bridge](images/THX_AAA_Bridge.svg)

In this RC bridge, using the same arm numbering as before, their impedances are

\\[
Z_1=R_1 \qquad Z_2=\frac{1}{sC_2}
\\]

\\[
Z_3=R_3\parallel\frac{1}{sC_1}
=\frac{R_3}{1+sR_3C_1}
\\]

\\[
Z_4=R_4+\frac{1}{sC_4}
=\frac{1+sR_4C_4}{sC_4}
\\]

The bridge is balanced when the voltages at points A and B are equal. The balance condition remains

\\[
Z_1Z_2=Z_3Z_4
\\]

Substituting the four impedances gives

\\[
\frac{R_1}{sC_2} = \frac{R_3}{1+sR_3C_1} \cdot \frac{1+sR_4C_4}{sC_4}
\\]

Rearranging,

\\[
R_1C_4(1+sR_3C_1) = R_3C_2(1+sR_4C_4)
\\]

For this equality to hold across frequency, both the constant terms and the coefficients of \\(s\\) must match. This gives two conditions:

\\[
R_1C_4=R_3C_2
\\]

and

\\[
R_3C_1=R_4C_4
\\]

The second condition means that the parallel RC network and the series RC network must have the same time constant. When these time constants match, their frequency-dependent factors cancel.

For the values shown in the diagram, the time constants are

\\[
R_3C_1=22\times100\times10^{-9}=2.2\ \mu\mathrm{s}
\\]

and

\\[
R_4C_4
=1000\times2.2\times10^{-9}
=2.2\ \mu\mathrm{s}.
\\]

Therefore, the bridge is ideally balanced. Although the voltage-division ratios change with frequency, they change together, keeping points A and B at the same voltage. 

But this amplifier need a DC feedback path to stable its opeartion point. For unity gain setting, add a feedback resistor between 1K~10K. If you want some gain, note Z4 is a high pass filter, so the feedback network need to be a low pass filter to flat the response.


![THX AAA Schematics](images/THX_AAA_789.svg)

Using the component labels from our simulation, \\(R_2\\) , \\(R_5\\), and \\(C_3\\) form a low-pass filter. Resistor \\(R_7\\) connects the inverting input to ground. 

For the following calculation, we assume sufficient amplifier loop gain and neglect the small voltage drop across \\(R_1\\) and the contribution of \\(C_2\\) around the RC transition. 

At DC, the capacitors are open, and \\(R_2\\) and \\(R_5\\) form a series feedback resistance. The closed-loop gain is approximately

\\[
G_{\mathrm{DC}}\approx1+\frac{R_2+R_5}{R_7}.
\\]


\\[
G_{\mathrm{DC}}\approx1+\frac{1000+1000}{1000}=3.
\\]

Above the RC transition, \\(C_3\\) increasingly holds the midpoint near AC ground, so \\(R_5\\) acts in parallel with \\(R_7\\). Meanwhile, the impedance of \\(C_4\\) becomes small compared with \\(R_4\\). Before other high-frequency effects become significant, the gain therefore approaches

\\[
G_{\mathrm{upper}}\approx1+\frac{R_4}{R_7\parallel R_5}.
\\]

To match the lower and upper gains, we require

\\[
\frac{R_2+R_5}{R_7}=\frac{R_4}{R_7\parallel R_5},
\\]

or

\\[
R_4=\frac{R_5(R_2+R_5)}{R_7+R_5}.
\\]

Our values satisfy this condition:

\\[
R_4=\frac{1000(1000+1000)}{1000+1000}=1\ \mathrm{k\Omega},
\\]

giving

\\[
G_{\mathrm{upper}}\approx1+\frac{1000}{500}=3.
\\]

Matching the gains is not enough; the transition frequencies must also match. In this simplified model, the T-network time constant is \\((R_2\parallel R_5)C_3\\), so we choose

\\[
(R_2\parallel R_5)C_3=R_4C_4=R_3C_1.
\\]

The bridge time constant is

\\[
R_4C_4=1000\times2.2\times10^{-9}=2.2\ \mu\mathrm{s},
\\]

corresponding to

\\[
f_b=\frac{1}{2\pi R_4C_4}\approx72.3\ \mathrm{kHz}.
\\]

Therefore,

\\[
C_3=\frac{R_4C_4}{R_2\parallel R_5}
=\frac{2.2\times10^{-6}}{500}
=4.4\ \mathrm{nF}.
\\]


For unity gain, omit both \\(R_7\\) and \\(C_3\\), keeping the resistive feedback path from the final output. The two feedback resistors then act as one:

\\[
R_F=R_2+R_5=2\ \mathrm{k\Omega}.
\\]

## Questyle CMA800R

Questyle's original CMA800 brought another high-speed composite approach to headphone amplifiers in the early 2010s. The name stands for **Current Mode Amplifier** (电流模放大器){{#cite wang2017currentanalogamp}}. Questyle specified THD+N of 0.00038% at 1 kHz into 300 ohms, that was excellent figures of its period.

I am hasitated to classify it as composite amp or op-amp + buffer topology, however its output stage add extra gain, so I put it here as composite amplifier.

![Questyle CMA800R Front](images/Questyle_CMA800R.jpg)

It is a opamp+buffer design, but the output transistor is not driven by the output of opamp as usual. The output stage is a VCCS(voltage control current source), so voltage gain depends on the load, for load larger than 250 ohms, it adds some gain, so I still classify it as composite amplifier.  

![Questyle CMA800 Current Mode Amplifier](images/Questyle_CMA800.svg)

To better illustrate its operation, I remove the R8 protection resistor, Add voltage/current probe A, B, C, D.

![Corrent Mode Illustrated](images/Questyle_CMA_800_illustrated.svg)

Let the small-signal voltage at the op-amp booster, point A, be \\(V_A\\). Resistor \\(R_9=1.5\ \mathrm{k\Omega}\\) converts this voltage into an op-amp output current \\(I_A\approx\frac{V_A}{R_9}\\).

During the positive half-cycle, this current is drawn through the positive supply pin, \\(Q_2\\), and \\(R_2\\). The \\(Q_4\\)–\\(R_{13}\\) path operates vice versa in the negative half-cycle. 

\\(R_2\\) act as a current-sensing resistor, it converts changes in the op-amp’s supply current into a control voltage at point B. The signal voltage across \\(R_2\\) is approximately 

\\[
V_B\approx {I_A} {R_2}
\approx{V_A}\frac{R_2}{R_9}
\\]

The complementary compound pair \\(Q_1\\)-\\(Q_3\\) makes the signal voltage across emitter resistor \\(R_4\\) approximately equal to the voltage across \\(R_2\\). Therefore \\(I_C\approx\frac{V_B}{R_4}\approx I_A\frac{R_2}{R_4}\\).

Substituting \\(R_2=500\ \Omega\\) and \\(R_4=15\ \Omega\\), the approximate current gain of one half of the output stage is

\\[
\frac{I_C}{I_A}\approx\frac{500}{15}\approx33.3.
\\]

Combining this result with \\(I_A\approx V_A/R_9\\) and \\(I_C\approx I_D\\), gives the booster's effective transconductance:

\\[
g_{m,\mathrm{boost}}
=\frac{I_D}{V_A}
\approx\frac{R_2}{R_9R_4}
=\frac{500}{1500\times15}
\approx22.2\ \mathrm{mS}.
\\]

The booster's standalone small-signal voltage transfer is not fixed; it depends on the headphone impedance. It is unity gain when load is about 45\\(\Omega\\):

\\[
A_{v,\mathrm{boost}}
\approx g_{m,\mathrm{boost}}R_L
\approx\frac{R_L}{45\ \Omega}.
\\]

For example,

\\[
A_{v,\mathrm{boost}}\approx0.71\quad(R_L=32\ \Omega)
\\]

\\[
A_{v,\mathrm{boost}}\approx6.67\quad(R_L=300\ \Omega).
\\]

These figures describe only the simplified current-booster path. In the complete amplifier, global negative feedback determines the final voltage gain. From \\(R_{10}=2.2\ \mathrm{k\Omega}\\) and \\(R_7=510\ \Omega\\), gives

\\[
A_{v,\mathrm{CL}}
\approx1+\frac{R_{10}}{R_7}
=1+\frac{2200}{510}
\approx5.31,
\\]

or

\\[
20\log_{10}(5.31)\approx14.5\ \mathrm{dB}.
\\]

Questyle's manual lists a nominal gain of 15.5 dB.