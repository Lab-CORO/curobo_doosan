#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import json

# Configuration MQTT
broker_address = "localhost"
topic = "Velocity"

# Données à publier au format JSON
message_data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]


# Convertir les données en format JSON
message_json = json.dumps(message_data)

# Initialiser le client MQTT
client = mqtt.Client("Publisher")
client.connect(broker_address)

# Publier le message JSON sur le topic MQTT
client.publish(topic, message_json)

# Déconnexion du client MQTT
client.disconnect()

# Afficher un message confirmant l'envoi du message
print(f"Published JSON message to {topic}: {message_json}")
