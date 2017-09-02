#création de la classe.
class Agent:

	#première fonction pour dire bonjour.
	def say_hello(self,first_name):
		return "Bien le bonjour "+first_name +"!"

	#seconde fonction, ici on travaille avec le dictionnaire "agent_attributes".
	def __init__(self, agent_attributes):
		#création d'une boucle pour récupérer l'ensemble des attributs et de leurs valeurs.
		#fin de la boucle quand tous les items de agent_attributes sont vus.
		for attr_name, attr_value in agent_attributes.items():
			setattr(self, attr_name, attr_value)

#Variable contenant le dictionnaire.
agent_attributes = {"neuroticism": -0.0739192627121713, "language": "Shona", "latitude": -19.922097800281783, "country_tld": "zw", "age": 12, "income": 333, "longitude": 29.798455535838603, "sex": "Male", "religion": "syncretic", "extraversion": 1.051833688742943, "date_of_birth": "2005-01-10", "agreeableness": 0.1441229877537559, "id_str": "LB3-3Cl", "conscientiousness": 0.2419104411765549, "internet": "false", "country_name": "Zimbabwe", "openness": -0.024607605122172617, "id": 6636726630}

#création d'un objet.
agent1 = Agent(agent_attributes)

#affichage de l'attribut désiré.
print(agent1.neuroticism)
