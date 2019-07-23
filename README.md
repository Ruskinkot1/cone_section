# cone_section
A machine learning model for determination of a conic section type
In mathematics, a conic section is a curve obtained as the intersection of the surface of a cone with a plane. 
The three types of conic section are the hyperbola, the parabola and the ellipse. 
Algebraically it can be written as Ax2+Bxy+Cy2+Dx+Ey+F=0, where not all of A, B and C are zero. 
If the conic section is non-degenerate, it can be classified in terms of the value B^2-4AC called discriminant:
Ellipse if B^2-4AC<0.
Parabola if B^2-4AC=0.
Hyperbola if B^2-4AC>0.

In this work we created model, which predicts type of cone section according to it's specific coefficients A, B and C.
Model accuracy found to be 98.7% for ellipse, 98.6% for parabola and 99.9% for hyperbola using K-nearest neighbourhood algorithm
