# AI_Snake_Agent

Genetic algorithm based model for learning to play Snake.

quick explanation:

The main idea behind genetic algorithm is imitating evolution processes (Natural selection in specific).

the paradigm goes as follows:

1) Some pre defined number of agents are being anitialized.each agent is basiclly a Player consists of a name,score and
   a vanilla neural network with random parameters.for the sake of this explanation the NN is the brain of the agent,and the parametes are the agent's DNA.

2) In each generation(the number of generations is defined by the user):

    a.Each agent plays a fixed number of games(also defined by the user),after which a score is being given to him based on his performance.
    
    b.The agents with the highest scores(top 10% based on the score) are picked in order to reproduce.
    
    c.The next generation's population will consists of the children of those agents.


Player/Agent: an object cosists of few attributes and few mathodes.
    
Reproducing process: creating a new agent with the DNA(parameters) of his father+ some noise.`




