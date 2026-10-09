import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

#Different gains for control scheduling
K_P1 = 0.5
K_I1 = 0.025
K_D1 = 0.5

K_P2 = 0.5
K_I2 = 0.01
K_D2 = 0.5

K_P3 = 0.4
K_I3 = 0.005
K_D3 = 0.6

K_P4 = 0.5
K_I4 = 0.0025
K_D4 = 0.5

K_P5 = 0.5
K_I5 = 0.0015
K_D5 = 0.6
 
STEPS = 550
 
car = make_car(desired_v=20.0, dt=0.1)

velocity = []
errors = []
times = []

for step in range(STEPS):
    if car["desired_v"] <= 20:
        desire_accel, error = calculate_desired_acceleration(car, K_P1, K_I1, K_D1)
    elif car["desired_v"] <= 40:
        desire_accel, error = calculate_desired_acceleration(car, K_P2, K_I2, K_D2)
    elif car["desired_v"] <= 60:
        desire_accel, error = calculate_desired_acceleration(car, K_P3, K_I3, K_D3)
    elif car["desired_v"] <= 80:
        desire_accel, error = calculate_desired_acceleration(car, K_P4, K_I4, K_D4)
    elif car["desired_v"] <= 100:
        desire_accel, error = calculate_desired_acceleration(car, K_P5, K_I5, K_D5)
    else:
        ## Helps catch any errors if car is past 100
        raise ValueError("Has to be between 0-100 for this 1D Model")
    ## desire_accel, error = calculate_desired_acceleration(car, K_P, K_I, K_D)
    throttle = acceleration_to_throttle_percentage(desire_accel)
    update(car, throttle)
    velocity.append(car["v"])
    errors.append(error)
    times.append(car["t"])


plt.figure(1)
plt.plot(times, velocity)
plt.title('Velocity over Time')
plt.xlabel('Time')
plt.ylabel('Velocity')

plt.figure(2)
plt.plot(times, errors)
plt.title('Error over Time')
plt.xlabel('Time')
plt.ylabel('Error')
plt.show()


#Hello! :)