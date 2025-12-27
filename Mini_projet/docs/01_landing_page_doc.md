# Page d'accueil (home.html) - Documentation de Refactoring

## 1. Composants à extraire vers des fichiers inclus

### Composant En-tête (`templates/includes/header.html`)

- **Emplacement :** Lignes 112-165 dans le home.html actuel
- **Contient :** Logo, menu de navigation (bureau et mobile), liens d'authentification
- **Dynamique :** Statut d'authentification de l'utilisateur, mise en évidence de la page active
- **Contexte nécessaire :** `user`, `request.path`

### Composant Pied de page (`templates/includes/footer.html`)

- **Emplacement :** Lignes 633-698 dans le home.html actuel
- **Contient :** Logo, liens sociaux, navigation, catégories, formulaire de newsletter, droits d'auteur
- **Dynamique :** Liste des catégories depuis la base de données
- **Contexte nécessaire :** `categories`, `current_year`

### Styles CSS (`static/css/main.css`)

- **Emplacement :** Lignes 10-109 dans le home.html actuel
- **Extraire :** Variables CSS, typographie, styles des composants, requêtes responsives

### JavaScript (`static/js/main.js`)

- **Emplacement :** Lignes 700-796 dans le home.html actuel
- **Extraire :** Bascule du menu mobile, en-tête collant, défilement fluide, initialisation de l'en-tête

### JavaScript spécifique à la page (`static/js/home.js`)

- **Extraire :** Curseur (slider) mis en avant, bouton "charger plus", soumission du formulaire de newsletter

---

## 2. Éléments dynamiques à implémenter

### 2.1 Section Héros (Lignes 167-290)

**Rendre dynamique :**

- Titre et sous-titre du héros
- Boutons CTA basés sur le statut d'authentification
- Curseur des articles mis en avant (3 articles avec image, catégorie, date, titre, extrait, auteur)

**Besoins base de données :**

- Modèle HeroSection (titre, sous-titre, image_de_fond, est_actif)
- Modèle BlogPost avec champs est_mis_en_avant et ordre_mise_en_avant

### 2.2 Section Derniers Articles (Lignes 292-404)

**Rendre dynamique :**

- Titre et sous-titre de la section
- Cartes d'articles de blog (image, catégorie, date, titre, extrait, auteur, temps de lecture)
- Pagination avec bouton "Charger plus"

**Besoins base de données :**

- Modèle BlogPost (titre, slug, extrait, contenu, image_mise_en_avant, auteur, catégorie, tags, date_publication, temps_lecture, est_publie, nombre_vues)

### 2.3 Aperçu de l'Article Mis en Avant (Lignes 406-528)

**Rendre dynamique :**

- Image mise en avant, catégorie, titre, infos auteur, date, temps de lecture
- Aperçu du contenu de l'article, tags, partage social, bio de l'auteur

**Note :** Afficher un seul article mis en avant sélectionné depuis l'administration

### 2.4 Barre latérale - Newsletter (Lignes 533-542)

**Rendre dynamique :**

- La soumission du formulaire sauvegarde en base de données
- Validation de l'email et gestion des doublons
- Messages de succès/erreur

**Besoins base de données :**

- Modèle Newsletter (email, date_inscription, est_actif, adresse_ip)

### 2.5 Barre latérale - Catégories (Lignes 544-579)

**Rendre dynamique :**

- Nom de la catégorie, nombre d'articles, lien

**Besoins base de données :**

- Modèle Category (nom, slug, description, icône, couleur, est_actif)

### 2.6 Barre latérale - Articles Récents (Lignes 581-613)

**Rendre dynamique :**

- Miniature de l'article, titre, date, lien
- Récupérer les 3 derniers articles publiés

### 2.7 Barre latérale - Tags Populaires (Lignes 615-628)

**Rendre dynamique :**

- Nom du tag, lien, nombre d'articles

**Besoins base de données :**

- Modèle Tag (nom, slug, est_actif)

---

## 3. Exigences Backend

### Modèles à Créer

1. **Category** - Catégories du blog avec icône et couleur
2. **Tag** - Tags du blog
3. **BlogPost** - Contenu principal du blog avec toutes les métadonnées
4. **HeroSection** - Contenu héros de la page d'accueil
5. **Newsletter** - Inscriptions par email

### Vues à Créer

1. **home()** - Vue principale de la page d'accueil avec toutes les données de contexte
2. **subscribe_newsletter()** - Point de terminaison AJAX pour l'inscription à la newsletter
3. **load_more_posts()** - Point de terminaison AJAX pour la pagination

### URLs à Ajouter

- `/` - Page d'accueil
- `/subscribe/` - Inscription newsletter
- `/load-more/` - Charger plus d'articles

---

## 4. Fonctionnalité JavaScript

### Inscription Newsletter

- Gérer la soumission du formulaire via AJAX
- Afficher les messages de succès/erreur
- Vider le formulaire en cas de succès
- Gestion du jeton CSRF

### Charger Plus d'Articles

- Récupérer la page suivante d'articles via AJAX
- Ajouter les nouveaux articles à la grille
- Mettre à jour l'état du bouton (chargement, désactivé, caché)
- Mettre à jour l'affichage du nombre d'articles

### Curseur Mis en Avant (Slider)

- Fonctionnalité de défilement avec boutons précédent/suivant
- Comportement de défilement fluide

---

## 5. Structure des Fichiers après Refactoring

```
templates/
├── base.html (NOUVEAU - amélioré)
├── home.html (MIS À JOUR - étend base)
├── includes/ (NOUVEAU DOSSIER)
│   ├── header.html (NOUVEAU)
│   └── footer.html (NOUVEAU)

static/
├── css/
│   └── main.css (NOUVEAU)
└── js/
    ├── main.js (NOUVEAU)
    └── home.js (NOUVEAU)

blog/
├── models.py (MIS À JOUR)
├── views.py (MIS À JOUR)
├── urls.py (MIS À JOUR)
└── admin.py (MIS À JOUR)
```

---

## 6. Étapes d'Implémentation

1. Créer le dossier includes et extraire en-tête/pied de page
2. Créer le modèle base.html
3. Extraire le CSS vers un fichier statique
4. Extraire le JavaScript vers des fichiers statiques
5. Créer tous les modèles requis
6. Exécuter les migrations
7. Créer les vues avec les données de contexte
8. Mettre à jour les URLs
9. Enregistrer les modèles dans l'administration
10. Mettre à jour home.html pour utiliser les données dynamiques
11. Tester toutes les fonctionnalités
