# Chapter 6

## Maida Power Supply
Almost all tube headphone amplifiers suffer from low PSRR (power-supply rejection ratio), so they need a precision power supply with extremely low ripple.

The Maida power supply {{#cite maida1980highvoltageadjustablepowersupplies}} suits this need. Tom Christiansen also suggests a modern design that uses up-to-date components and delivers better performance.

![21st Century Maida Power Supply](images/21st_century_maida_reg.svg)

[Michael Maida's original regulator](https://www.ti.com/lit/an/snva583/snva583.pdf) uses a floating three-terminal regulator behind a high-voltage pass device. The regulator IC sees only a small input-to-output voltage, while the pass device withstands most of the B+ voltage. This makes it possible to regulate supplies of several hundred volts without applying the full voltage across the low-voltage regulator IC.

[Tom Christiansen's 21st Century Maida](https://www.diyaudio.com/community/threads/21st-century-maida-regulator.209067/) retains this principle but replaces the LM317 with an LT3080 and uses a high-voltage MOSFET cascode. The LT3080 requires less minimum-load current and has lower dropout, reducing dissipation in the feedback network. Soft start and protection diodes improve behavior during startup, shutdown, and load transients; Christiansen reported about 20 uV RMS of output ripple and noise with 50 V peak-to-peak ripple at the input.
