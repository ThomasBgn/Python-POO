import json
#création de la classe.
class Agent:

	#première fonction pour dire bonjour.
	def say_hello(self,first_name):
		return "Bien le bonjour "+first_name +"!"

	#seconde fonction, ici on travaille avec le dictionnaire "agent_attributes".
	def __init__(self, **agent_attributes):
		#création d'une boucle pour récupérer l'ensemble des attributs et de leurs valeurs.
		#fin de la boucle quand tous les items de agent_attributes sont vus.
		for attr_name, attr_value in agent_attributes.items():
			setattr(self, attr_name, attr_value)

#fonction de lancement.
def main():
	#pour chaque agent présent dans "agents-100k.json" créer un agent avec la methode agent_attributes.
	#afficher l'item agreeableness de chaque agent
	for agent_attributes in json.load(open("agents-100k.json")):
		agent = Agent(**agent_attributes)
		print(agent.agreeableness)

main()
