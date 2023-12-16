
# Prédiction du succès d'une nouvellle chanson sur la plateforme Spotify

## Contexte
La popularité des morceaux joue un rôle crucial dans l'expérience utilisateur, impactant ainsi la durée d'écoute et potentiellement les abonnements. Les publicités constituent une part significative des revenus de l'entreprise. Pour garantir une expérience agréable, Spotify cherche à obtenir les droits de diffusion des morceaux les plus engageants pour ses utilisateurs. C'est pourquoi l'entreprise cherche à prédire le succès des morceaux sur sa plateforme afin d'optimiser la sélection des contenus diffusés.

# Analyse CRISP-DM
## Compréhension du problème
### Evaluation de la situation
**Expérience Utilisateur** : Recommandations de chansons plus personnalisées pour accroître la satisfaction et réduire le désabonnement.

**Contenu Musical** : Promotion d'artistes émergents et adaptation des licences en fonction des prédictions de succès des chansons.

**Stratégie Marketing** : Ciblage des campagnes publicitaires sur les chansons attractives et utilisation de données prédictives pour des campagnes plus efficaces.

**Analyse des Tendances** : Suivi des tendances musicales pour anticiper les évolutions du marché et informer les décisions stratégiques.

**Modèle de Revenus** : Amélioration de l'expérience utilisateur pour augmenter les revenus issus des abonnements, maximisation des revenus publicitaires en augmentant le temps d'écoute.

**Collaboration avec les Artistes** : Partage d'informations pertinentes avec les artistes et labels pour établir des partenariats stratégiques basés sur les données de succès.

**Innovation Technologique** : Utilisation de technologies avancées (analyse de données, apprentissage automatique) pour améliorer les algorithmes de prédiction et explorer de nouvelles fonctionnalités pour la plateforme.

### Evaluation de la situation
**Évaluation des Ressources** :

Données Disponibles : Données complètes sur les écoutes et interactions des utilisateurs, mais des lacunes possibles concernant les données démographiques et les feedbacks qualitatifs.
Technologie et Outils : Infrastructure solide nécessitant une mise à niveau pour gérer le volume croissant des données. Des investissements supplémentaires en outils analytiques avancés pourraient être nécessaires.
Expertise et Compétences : Expertise solide en data science mais expérience limitée dans l'industrie musicale. Besoin potentiel de formations supplémentaires ou de recrutement spécifique.

**Identification des Exigences** :

Exigences Techniques : Mise à jour de l'infrastructure et renforcement de la sécurité des données.
Exigences Légales et Éthiques : Conformité aux réglementations de confidentialité et respect des valeurs éthiques de l'entreprise.

**Analyse des Risques** :

Risques Liés aux Données : Risques liés à la qualité et à la confidentialité des données des utilisateurs.
Risques Technologiques : Défis d'intégration de nouvelles technologies et complexité des modèles prédictifs.
Risques de Projet : Risques de dépassement des délais et du budget, ainsi que d'alignement avec les objectifs commerciaux.

**Considérations et Contraintes** :

Budget et Financement : Budget limité pouvant restreindre la portée du projet. Nécessité de définir un retour sur investissement clair.
Délais : Contraintes temporelles nécessitant une gestion efficace du temps et des ressources.
Contraintes Opérationnelles : Capacité limitée de l'équipe et besoin de s'assurer que le projet n'interfère pas avec les opérations courantes.

### Détermination des objectifs du Data mining
**Modélisation Prédictive** :
Développer un modèle capable de prédire la popularité ou le succès d'une nouvelle chanson sur Spotify, basé sur des critères tels que le nombre d'écoutes, les interactions des utilisateurs, et l'inclusion dans les playlists populaires...

Examiner les tendances historiques et actuelles dans les données d'écoute pour identifier les patterns de succès des chansons.
Analyser comment ces tendances varient en fonction des genres musicaux, des régions géographiques, et des groupes démographiques.

### Production d’un plan de projet
- Phase 1 : Compréhension du Problème d'Affaires.
- Phase 2 : Compréhension des Données 
- Phase 3 : Préparation des Données
- Phase 4 : Modélisation 
- Phase 5 : Évaluation
- Phase 6 : Déploiement
- Suivi et Maintenance

## Compréhension des données
### Collecte des données initiales
Les données ont été collectées de sources différentes 
- SOUNDCLOUD Music Data
- Kaggle
- Gihub
### Description des données
-Donnée obtenue de kaggle

A. Structure des Données
La base de données comprend 195 entrées, chacune représentant une chanson, et 14 attributs décrivant divers aspects musicaux. Les caractéristiques comprennent des éléments tels que la danseabilité, l'énergie, la tonalité, le volume sonore, la présence de paroles, la probabilité d'acoustique ou d'instrumental, la vivacité, la positivité, la vitesse, la durée, la signature temporelle, et un attribut binaire indiquant si l'utilisateur a aimé la chanson.

B. Types de Données
Les types de données incluent des valeurs numériques (float64 et int64) pour la plupart des attributs, ainsi qu'un attribut binaire (liked) indiquant la préférence de l'utilisateur.

-Donnée obtenue de Github

A. Structure des Données
L'ensemble de données Spotify (intitulé data.csv) comprend plus de 160 000 pistes de 1921 à 2020 trouvées dans Spotify en juin 2020. 
Chaque ligne de l'ensemble de données correspond à une piste, avec des variables telles que le titre, l'artiste et l'année situées dans leurs colonnes respectives. Outre les variables fondamentales, des éléments musicaux de chaque morceau, tels que le tempo, la dansabilité et la tonalité, ont également été extraits.

B. Types de Données
L'ensemble de données est divisé en 169909 lignes et 19 colonnes. Ces 19 colonnes de données sont divisées en 15 colonnes numériques et 4 colonnes catégorielles.

### Exploration des données
-Donnée obtenue de kaggle

A. Valeurs Uniques
La diversité des valeurs uniques dans chaque attribut reflète la variété des caractéristiques musicales dans la base de données. Par exemple, la danseabilité et l'énergie ont respectivement 169 et 168 valeurs uniques, démontrant la richesse de ces caractéristiques.

B. Statistiques Descriptives
Les statistiques descriptives fournissent un aperçu des tendances centrales et de la dispersion des données. Par exemple, la danseabilité moyenne est de 0.64, suggérant que la plupart des chansons ont une facilité de danse raisonnable.

- Données de Github
Forte popularité au fil des années.



### Vérifiction de la qualité des données
-Donnée obtenue de kaggle

Aucune valeur manquante n'a été identifiée dans la base de données après le processus de remplacement, garantissant l'intégrité des données pour l'analyse ultérieure.
