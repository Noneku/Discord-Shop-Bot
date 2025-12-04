Discord Shop Bot est une application développée en Python permettant d’intégrer une véritable vitrine de produits directement dans un serveur Discord.  
Le bot interagit avec une API externe pour récupérer un catalogue de vêtements et les présenter sous forme d’embeds structurés, lisibles et attractifs.  

Ce projet a pour objectif d'offrir une expérience de consultation simple et rapide pour les utilisateurs, tout en proposant une architecture propre, modulaire et évolutive.  
Grâce à cette organisation, le bot pourra facilement intégrer de nouvelles fonctionnalités comme des filtres avancés, des notifications automatiques, une wishlist personnalisée ou encore la connexion à une API e-commerce personnalisée.

Le bot a été pensé pour être maintenable, professionnel et déployable dans un contexte réel, tout en constituant un excellent support d’apprentissage autour de Discord.py, de la gestion d’API et de la structuration d’un projet backend moderne.



## 🔄 Git Workflow

Pour garantir un développement propre et organisé, ce projet suit un Git Workflow simple :

### 🔹 Branches principales
- **main** : contient le code stable, prêt pour la production ou le déploiement.
- **dev** : branche de développement utilisée pour intégrer et tester les nouvelles fonctionnalités.

### 🔹 Branches de fonctionnalité
Chaque nouvelle fonctionnalité doit être développée dans une branche dédiée :

    feature/nom-de-la-feature

Exemples :  
- `feature/shop-command`  
- `feature/api-connection`  
- `feature/auto-update`  

### 🔹 Cycle de développement
1. Créer une branche feature  

    git checkout -b feature/ma-feature

2. Développer et faire des commits réguliers  
3. Merger la branche dans `dev`

    git checkout dev
    git merge feature/ma-feature

4. Tester et valider  
5. Merger `dev` dans `main` lorsque tout est stable  
    git checkout main
    git merge dev

### ✍️ Convention de commits
Les messages suivent un format simple :

- `feat:` → nouvelle fonctionnalité  
- `fix:` → correction de bug  
- `docs:` → documentation  
- `refactor:` → amélioration interne du code  
- `chore:` → maintenance ou configuration  

Exemples :  
feat: add /shop command
fix: correct API URL error
docs: update README