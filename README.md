# Advanced_Lab

Open-ended laboratory experiments were conducted for introduction into the world of research. 

---

## Lab 1: Cavendish Experiment: Calcuating Newtons Gravitational Constant "Big G"

The Cavendish experiment was carried out with the Pasco Gravitational Torsion Balance. This apparatus is capable of negating the effects of Earth's gravity in order to measure the gravitational forces acting on the smaller weighted spheres $m_2$, suspended on a pendulum, by the larger spheres $m_1$. For the experiment, we utilized Mathematica and video recording equipment to obtain position data of the oscillating beam reflected by the pendulum's mirror. 

We carried out **Method II: Measurement by Equilibrium Positions** from the Cavendish Pasco Manual. Equation 1.9 from the manual gives the calculation for $G$ with only 2 unknowns. These unknowns are the differences in equilibrium positions $\Delta s$ & the period $T$. The following is Eq. 1.9 and all known values:

$$
G = \pi^2 \Delta s b^2 \frac{d^2+\frac{2}{5}r^2}{T^2m_1Ld}
$$

where:

$r=9.55mm$

$d=50mm$

$b=46.5mm$
    
$m_1 = 1.5kg$

$L1= 8.80216m$ {Small Measurements and Trig relations}

$L2=8.724m$  {Single Tape Mearument}

We will also use the equation for $G_o$ on page 12 of the manual that accounts for systematic error as follows:

$$
G_o = \frac{G}{1-b}
$$


For comparison, we found the accepted value is, $G = 6.67430e-11$ from https://pml.nist.gov/cuu/Constants/.

### Conclusion 

For the four experimental runs, we carried out our closest value to the accepted $G$ value is, $G_o \approx 6.61758 \times 10^{-11} \pm 1.28143 \frac{m^3}{kg\cdot s}$, which was calculated from our first experimental run's first equilibrium position. However, this value also carries with it the second to greatest uncertainty behind data set 3's uncertainty of $0.8499 \%$. Thus, there is still some systematic error unaccounted for within the experiment. Especially when this is compared to the values from our second and fourth experimental run. We somehow found approximate values for the first and third runs, yet our second and fourth showed severe errors. This could have come from miscalculated lowering of the saddle which keeps the pendulum in place while not being used. 

### Uncertainty
The uncertainty for each $G_o$ calculation was taken from the square root of the diagonal of the covariance matrix. This means that the uncertainty for each of the fit parameters $T$, $S_1$, & $S_2$ were used within the equation for $G$. Given that $\Delta S$ is a summation then we can sum their uncertainties, but the calculation of the period is $\frac{2\pi}{\omega}$ and in $G$ the period is squared; thus we must finish our summation of uncertainties as the fractional uncertainties of $\Delta S$ & $T$. 

The uncertainty for the mass $m_1$ was found to be $\pm 10g$ as defined on page 3 of the Pasco manual, and it's percentage of uncertaitny was calculated as $\frac{10g}{1500g}\cdot100\%$. For our measurements of L we decided to use L1 which we defined as our smaller measurments of the apparatus along with trigonometric relations. We also defiend the uncertainty of this mesurement to be $\pm 0.0005$. These were also included in the calculation of the uncertainty percentage.   

With this taken into account we can see our measurement with the least uncertainty was from our fourth data set. This measurment of $G_o = 8.64524 \times 10^{-11} \pm 1.19537 \frac{m^3}{kg\cdot s}$ was roughly $29.5\%$ away from the accepted value for $G$, yet has the least uncertainty within it's mearuments. Overall, our results show that we did in fact get a measurement within $1\%$ of the accepted value. The uncertainty within the fit parameters shows that there is an error in processing the data to find the period and equilibrium positions. Also as the uncertainty was greater for the closest calculation of $G$ it can be concluded that this is not as accurate as it may appear.

---
---


## Lab 2: Two-Slit Single Photon at a Time

The Two-slit experiment utilized both a laser and a light bulb as the source of photons. For the laser measurements, voltage readings were taken to measure the interference pattern of the photons after passing the double slit within the apparatus. For the bulb, a photomultiplier tube (PMT) was used along with an oscilloscope and a pulse counter/interval timer (PCIT) in order to count the individual photons passing through the apparatus into the PMT. The PCIT was set to a $10$ $second$ interval thus each initial reading of the counts was in $\frac{counts}{10 \textit{ sec.}}$ and then converted into $\frac{counts}{1 \textit{ sec.}}$. 

### Best Fit Function

For our model, we utilized the **Fraunhofer** model presented within the lab manual. This uses the assumption that the light will act as a plane wave from an infinitely far source. This assumption is for both before and after the light passes through the double-slit. The following is the **Fraunhofer** model equation: 

$$
    I(0) = I_0(\cos{\beta})^2(\frac{\sin{\alpha}}{\alpha})^2 
$$

where:


- $\alpha = \frac{\pi a}{\lambda}\sin{\theta}$  
- $\beta = \frac{\pi d}{\lambda}\sin{\theta}$


and the following are the given constants:
- The slit-width: a = 0.085 mm
- Center-to-separation: d = 0.353 mm
- Laser wavelength:  $\lambda_{laser}$ = 0.670 $\pm$ 0.005 $\mu$ m
- Bulb wavelength:  $\lambda_{bulb}$ = 0.541 to 0.551 $\mu$ m


From this it can be assumed that the variable $\theta$ expresses the radiation pattern, yet we further this by finding the relation of:

\begin{align*}
    \theta = \arctan{\frac{x}{l}} + \phi
\end{align*}

where the position of the micrometer is $x$, the length of the chamber of travel is $l = 50$ $cm$, and $\phi$ is the phase shift parameter for the best fit.


The model was modified for the single slits by setting the Center-to-seperation distance $d=0$, as there is only one slit, which in turn makes $\beta = 0$. Using this value for $\beta$ shows that we can disregard the $\cos$ term as $(\cos{0})^2 = 1$.

### Conclusion

As we examine the first graph from our laser data we can see the diffraction pattern from the double-slit data which is a clear sign of the wave-like nature of the photons being emitted from the laser source. This of course is caused by the interference of the waves coming from either of the two slits. The peaks of the graph represent the constructive parts where both waves have joined to significantly magnify the intensity of the light, and the destructive parts are shown as the dips of the graph where the waves have fully interfered with each other causing almost no light to be measured at their respective positions. We also see the non-interference pattern from our single slit data, which shows the single wave nature which is not being interfered with by any other wave.

Next, as we examine the graph for the bulb we can see that the diffraction pattern also emerges for the single photon. As both the laser and bulb graphs are similar we can conclude the same wave-like nature for the bulb's photon emission as we had for the laser source. Where this becomes interesting is when we recognize that the bulb source is calibrated to emit single photons at a time. From this, we can now introduce the proven paradox which is the main goal of this experiment. This paradox is that we are witnessing a single photon particle, or quanta, traveling through our apparatus, and displaying wave-like behavior as it reaches the detector. Particle wave duality tells us that we can observe a photon as either a wave or as a particle, yet within this experiment, we see both the particle and wave behaviors occurring within the same time frame. Thus as we see the diffraction pattern emerge from the single photons traveling from the light source we can conclude that we have successfully proven the paradox.  

---
---


## Lab 3: Muon Decay

As cosmic rays bombard Earth, protons within these rays will collide with nuclei within the upper atmosphere. This will produce pions \& antipions which begin to decay into muons and antimuons plus either a neutrino or anti-neutrino. Thus, the muon is a sub-particle by-product of cosmic rays which hit our atmosphere. These muons will decay further into a positron or electron plus another $2$ neutrinos or anti-neutrinos. This process is illustrated below:

\begin{align*}
    \mu^+ \rightarrow e^+ \nu  \bar{\nu}\\
    \mu^- \rightarrow e^- \bar{\nu}  \nu
\end{align*}

where:

- $\mu^-$ designates the muon 

- $\mu^+$ designates the antimoun

- $e^+$ \& $e^-$ are the positron and electron respectively

- $\nu$ is the neutrinos 

- $\bar{\nu}$ is the antineutrino




The scintillator is able to stop muons with a reduced total energy of approximately $160$ $MeV$. This energy is low enough that the moun is capable of stopping within the scintillator and releasing their remaining kinetic energy of order $50$ $MeV$ in the form of a photon. This photon is then sent to the photomultiplier tube which is capable of increasing the photon, or multiplying its energy, to allow for measurements. This creates 2 successive flashes one from arrival and one from decay. However, other sources such as beta and gamma rays or even muons with total energy greater than $160$ $MeV$ will cause unwanted sources of error which can be seen as uncorrelated events that will serve as our background. 

### Conclusion

The accepted value for muon lifetime is $2.19703 \pm 0.00004$ $\mu sec$, and from our experiment, we see a value of  $2.046\pm 0.020$ $\mu sec$. We can conclude that our value was within roughly $- 6.88697$ % of the accepted value. This is with the optimized bin size of $32$ \& the optimized start time of $ 0.354$ $\mu sec$.

As our accepted value is for a vacuum, and our value comes from muons that travel within our atmosphere, we should expect our value to be lower than the accepted. Thus, our value is an excellent representation of muon decay time, and we have successfully calculated the average lifetime of muon decay.

### Other Sources of Error & Why Our Value is Lower Then the Expected Value

We know of many other sources of error such as gamma rays and beta rays from the background radiation of Earth, yet these should be filtered out by the discriminator when set properly. As our discriminator was already set up from the previous experimenters and verified that it was correct we took the assumption that this would not be a source of error. 

Yet, many of the muons that enter the scintillator have a variety of different kinetic energies that cause a variety of decay times. This can come from the muon itself being interrupted by other nuclei in the atmosphere, slowing it down to below the ideal $160$ $MeV$. We also don't know at what angle these muons enter the scintillator at, if at an angle this could also have undesired effects on the kinetic energy, and thus it would emit a photon at a significantly lower energy and yield a lower reading. 

We also did not factor in the difference between the muon and antimuon, as they are both leptons with identical masses yet the muon is a negatively charged particle while the antimuon is positively charged. These antimuons may have been picked up by the detector causing unwanted decay times.

Overall, we know that the velocity of the muon can actually determine the energy release upon arrival in the scintillator and thus impact the overall decay time. As we did not find a method to distinguish between muons with enough velocity to release a photon with an energy of $50$ $MeV$ we can assume that these slower muons could have also decreased the overall lifetime calculations.  
