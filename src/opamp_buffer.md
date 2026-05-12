# Chapter 2

An op-amp with a current buffer is a very common approach in headphone amplifier design. The op-amp guarantees baseline performance and saves a lot of PCB space. The current buffer can be either an IC or a discrete stage: IC buffers simplify the design, while discrete buffers can achieve the highest performance.

## The wire headphone amplifier

The Wire headphone amplifier was published on diyaudio by opc in 2010. It is extremely simple yet offers ultra-high performance, with THD+N down to 0.0005%.

![The wire headphone amplifier](images/The%20Wire.svg)

Note: 
$$ R1 \parallel R2 = R3 \parallel R4 $$

The equal resistances on both inputs ensure that the input bias currents produce identical bias voltages, thereby minimizing the output offset voltage. This is particularly important when using BJT-input op-amps. 

Also note that the LME49600 output buffer has about 100 MHz bandwidth. When driving capacitive loads at high frequency, it can add significant phase lag, so avoid pairing it with an excessively high-GBW op-amp unless compensation is verified.

## The Graham Slee SOLO Headphone Amplifier
This is an old-fashioned headphone amplifier that is especially suitable for driving the Sennheiser HD600/HD650 (and likely the HD660S2). Its measured performance is often debated, but in practice it drives these older Sennheiser headphones very well.

There are many SOLO versions; the one shown here is the latest SOLO ULDE version.

![Graham Slee SOLO](images/Graham%20Slee%20SOLO.svg)

There are two purposes for the output resistor R17:
1. Standard 6.35 mm gauge A connectors can momentarily short channels to ground during insertion and removal. Without R17, the short-circuit current through BC337/BC327 can become excessive and exceed safe operating limits.
2. It isolates the parasitic capacitance of the headphone cable and driver, improving phase margin.

R15/R16 are emitter degeneration resistors, and they also serve two purposes:
1. They reduce thermal runaway risk when the bias diodes are not thermally coupled to the output transistors. In this case, a practical minimum value is about 3.3 ohms.
2. They help the output transistors to turn off during Class AB operation.

Some designers dislike output resistors and degeneration resistors. If the bias diodes are thermally coupled to the output transistors, or if a FET output stage is used, degeneration resistors can be removed. However, an output resistor is still useful for protecting the output stage from the inherent shorting risk of headphone connectors.

Although it is listed on the official website as opearting in Class AB, it is actually operating in Class A at normal listening levels with HD600/HD650 loads. With lower-impedance headphones, it moves toward Class B operation and distortion rises quickly. This may explain why user opinions are polarized.

## Beyerdynamic A1 Headphone Amplifier
This is another veteran headphone amplifier, designed by Beyerdynamic to drive its DT880/DT990 headphones.

![Beyerdynamic A1](images/Bayerdynamic%20A1.svg)

It is a Class A design. The output bias current is about 50 mA, which is just enough to drive 300-ohm DT880 headphones at maximum output. It uses simple diode (LED) biasing without thermal coupling, so it needs a higher degeneration resistor value; therefore, no need for output resistor unlike SOLO.

It is worth mentioning that the lower-end Beyerdynamic A20 uses essentially the same topology as the A1, but adds an output resistor that increases output impedance. This can be reversed by bypassing that resistor with a jumper, I believe such modification can significantly improve its performance(modification at your own risk).

The measured distortion of the MC33078 is around 0.003%, so op-amp rolling may significantly improve performance too. If you roll op-amps, choose parts with similar GBW and phase margin to the MC33078, because C1/C2/C4 form a deliberate compensation network.

The op-amp is configured for inverting gain. For many older op-amps with only moderate CMRR, this can produce lower distortion than a non-inverting setup. With modern audio op-amps that have very high CMRR, inverting configuration is less necessary.

An input buffer is added because, in an inverting topology, a 2 kΩ input resistor (R9) presents too heavy a load for typical CD/DAC outputs. If R9 is increased to 47 kΩ, the feedback resistor must exceed 200 kΩ to keep the same gain, which raises resistor noise to an audible level.

## Lehmann Audio Linear Headphone Amplifier
This is another old-fashioned headphone amplifier that pairs well with HD600/HD650.

![Lehmann Audio Linear](images/Lehmann%20Linear.svg)

It uses a diamond buffer output stage, where the output bias current is set by resistor ratios (R8/R3 and R9/R4). This is different from the simpler diode-biased output stages in SOLO/A1, where bias current is harder to set precisely.

The output stage is outside global feedback loop, so low distortion depends heavily on Class A operation. Their website claims of "no global feedback" can be misleading: the op-amp itself is a multi-stage amplifier, so feedback of op-amp is already global feedback.

However, this topology simplifies stability analysis. If the op-amp is stable, the amplifier is usually stable, so fewer compensation capacitors are needed compared with SOLO/A1.

Finally, it is worth mentioning that it uses the audio-grade op-amp(Ti OPA2134), with typical distortion around 0.00008%, which was state-of-the-art for its era.

