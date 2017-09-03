import json
import math

#création de la classe agent.
class Agent:

	#première fonction pour dire bonjour.
	def say_hello(self,first_name):
		return "Bien le bonjour "+first_name +"!"

	#seconde fonction, ici on travaille avec le dictionnaire "agent_attributes".
	def __init__(self, position, **agent_attributes):
		self.position = position
		#création d'une boucle pour récupérer l'ensemble des attributs et de leurs valeurs.
		#fin de la boucle quand tous les items de agent_attributes sont vus.
		for attr_name, attr_value in agent_attributes.items():
			setattr(self, attr_name, attr_value)

# création de la classe Position.
class Position:

	# init cherche les longitudes et latitudes en degrés
	def __init__(self, longitude_degrees, latitude_degrees):
		# prend la latitude en degrés pour chaque objet.
		self.latitude_degrees = latitude_degrees
		# prend la lontitude en degrés pour chaque objet.
		self.longitude_degrees = longitude_degrees

	# @property permet de passer une methode en propriété.
	@property
	def longitude(self):
		# Permet de convertire la longitude en degrés en longitude en radians.
		return self.longitude_degrees * math.pi / 180

	@property
	def latitude(self):
		# Permet de convertire la latitude en degrés en longitude en radians.
		return self.latitude_degrees * math.pi / 180

#fonction de lancement.
def main():
	#pour chaque agent présent dans le dictionnaire "agents-100k.json" créer un agent avec la methode agent_attributes.
	#afficher l'item agreeableness de chaque agent
	for agent_attributes in json.load(open("agents-100k.json")):
		latitude = agent_attributes.pop("latitude")
		longitude = agent_attributes.pop("longitude")
		position = Position(longitude, latitude)
		# "**" permet de prendre les données depuis un dictionnaire.
		# si c'est un tuples il faut utiliser "*"
		agent = Agent(position, **agent_attributes)
		print(agent.position.latitude, agent.position.longitude)

main()
