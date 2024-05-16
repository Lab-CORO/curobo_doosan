# Matériel utilisé

Nvidia propose un tutoriel afin de pouvoir implémenter un nouveau robot dans le framework CuRobo. Pour ce faire, un ordinateur équipé d'un processeur **Intel vPRO i9 13900**, et d'une carte graphique **Nvidia RTX 2000 ADA Generation** est utilisé, tout ceci sous l’OS **Ubuntu 22.04**. Plusieurs modules sont nécessaires au bon fonctionnement de ce framework, le choix de leurs versions est crucial. Voici les versions utilisées pour l'implémentation du robot Doosan M1013:

- **Isaac Sim 2022.2.1**
- **Pytorch 11.8**
- **CUDA 11.7**

## Obtention du fichier URDF

Afin d’utiliser le robot M1013 dans Isaac Sim, CuRobo propose un convertisseur URDF vers USD, le format de fichier propriétaire de Nvidia. Le fichier URDF est généré à partir des fichiers `.xacro` présent sur le GitHub de Doosan. Ce fichier, qui est une description complète du robot, doit être soigneusement vérifié, en prêtant attention aux chemins vers les différents fichiers afin d’éviter des erreurs.

## Génération du fichier USD

Pour générer le fichier `.USD`, deux options sont disponibles :

1. Utiliser le script `urdf_to_usd_converter.py` du dossier CuRobo
2. Utiliser le convertisseur intégré dans Isaac Sim.

Notre conversion est réalisée avec la seconde méthode car la première nous procure un fichier `.USD` non fonctionnel.

## Création du fichier YML

La création du fichier `.yml` du robot est ensuite nécessaire. Les fichiers YAML en robotique et sur Isaac Sim servent à configurer de manière lisible et flexible les propriétés des robots et les paramètres des simulations. Un modèle vierge peut être téléchargé sur le site de CuRobo et complété selon les instructions données. Les chemins vers les fichiers requis, le lien à la base et à l'effecteur, ainsi que les noms des joints doivent être spécifiés, en prêtant attention à leur orthographe. Les valeurs de `null_space_weight` et `cspace_distance_weight` sont initialisées avec un vecteur unitaire de taille correspondant au nombre de joints du robot.

## Génération des sphères de collisions

CuRobo utilise des sphères afin de déterminer les collisions du robot. Elles sont utilisées pour simplifier les calculs de collision, accélérer les simulations et prévenir les interférences entre les parties du robot et son environnement. Ces sphères sont générées grâce au module Lula Robot Description présent dans Isaac Sim. Cette étape est cruciale pour éviter des comportements non voulus du robot. Le dictionnaire est créé en prenant compte des propriétés du robot, ce dictionnaire donne la liste des collisions à ignorer. Cela permet d'éviter l’apparition d’erreurs de collisions inutiles. Un buffer pour les collisions `collision_sphere_buffer` est initialisé avec des valeurs nulles, modifiables selon les besoins. Un buffer pour les collisions augmente la marge de sécurité dans les simulations en créant un espace supplémentaire qui prévient les contacts accidentels entre les objets.

## Tests dans Isaac Sim

Une fois ces fichiers obtenus, des exemples de validation proposés par CuRobo peuvent être effectués pour vérifier le bon fonctionnement de l’environnement, notamment avec les tests de `motion_gen_reacher`, `ik_reachability` et `mpc_example`.
