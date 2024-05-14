import numpy as np

class Particle:
    def __init__(self, num_dimensions, min_values, max_values):
        self.position = np.random.uniform(low=min_values, high=max_values, size=num_dimensions)
        self.velocity = np.zeros(num_dimensions)
        self.best_position = self.position
        self.best_fitness = float('inf')

def objective_function(x):
    # Example objective function (minimize)
    return sum(x**2)

def initialize_swarm(num_particles, num_dimensions, min_values, max_values):
    return [Particle(num_dimensions, min_values, max_values) for _ in range(num_particles)]

def update_velocity(particle, global_best_position, inertia_weight, cognitive_weight, social_weight):
    inertia_term = inertia_weight * particle.velocity
    cognitive_term = cognitive_weight * np.random.rand() * (particle.best_position - particle.position)
    social_term = social_weight * np.random.rand() * (global_best_position - particle.position)
    return inertia_term + cognitive_term + social_term

def update_position(particle, max_values, min_values):
    particle.position = np.clip(particle.position + particle.velocity, min_values, max_values)

def update_best_position(particle):
    fitness = objective_function(particle.position)
    if fitness < particle.best_fitness:
        particle.best_fitness = fitness
        particle.best_position = particle.position

def get_global_best(particles):
    return min(particles, key=lambda x: x.best_fitness).best_position

def pso(num_iterations, num_particles, num_dimensions, min_values, max_values):
    inertia_weight = 0.7
    cognitive_weight = 1.5
    social_weight = 1.5

    particles = initialize_swarm(num_particles, num_dimensions, min_values, max_values)
    global_best_position = get_global_best(particles)

    for _ in range(num_iterations):
        for particle in particles:
            particle.velocity = update_velocity(particle, global_best_position, inertia_weight, cognitive_weight, social_weight)
            update_position(particle, max_values, min_values)
            update_best_position(particle)

        global_best_position = get_global_best(particles)

    return global_best_position

# Example usage
num_iterations = 100
num_particles = 20
num_dimensions = 2
min_values = -5
max_values = 5

best_solution = pso(num_iterations, num_particles, num_dimensions, min_values, max_values)
print("Best solution found:", best_solution)
print("Objective function value:", objective_function(best_solution))
