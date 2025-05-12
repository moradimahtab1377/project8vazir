ی
    def random_chromosome(self):
        return random.sample(range(self.n), self.n)  
    def selection(self):
        weighted_population = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        weighted_population.sort(reverse=True)
        selected = [chromosome for fitness, chromosome in weighted_population[:self.population_size // 2]]
        return selected

 # تابع اجرای الگوریتم
    def run(self):
        for generation in range(self.generations):
            self.next_generation()
            best_fit = max(self.population, key=lambda chrom: self.fitness(chrom))
            if self.fitness(best_fit) == self.n * (self.n - 1) // 2:
