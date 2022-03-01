
# travelling salesman problem using genetic algorithm
import random
#chromosome is a single string representing sequence path of visiting all cities
# eg : chromosome 012430 is called gnome and represents path 0->1->2->4->3->0
class Chromosome:
  def __init__(self,length):
    self.length = length #length of chromosome
    self.gnome = self.generateGnome() # gnome string 
    self.fitness=0 
    # fitness of gnome, higher fitness more likely it is selected for generating next generations
  
  def generateGnome(self):
    gnome = "0"
    generated = ["0"]
    while (True):
      if (len(gnome) == 5):
          gnome += gnome[0]
          break
      
      temp = random.randint(0,self.length-1)
      if str(temp) not in generated:
          gnome += str(temp)
          generated.append(str(temp))
    return gnome

  def calc_fitness(self,graph):
    # fitness of a gnome is the length of path represented by the gnome string
    # if path does not exist then set path as infinity
    # lower the value better it the fitness
    f=0
    INT_MAX = 2147483647
    list_genes = self.gnome
    for i in range(len(list_genes)-1):
      if(graph[int(list_genes[i])][int(list_genes[i+1])]==INT_MAX):
        self.fitness =  INT_MAX
        return
      f+=graph[int(list_genes[i])][int(list_genes[i+1])]
    self.fitness=f
  
  def mutate(self):
    #mutation happens and resulting gnome is of next generation 
    #mutation is nothing but swaping any 2 random charecters of the string
    while(True):
      first = random.randint(1,self.length-2)
      second = random.randint(1,self.length-2)
      list_gnome = list(self.gnome)
      if(first!=second):
        temp = list_gnome[first]
        list_gnome[first] = list_gnome[second]
        list_gnome[second] = temp
        break
    self.gnome = ''.join(list_gnome)

class TSP:
  def __init__(self,graph):
    self.graph = graph
    self.temperature = 1000 # a threshold,decreses after each iteration
    self.gen_threshold = 10 # max no of generations
  
  #generate random population
  def generate_population(self,pop_count):
    population = []
    for i in range(0,pop_count):
      chromosome = Chromosome(len(self.graph))
      chromosome.calc_fitness(self.graph)
      population.append(chromosome)
    return population

  def cooldown(self):
    self.temperature =  (90*self.temperature)/1000
  
  def print_population(self,population,generation):
    print("GENERATION " + str(generation) + "....")
    print("population   fitness_value")
    for gnome in population:
      print(gnome.gnome + "    " + str(gnome.fitness))
  
  def run(self):
    generation=1
    population = self.generate_population(5)
    self.print_population(population,generation)
  
    while(self.temperature<=1000 and generation<=self.gen_threshold):
      population = sorted(population,key=lambda x : x.fitness) 
      #arrange gnomes in ascending order of fitness
      #lower the value of fitness better it is
      new_population = []

      for i in range(0,len(population)):
        chromosome = population[i]
        while(True):
          new_chromosome = chromosome
          new_chromosome.mutate()
          new_chromosome.calc_fitness(self.graph)
          if new_chromosome.fitness <= chromosome.fitness:
            new_population.append(new_chromosome)
            break
          else :
            prob = pow(2.7,-1 * ((new_chromosome.fitness - population[i].fitness) / self.temperature))
            if prob > 0.5:
              new_population.append(new_chromosome)
              break
      population = new_population
      self.cooldown()
      generation+=1
      self.print_population(population,generation)

INT_MAX = 2147483647
graph = [
  [0, 2, INT_MAX, 12, 5],
  [2, 0, 4, 8, INT_MAX],
  [INT_MAX, 4, 0, 3, 3],
  [12, 8, 3, 0, 10],
  [ 5, INT_MAX, 3, 10, 0]
]
TSP(graph).run()

