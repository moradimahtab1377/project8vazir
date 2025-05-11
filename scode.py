# تابع برای ایجاد یک کروموزوم تصادفی
    def random_chromosome(self):
        return random.sample(range(self.n), self.n)  
    def selection(self):
        weighted_population = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        weighted_population.sort(reverse=True)
        selected = [chromosome for fitness, chromosome in weighted_population[:self.population_size // 2]]
        return selected