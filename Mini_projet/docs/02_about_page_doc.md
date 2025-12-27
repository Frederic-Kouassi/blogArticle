# Page À Propos - Documentation de Refactoring

## 1. Composants à Extraire

### Utiliser les Composants Partagés

- En-tête de `includes/header.html`
- Pied de page de `includes/footer.html`
- CSS de `static/css/main.css`
- JavaScript de `static/js/main.js`

### Mettre à Jour le Modèle

- Faire en sorte que about.html étende base.html
- Supprimer le code dupliqué en-tête/pied de page
- Supprimer le CSS et JavaScript inline

---

## 2. Éléments Dynamiques à Implémenter

### 2.1 Section Statistiques (Lignes 171-198)

**Actuel :** Chiffres statiques (10,000+ lecteurs, 250+ articles, 150+ pays)

**Rendre dynamique :**

- Nombre de lecteurs mensuels
- Nombre d'articles publiés
- Nombre de pays atteints

**Besoins base de données :**

- Modèle AboutPageStats avec ces trois champs entiers
- Enregistrement unique mis à jour depuis l'administration

### 2.2 Mission & Vision (Lignes 202-214)

**Actuel :** Blocs de texte statiques

**Rendre dynamique :**

- Titre et texte de la Mission
- Titre et texte de la Vision

**Besoins base de données :**

- Modèle AboutPageContent avec champs mission et vision
- Éditable depuis le panneau d'administration

### 2.3 Valeurs Fondamentales (Lignes 216-244)

**Actuel :** 3 valeurs codées en dur

**Rendre dynamique :**

- Icône de la valeur (classe FontAwesome)
- Titre de la valeur
- Description de la valeur
- Ordre d'affichage

**Besoins base de données :**

- Modèle CoreValue avec icône, titre, description, ordre, est_actif
- Enregistrements multiples, ordonnés par le champ ordre

### 2.4 Chronologie/Parcours (Lignes 246-308)

**Actuel :** 4 éléments de chronologie codés en dur

**Rendre dynamique :**

- Année/période
- Titre
- Description
- Ordre d'affichage

**Besoins base de données :**

- Modèle TimelineItem avec année, titre, description, ordre, est_actif
- Enregistrements multiples montrant l'histoire de l'entreprise

### 2.5 Membres de l'Équipe (Lignes 310-422)

**Actuel :** 4 cartes d'équipe codées en dur

**Rendre dynamique :**

- Photo de profil (avec téléchargement d'image)
- Nom
- Poste/titre
- Bio
- Liens réseaux sociaux (Twitter, LinkedIn, Email)
- Ordre d'affichage

**Besoins base de données :**

- Modèle TeamMember avec tous les champs de profil
- Téléchargement d'image pour les photos
- URLs de réseaux sociaux optionnelles

---

## 3. Exigences Backend

### Modèles à Créer

1. **AboutPageStats** - Chiffres statistiques
2. **AboutPageContent** - Texte mission/vision
3. **CoreValue** - Valeurs de l'entreprise
4. **TimelineItem** - Histoire de l'entreprise
5. **TeamMember** - Profils de l'équipe

### Vue à Créer

- **about()** - Récupérer toutes les données de la page à propos et rendre le modèle

### URL à Ajouter

- `/about/` - Page à propos

### Interface Admin

- Enregistrer tous les modèles
- Rendre les stats et le contenu éditables (enregistrement unique)
- Permettre l'ajout/édition/ordre des valeurs, chronologie, membres d'équipe

---

## 4. Étapes d'Implémentation

1. Mettre à jour about.html pour étendre base.html
2. Utiliser les includes d'en-tête et de pied de page
3. Créer tous les modèles requis
4. Exécuter les migrations
5. Créer la vue about avec le contexte
6. Mettre à jour les URLs
7. Enregistrer les modèles dans l'administration
8. Mettre à jour le modèle (template) pour utiliser les données dynamiques
9. Ajouter des données exemple via l'admin
10. Tester le design responsif
