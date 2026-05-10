# Chapter 1

Like a story that begins with its ending, we will start this book with the ultimate answer. We will look at the most advanced and best-measuring circuit of the 21st century first. If your only goal is to build the "Best Headphone Amplifier" right now, this chapter is all you need. After this, we will travel back in time to explore the older, classic designs that led us here.

Composite Amplifer has many alias, Topping calls their composite amp "NFCA" (Nested Feedback Composite Amplifier). Other brand 

The idea of composite amp is rather simple, combine two amplifier together so it has more gain for deeper feedback, and distortion, bandwith, noise, output impedance will all benefit. The only concern is oscilation, each amp got its own dominent pole, one pole will cause 90° phase shift, two amps got two poles, the phase shift reachs 180° will cause oscilation, so zeros and poles must carefully configured to make a composite amp stable.

The simplest way to build a composite amplifier is to use a slow amp to drive a fast amp. This configuration is inherently stable because the slow amp's gain drops below zero dB before the fast amp introduces significant phase shift. To explain this non-technically, imagine the relationship between a driver (the first amp) and a vehicle (the second amp). If you pilot a massive vehicle that only reacts seconds after you turn the wheel, steering a straight path becomes incredibly difficult. Your constant overcorrecting and steering back and forth is the mechanical equivalent of an amplifier oscillating. Conversely, if the vehicle's response is faster than the driver's reflexes, the driver perceives no delay, no overcorrection happens, which equivalent to a stable amp.

## Topping A90
The first amp introduced is Topping A90 Headphone amplifier, it use an OPA1612 to driver 2 TPA6120A2 in one package for each channel. The topology is shown below:

![Topping A90 Schematic](images/topping_a90.svg)

Since topping A90 set the gain of the second amp to be 1, so it is simpler to treat the second amp a low distortion output stage as it only use its gain to correct it own output error. OPA1612 claims 40Mhz GBW, TPA6120 didn't claims its GBW on its datasheet, but we know it is basicly THS6012, which has 315Mhz GBW. So the second amp will bring 45° phase lag at about 300Mhz in theory. The gain of the first amp is far below zero at that frequency, because its GBW is only 40Mhz. Theoreticlly it is stable inherently.

In real world, parasite capacitance of headphone and its wire may worse the amp stability, a zobel network is placed at the output. And C1\C2 together form a 1st order low-pass filter to better stable the amp.

The Successor model A90 Discrete is still the same topology, a classic op-amp drive a current-feedback op-amp, but use discrete component to build each amps. I may add its schematic in later version.

## Turbocharged Audio Amplifier
By placing the voltage gain of the second amp inside the global feedback loop, the composite amp leverages the combined open-loop gain (A1×A2) for deep global error correction, rather than limit the second amp's gain to 1, treat it as a output stage. I have not find any design example of such headphone amplifier, however an LM1875 based "Turbocharged audio amplifer" if proposed by Kitchin et al.  {{#cite kitchin1992turbocharged}}.

![Turbocharged Audio Amplifier](images/Turbocharged_LM1875.svg)

R1,R2 and C1 form a phase-leading network, which make a zero at $$ f_z = \frac{1}{2 \pi R_1 C_1} $$, then consequently there is a pole at a higher frequency $$ f_p = \frac{1}{2 \pi (R_1 \parallel R_2) C_1} $$ 

It is designed for speakers, but can definitely use for headphone, due to composite design improve the noise performance of LM1875.



