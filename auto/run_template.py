import matplotlib.pyplot as plt
from main import make_car
from main import update
from main import calculate_desired_acceleration
from main import acceleration_to_throttle_percentage

K_P = 0.1
K_I = 0.1
K_D = 0.1
 
STEPS = 550
 
car = make_car(desired_v=20.0, dt=0.1)

velocity = []
errors = []
times = []

for step in range(STEPS):
    desire_accel, error = calculate_desired_acceleration(car, K_P, K_I, K_D)
    throttle = acceleration_to_throttle_percentage(desire_accel)
    update(car, throttle)
    velocity.append(car["v"])
    errors.append(error)
    times.append(car["t"])

# bruh matlab easier than this
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
