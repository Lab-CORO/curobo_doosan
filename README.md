# Instructions pour l'utilisation des scripts Docker

## Étape 1 : Construire le conteneur Docker
Pour construire le conteneur Docker avec la configuration Noetic, exécutez la commande suivante :
```bash
bash build_docker.sh noetic
```
## Étape 2 : Démarrer le conteneur Docker
Pour démarrer le conteneur Docker avec la configuration Noetic, exécutez la commande suivante :
```bash
bash start_docker.sh noetic
```
# Instructions pour lancer le contrôle du robot

Pour lancer le contrôle du robot en vitesse de joint, exécutez le script suivant :

```bash
bash /home/catkin_ws/script/launch_robot.sh
```
# Instructions pour lancer le MQTT

Pour démarrer le service MQTT, exécutez la commande suivante :

```bash
sudo service mosquitto start
```

Ensuite, lancez le client MQTT avec la commande :

```bash
roslaunch mqtt_client standalone.launch params_file:=config/config.yml
```

Par défaut, le service est configuré pour utiliser `localhost` sur le port `1883`.
