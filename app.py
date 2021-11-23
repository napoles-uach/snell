import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

st.sidebar.title('Ley de Snell')
st.sidebar.markdown('''
Software didáctico diseñando
por los profesores
* D.C. José Manuel Nápoles Duarte
* M.C. Carlos Armando de la Vega Cobos

En apoyo a las materias:
Física Básica II
y
Fenómenos Electroópticos

de la Facultad de Ciencias Químicas
de la Universidad Autónoma de Chihuahua
''')

st.sidebar.image('logofcq.png')

x1=np.linspace(-10,0,500)

x2=np.linspace(0,10,500)

#n1=1.6
#n2=1.2
col1,col2,col3,col4=st.columns([4,4,5,3])
n1=col1.number_input('n1',1.0)
n2=col2.number_input('n2',1.0)
alpha1=1-1/n1
alpha2=1-1/n2
theta1=col3.slider('Ángulo de incidencia',0,89,30)
#theta1=45
theta2=np.arcsin(n1*np.sin(theta1*np.pi/180)/n2)
m=np.tan(theta1*np.pi/180)
y1=m*x1

fig, ax = plt.subplots(figsize=(4, 4))
#plt.figure(figsize=(5, 5))
m=np.tan(theta2)





#m=np.tan(theta2)
y2=m*x2
def plot_all(x1,y1,x2,y2,alpha1,alpha2):
  ax.add_patch(Rectangle((0, -10), 10, 20,alpha=alpha2))
  ax.add_patch(Rectangle((-10, -10), 10, 20,alpha=alpha1))
  ax.axis('off')
  ax.axhline(y=0,c='black',ls='--')
  ax.axes.set_xlim(-10,10)
  ax.axes.set_ylim(-10,10)
  ax.plot(x1,y1,x2,y2,c='red')
  st.write(fig)

if np.isnan(m)==False:
  plot_all(x1,y1,x2,y2,alpha1,alpha2)
  col4.write('Ángulo de refracción '+str(theta2*180/np.pi))
else:
  y2=-y1
  plot_all(x1,y1,x1,y2,alpha1,alpha2)
