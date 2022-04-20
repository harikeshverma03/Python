# -*- coding: utf-8 -*-
"""
Created on Tue Dec 4 17:18:38 2022

@author: Jakub
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# Input function
#modeling the initiator of the bump input
def sin_input(t, y_in, tstart, y_start_end, tend):

    y = y_in #initial y values
   
    index_start = np.where(t == tstart)[0][0] #index - position of the start (when should the bump start?)
    index_end   = np.where(t == tend)[0][0] #index - position of the end (when should the bump end?)

    length_difference = index_end - index_start              
    
    #characteristics of the sin function, that represent the bump
    frequency = 0.005  #number of bumps #the frequency coeff is just randomly found number, so it is only one bump
    amplitude = 0.08  # Road height (in meters)
    #creating the sin function 
    for i in range(0,length_difference+1): 
 
        index = index_start + i    
        y[index] = -amplitude * np.sin(2 * np.pi * frequency * i )   
  
    return y   


# A function containing the system model which will be called by odeint
def Suspension_analysis(X, t, sprung_mass, unsprung_mass, spring_stiffness, damping_coeff, tire_stiffness, road_profile):
    
    unsprung_displacement = X[0]
    unsprung_speed = X[1]
    sprung_displacement = X[2]
    sprung_speed = X[3]
    
    g  = 9.81 #gravity acceleration in m\s^2
    tire_radius = 0.35         # Tire radius in meters
    spring_free_length = 0.45         # Free length of spring in meters
    
    ends_suspension_displacement = (unsprung_displacement - sprung_displacement + spring_free_length)     # Relative displacment of both ends of suspension
    ends_suspension_velocity = unsprung_speed - sprung_speed # Relative velocity for suspension ends in vertical direction
    road_wheel_displacement = road_profile - unsprung_displacement + tire_radius   # Relative vertical displacement of Road and wheel
    
    suspension_force = (spring_stiffness * ends_suspension_displacement + damping_coeff * ends_suspension_velocity)      # Suspension force
    tire_force = (tire_stiffness * road_wheel_displacement)                     # Tire force or wheel force
    
    
    unsprung_acceleration = (1/unsprung_mass) * (tire_force - suspension_force - (unsprung_mass*g))
    sprung_acceleration = (1/sprung_mass) * (suspension_force - (sprung_mass*g))
    
    return unsprung_speed, unsprung_acceleration, sprung_speed,sprung_acceleration

      

if __name__  == '__main__':
    print("---------------- Suspension Analysis ------------------------------------------")     
 
    sprung_mass= 450 #Sprung Mass in Kg
    unsprung_mass = 60 #Unsprung Mass in Kg
    spring_stiffness = 10000 #Spring stiffness N/m
    damping_coeff = 3000    #Damping coefficient Ns/m
    tire_stiffness = 13000 #Stiffness of tire N/m
    
    # Simulation start time, end time, step size and time span are declared here together with the coefficients for the input function
    sim_start = 0    #Simulation start time (sec)
    sim_end = 5      #Simulation end time (sec)
    step_size = 0.01 #Simulation step size 
    
    num_steps = int((sim_end-sim_start)/step_size + 1)              
    time_span = np.linspace(sim_start, sim_end, num = num_steps)
    
    # System input is defined here  
    # Road height step input:
    tstart = 0     #Start of change of road height
    tend = 1     #End of change in road height
    ystart = 0     #Value of road height at the beginning of step input
    yend = 0.05  #Road height 

    y_initial = np.full((num_steps, 1), ystart,'float')   
    
    road_profile = sin_input(time_span, y_initial, tstart, ystart, tend)    # Create input for Road height
    
    # Collectors defined to collect the result array
    state_var = np.empty((num_steps, 4))
    acc_unsprung = np.empty((num_steps, 1))
    acc_sprung = np.empty((num_steps, 1))
   
    #Simulation loop
    
    for i in range(0, num_steps - 1):
        inputs = (sprung_mass, unsprung_mass, spring_stiffness, damping_coeff, tire_stiffness, road_profile[i])  #Inputs, where road_profile[i] is theinput from the bump  
        #####Start of the inspired code######
        y = odeint(Suspension_analysis, state_var[i], [0, step_size], args = inputs)   
        ####end of inspired code#####
        ##for odeint a inspiration was found in the following website https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html
        
        state_var[i+1] = y[-1]      # Position, velocity (integrated from velocity and acceleration)
        acc_unsprung[i+1] = state_var[:,1][i] * time_span[i]   # Acceleration = velocity * time
        acc_sprung[i+1] = state_var[:,3][i] * time_span[i] 
      
      
    # Plots #
   
    plt.figure(figsize=(8, 8))
    
    plt.subplot(4,1,1)
    plt.plot(time_span,road_profile,'k-',linewidth=1,label='Initial bump input') 
    plt.ylabel('Road Height (m)')
    plt.grid(True)
    
    plt.subplot(4,1,2)
    plt.plot(time_span,state_var[:,1],'b:',linewidth=1,label='Displacement Unsprung Mass')
    plt.plot(time_span,state_var[:,3],'r:',linewidth=1,label='Displacement Sprung Mass')
    
    plt.ylabel('Displacment (m)')
    plt.grid(True)
    
    plt.subplot(4,1,3)
    plt.plot(time_span,acc_unsprung     ,'b--',linewidth=1,label='Acceleration Unsprung Mass')
    plt.plot(time_span,acc_sprung   ,'r--',linewidth=1,label='Acceleration Sprung Mass')
   
    plt.ylabel('Acceleration (m/s^2)')
    plt.grid(True)
    
    plt.xlabel('Time')
    plt.grid(True)
    plt.savefig('Suspension_Simulation.png')
    plt.show()    
    
   
    
    