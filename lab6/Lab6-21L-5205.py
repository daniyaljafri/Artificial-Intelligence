import random

class NQueensGeneticSolver:
    def __init__(self, board_size, population_size, mutation_rate):
        self.board_size = board_size
        self.population_size = population_size
        self.mutation_rate = mutation_rate

    def generate_board(self):
        return [random.randint(0, self.board_size-1) for _ in range(self.board_size)]

    def fitness(self, board):
        conflicts = 0
        for i in range(len(board)):
            for j in range(i+1, len(board)):
                if board[i] == board[j] or abs(i-j) == abs(board[i]-board[j]):
                    conflicts += 1
        return conflicts

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, self.board_size - 2)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def mutate(self, board):
        if random.random() < self.mutation_rate:
            index = random.randint(0, self.board_size - 1)
            board[index] = random.randint(0, self.board_size - 1)
        return board

    def solve(self, max_generations):
        population = [self.generate_board() for _ in range(self.population_size)]
        for generation in range(max_generations):
            population = sorted(population, key=lambda x: self.fitness(x))
            if self.fitness(population[0]) == 0:
                return population[0], generation
            new_population = [population[0]]
            while len(new_population) < self.population_size:
                parent1, parent2 = random.choices(population[:self.population_size // 2], k=2)
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.extend([child1, child2])
            population = new_population
        return None, max_generations


board_size = 6
population_size = 10
mutation_rate = 0.1
max_generations = 1000

solver = NQueensGeneticSolver(board_size, population_size, mutation_rate)
solution, generations = solver.solve(max_generations)

if solution:
    print("Solution found in {} generations:".format(generations))
    print(solution)
else:
    print("No solution found within {} generations".format(max_generations))
