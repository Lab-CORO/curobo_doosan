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

## Recompiler le package OpenCV
Lors de l'utilisation de la camera, il se peut que vous rencontriez l'erreur `AttributeError: module 'cv2.dnn' has no attribute 'DictValue' `
Pour resoudre cela, vous pouvez commenter la ligne 171 du fichier suivant :
```bash
code /usr/local/lib/python3.10/dist-packages/cv2/typing/__init__.py
```

## Résolution du problème de symbole

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
ros2 run trajectory_publisher trajectory_pub_node
```

## Problème potentiel avec CUDA

Lors de l'utilisation de ce projet Docker, il est possible que vous rencontriez des problèmes avec CUDA, comme le message d'erreur `CUDA device not found`. Si cela se produit, il peut être nécessaire de redémarrer le serveur graphique GDM pour résoudre ce problème.

Pour redémarrer le serveur graphique GDM, exécutez la commande suivante :

```bash
sudo systemctl stop gdm
```
