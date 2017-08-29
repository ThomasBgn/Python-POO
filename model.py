class Agent:
	def say_hello(self,first_name):
		return "Bien le bonjour "+first_name +"!"

	def __init__(self,agreeableness):
		self.agreeableness = agreeableness

agent1 = Agent(0)
agent2 = Agent(10)
print(agent1.agreeableness,agent2.agreeableness)