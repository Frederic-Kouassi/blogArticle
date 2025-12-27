# Tableau de Bord Utilisateur - Documentation de Refactoring

## Aperçu

Refactoriser le tableau de bord utilisateur pour utiliser des Vues Basées sur des Classes (CBV), des inclusions de templates, et des données dynamiques depuis la base de données.

---

## 1. Composants à Extraire

### Utiliser les Composants Partagés

- En-tête de `includes/header.html` (si applicable pour le tableau de bord)
- Créer `includes/dashboard_sidebar.html` pour la navigation latérale
- Créer `includes/dashboard_header.html` pour la barre d'en-tête supérieure
- CSS vers `static/css/dashboard.css`
- JavaScript vers `static/js/dashboard.js`

### Structure du Modèle (Template)

- Créer `templates/dashboard/base_dashboard.html` - Modèle de base pour toutes les pages du tableau de bord
- Mettre à jour `user_dashboard.html` pour étendre base_dashboard
- Extraire la barre latérale (lignes 167-232) vers un include
- Extraire l'en-tête supérieur (lignes 236-308) vers un include

---

## 2. Sections du Tableau de Bord (Onglets)

### 2.1 Vue d'Ensemble (Lignes 313-453)

**Actuel :** Statistiques statiques et activité récente

**Rendre dynamique :**

- Nombre total de blogs (des articles de l'utilisateur)
- Nombre total de vues (somme de toutes les vues des articles)
- Nombre de commentaires (total des commentaires sur les articles)
- Nombre d'abonnés
- Flux d'activité récent (dernières actions)
- Boutons d'action rapide

### 2.2 Mes Blogs (Lignes 456-647)

**Actuel :** Tableau statique avec 4 blogs codés en dur

**Rendre dynamique :**

- Lister tous les articles de blog de l'utilisateur
- Afficher titre, catégorie, statut, vues, date
- Pagination (4 articles par page)
- Actions : Modifier, Voir, Supprimer
- Filtrer par statut (tous, publié, brouillon, en attente)
- Fonctionnalité de recherche

### 2.3 Créer un Blog (Lignes 650-788)

**Actuel :** Formulaire statique avec éditeur de texte riche

**Rendre dynamique :**

- Soumission du formulaire pour créer un nouveau blog
- Téléchargement d'image pour l'image mise en avant
- Éditeur de texte riche pour le contenu
- Menu déroulant de catégorie depuis la base de données
- Entrée des tags
- Sélection du statut (brouillon, en attente, publié)
- Validation du formulaire

### 2.4 Profil (Lignes 791-800+)

**Rendre dynamique :**

- Informations de profil utilisateur
- Téléchargement d'avatar
- Édition de la bio
- Liens réseaux sociaux
- Préférences email

### 2.5 Analytique

**Créer nouvelle section :**

- Vues au fil du temps (graphique)
- Articles les plus populaires
- Sources de trafic
- Métriques d'engagement

### 2.6 Paramètres

**Créer nouvelle section :**

- Paramètres du compte
- Préférences de notification
- Paramètres de confidentialité
- Changement de mot de passe

---

## 3. Exigences Backend - Vues Basées sur des Classes (CBV)

### Vues à Créer

**Utiliser les CBV génériques de Django :**

1. **DashboardView** (TemplateView)

   - Afficher les statistiques de vue d'ensemble
   - Activité récente

2. **BlogListView** (ListView)

   - Lister les blogs de l'utilisateur avec pagination
   - Filtrer et rechercher

3. **BlogCreateView** (CreateView)

   - Créer un nouvel article de blog
   - Gérer la soumission du formulaire et le téléchargement d'image

4. **BlogUpdateView** (UpdateView)

   - Modifier un article existant

5. **BlogDeleteView** (DeleteView)

   - Supprimer un article avec confirmation

6. **ProfileView** (UpdateView)

   - Voir et mettre à jour le profil utilisateur

7. **AnalyticsView** (TemplateView)

   - Afficher les données analytiques

8. **SettingsView** (UpdateView)
   - Gérer les paramètres utilisateur

### Mixins à Utiliser

- **LoginRequiredMixin** - Exiger l'authentification pour toutes les vues
- **UserPassesTestMixin** - Assurer que l'utilisateur ne peut modifier que ses propres articles

---

## 4. Modèles Nécessaires

### Extension Profil Utilisateur

- Bio, avatar, liens sociaux, préférences

### Article de Blog (BlogPost)

- Existe déjà (de la page d'accueil)
- Assurer la clé étrangère utilisateur

### Activité Utilisateur

- Suivre les actions utilisateur (créer, modifier, publier, supprimer)
- Horodatage et type d'action

### Paramètres Utilisateur

- Préférences de notification
- Paramètres de confidentialité

---

## 5. Structure des URLs

```
/dashboard/ - Vue d'ensemble
/dashboard/blogs/ - Liste de mes blogs
/dashboard/blogs/create/ - Créer nouveau blog
/dashboard/blogs/<id>/edit/ - Modifier blog
/dashboard/blogs/<id>/delete/ - Supprimer blog
/dashboard/profile/ - Profil utilisateur
/dashboard/analytics/ - Analytique
/dashboard/settings/ - Paramètres
```

---

## 6. Formulaires à Créer

1. **BlogForm** - Créer/modifier articles
2. **ProfileForm** - Mettre à jour profil utilisateur
3. **SettingsForm** - Mettre à jour paramètres utilisateur

---

## 7. Fonctionnalité JavaScript

### Navigation par Onglets

- Basculer entre les sections du tableau de bord
- Mettre à jour l'URL sans rechargement de page
- Sauvegarder l'onglet actif dans localStorage

### Éditeur de Texte Riche

- Implémenter la fonctionnalité de barre d'outils
- Formater le texte (gras, italique, titres, listes)
- Insérer liens et images
- Sauvegarde automatique des brouillons

### Téléchargement d'Image

- Fonctionnalité glisser-déposer
- Prévisualisation avant téléchargement
- Valider taille et type de fichier

### Notifications

- Bascule menu déroulant
- Marquer comme lu
- Mises à jour temps réel (optionnel - WebSocket)

### Actions Blog

- Modifier, voir, supprimer avec confirmation
- AJAX pour action supprimer

---

## 8. Étapes d'Implémentation

1. Créer le template base_dashboard.html
2. Extraire la barre latérale vers un include
3. Extraire l'en-tête vers un include
4. Créer toutes les CBV (Dashboard, BlogList, BlogCreate, etc.)
5. Créer les formulaires (BlogForm, ProfileForm, SettingsForm)
6. Mettre à jour les modèles (UserProfile, UserActivity, UserSettings)
7. Exécuter les migrations
8. Créer les motifs d'URL
9. Extraire le CSS vers dashboard.css
10. Extraire le JavaScript vers dashboard.js
11. Implémenter la fonctionnalité AJAX
12. Ajouter la validation de formulaire
13. Tester toutes les fonctionnalités du tableau de bord
14. Ajouter les vérifications de permissions

---

## 9. Considérations de Sécurité

- LoginRequiredMixin sur toutes les vues
- Protection CSRF sur tous les formulaires
- Valider que l'utilisateur possède le blog avant modification/suppression
- Aseptiser l'entrée de l'éditeur de texte riche
- Valider les téléchargements d'images (type, taille)
- Limitation de débit sur les soumissions de formulaire

---

## 10. Fonctionnalités à Ajouter

- Sauvegarde auto des brouillons (toutes les 30 secondes)
- Prévisualisation avant publication
- Dupliquer un article
- Actions en masse (supprimer plusieurs articles)
- Exporter les données du blog
- Planifier les articles pour publication future
- Paramètres SEO par article
- Calcul du temps de lecture
