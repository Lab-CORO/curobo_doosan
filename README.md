# Instructions pour lancer le Docker x86

## Étape 1 : Construire le conteneur Docker
Pour construire le conteneur Docker avec la configuration x86, exécutez la commande suivante :
```bash
bash build_docker.sh x86
```

## Étape 2 : Démarrer le conteneur Docker
Pour démarrer le conteneur Docker avec la configuration x86, exécutez la commande suivante :
```bash
bash start_docker.sh x86
```

## Étape 3 : Recompiler le package OpenCV
Pour recompiler le package OpenCV, exécutez les commandes suivantes :
```bash
cd /pkgs/opencv/build
cmake ..
make
make install
```

## Étape 4 : Résolution du problème de symbole

Pour résoudre le problème de symbole manquant `ucm_set_global_opts`, veuillez exécuter le script ci-dessous à l'intérieur du conteneur Docker :

```bash
sudo apt-get update && sudo apt-get install --reinstall -y \
  libmpich-dev \
  hwloc-nox libmpich12 mpich
```




## Instructions pour lancer les scripts de curobo

Pour exécuter les scripts de curobo, utilisez la commande suivante :

```bash
python /chemin/vers/le/script
```

Remplacez `/chemin/vers/le/script` par le chemin réel du script que vous souhaitez exécuter.

## Utilisation de curobo pour générer une trajectoire avec incorporation de la caméra

Pour utiliser curobo et générer une trajectoire intégrant la caméra, veuillez suivre les étapes suivantes :

1. Assurez-vous d'avoir complété l'étape 4.
2. Accédez au répertoire `/home/ros2_ws`.
3. Exécutez la commande suivante :

```bash
ros2 run trajectory_publisher trajectory_publisher_node
```
