import numpy as np
import matplotlib.pyplot as plt

# Function to generate some points
def generate_points(num_points=100):
    np.random.seed(0)
    x = np.arange(0, 10, 0.1)
    x = np.expand_dims(x, 1)
    noise = np.random.randn(*x.shape)
    y = 5*x+10 + noise
    points = np.concatenate((x,y), axis=1)

    return points

def compute_SSE_for_line_given_points(a, b, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (a * x + b)) ** 2
    return totalError / float(len(points))

def step_gradient(a_current, b_current, points, learning_rate):
    a_gradient = 0
    b_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        a_gradient += -(2/N) * (x * (y - ((a_current * x) + b_current)))
        b_gradient += -(2/N) * ((y - ((a_current * x) + b_current)))
    new_a = a_current - (learning_rate * a_gradient)
    new_b = b_current - (learning_rate * b_gradient)
    return [new_a, new_b]

def gradient_descent_runner(points, starting_a, starting_b, learning_rate,
                            num_iterations):
    a = starting_a
    b = starting_b
    loss = []
    for i in range(num_iterations):
        a, b = step_gradient(a, b, np.array(points), learning_rate)
        loss.append(compute_SSE_for_line_given_points(a, b, points))

    return a, b, loss

# Generate some example points
points = generate_points()

# Parameters
initial_a = 20  # initial slope guess
initial_b = 30  # initial y-intercept guess
learning_rate = 0.008  # learning rate
num_iterations = 50000 # number of iteration, epoch

print("Starting gradient descent at a = {0}, b = {1}, error = {2}".format(initial_a, initial_b,
compute_SSE_for_line_given_points(initial_a, initial_b, points)))
print("Running...")
a, b , loss = gradient_descent_runner(points, initial_a, initial_b, learning_rate, num_iterations)
print("After {0} iterations a = {1}, b = {2}, error = {3}".format(
    num_iterations, a, b, compute_SSE_for_line_given_points(a, b, points)))
print(len(loss))

# Extract x and y from points for plotting
x = points[:, 0]
y = points[:, 1]

# Plot the points and the fitted line
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.scatter(x, y, color='blue')
plt.plot(x, a * x + b, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression with Gradient Descent')

# Plot the loss graph
plt.subplot(1, 2, 2)
plt.plot(range(num_iterations), loss, label='Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss over Epochs')
plt.legend()

plt.tight_layout()
plt.show()