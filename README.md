# **T<sub>1</suB> and PD mapping using Variable Flip Angle (VFA)**
## **Also known as Driven Equilibrium Single Pulse Observation of T<sub>1</sub> (DESPOT1)**

### **1. Data**
-   Spoiled gradient-echo (SPGR) data
    * 2 images: variable excitation angles (α)
    * Fixed repetition time (TR)
    * Fixed echo time (TE)

### **2. Inputs**
-   Signal S<sub>n</sub>(α<sub>n</sub>), for each flip angle α<sub>n</sub> (*n=1,2*).
-   Repetition time TR

### **3. Method**
Assuming a longitudinal steady-state has been reached with perfect spoiling, the signal S<sub>z</sub> (for a given voxel *z*) of a SPGR sequence is:

<div style="text-align:center">
​<img src="https://render.githubusercontent.com/render/math?math=$S_{z} = M_{0}sin{\alpha\frac{1 - \epsilon}{1 - \epsilon\cos\alpha}} \quad \textrm{where} \quad \epsilon = e^{\frac{- TR}{T_{1}}}$">
</div><br>

Which can rearranged to fit a linear form:

<div style="text-align:center">
<img src="https://render.githubusercontent.com/render/math?math=$\frac{S_{z}}{\sin\alpha} = \epsilon\frac{S_{z}}{\tan\alpha} + M_{0}( 1 - \epsilon) \quad \textrm{i.e.} \quad y = bx %2B c$">
</div><br>


If we plot
<img src="https://render.githubusercontent.com/render/math?math=$\frac{S_{z}}{\sin\alpha}"> against <img src="https://render.githubusercontent.com/render/math?math=$\frac{S_{z}}{\sin\alpha}">: <br>

![drawing](t1_pd_mapping_fig1.png)<br>
<sub>Fig. 1 - An example showing linearisation from two acquired signals</sub> <br>

Now it is clear that *ε* is equal to the line gradient *b*, from which we can gain the value of T<sub>1</sub>. And, the intercept *c*, from which we can gain the value of M<sub>0</sub> (Proton Density - PD). The gradient can be calculated as follows:

<div style="text-align:center">
<img src="https://render.githubusercontent.com/render/math?math=b = \epsilon = \frac{\frac{S_{z}(a_{2})}{\sin a_{2}} - \frac{S_{z}(a_{1})}{\sin a_{1}}}{\frac{S_{z}( a_{2})}{\tan a_{2}} - \frac{S_{z}(a_{1})}{\tan a_{1}}} \quad \textrm{i.e.} \quad b = \frac{y_{2} - y_{1}}{x_{2} - x_{1}})">
</div><br>

After which, the intercept can be calculated via substitution of one of the signal points:

<div style="text-align:center">
<img src="https://render.githubusercontent.com/render/math?math=c = M_{0}(1 - \epsilon) = \frac{S_{z}}{\sin\alpha} - \epsilon\frac{S_{z}}{\tan\alpha} \quad \textrm{i.e.} \quad c = y - bx)">
</div><br>

We are then able to gain our T<sub>1</sub> mapping and M<sub>0</sub> as:

<div style="text-align:center">
<img src="https://render.githubusercontent.com/render/math?math=T_{1} = \frac{-TR}{\ln(b)}, \quad M_{0} = \frac{c}{1 - b}">
</div>

### **4. References**

1.  Deoni, S. C. L., Williams, S. C. R., Jezzard, P., Suckling, J.,
    Murphy, D. G. M., & Jones, D. K. (2008). Standardized structural
    magnetic resonance imaging in multicentre studies using quantitative
    T1 and T2 imaging at 1.5 T. NeuroImage, 40(2), 662--671.
    <https://doi.org/10.1016/j.neuroimage.2007.11.052>

2.  Helms, G., Dathe, H., & Dechent, P. (2008). Quantitative FLASH MRI
    at 3T using a rational approximation of the Ernst equation. Magnetic
    Resonance in Medicine, 59(3), 667--672.
    https://doi.org/10.1002/mrm.21542

3.  Lee, Y., Callaghan, M. F., & Nagy, Z. (2017). Analysis of the
    precision of variable flip angle T1mapping with emphasis on the
    noise propagated from RF transmit field maps. Frontiers in
    Neuroscience, 11(MAR). <https://doi.org/10.3389/fnins.2017.00106>

4.  Maier, O. (2016). T 1 -mapping from variable flip angle data
    utilizing constrained model-based reconstruction.
