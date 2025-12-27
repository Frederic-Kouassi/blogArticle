# Page de Contact - Documentation de Refactoring

## 1. Composants à Extraire

### Utiliser les Composants Partagés

- En-tête de `includes/header.html`
- Pied de page de `includes/footer.html`
- CSS de `static/css/main.css`
- JavaScript de `static/js/main.js`

### Mettre à Jour le Modèle

- Faire en sorte que contact.html étende base.html
- Supprimer le code dupliqué en-tête/pied de page
- Supprimer le CSS et JavaScript inline

---

## 2. Éléments Dynamiques à Implémenter

### 2.1 Informations de Contact (Lignes 437-507)

**Actuel :** Cartes de contact statiques avec emails et adresses codés en dur

**Rendre dynamique :**

- Email demande générale
- Email éditorial/soumissions
- Email partenariats
- Email support technique
- Adresse du bureau
- Numéro de téléphone

**Besoins base de données :**

- Modèle ContactInfo avec tous les champs de contact
- Enregistrement unique éditable depuis l'admin

### 2.2 Formulaire de Contact (Lignes 496-557)

**Actuel :** Formulaire statique avec alerte JavaScript

**Rendre dynamique :**

- La soumission du formulaire sauvegarde en base de données
- Notification email envoyée à l'administrateur
- Messages de succès/erreur affichés
- Fonctionnalité de case à cocher inscription newsletter
- Validation du formulaire (côté serveur)
- Protection CSRF

**Besoins base de données :**

- Modèle ContactMessage (nom, email, sujet, message, inscription_newsletter, adresse_ip, cree_le, est_lu, repondu_le)
- Choix de sujet (général, soumission, partenariat, technique, feedback, autre)

**Besoins formulaire :**

- Django ModelForm pour ContactMessage
- Validation des champs
- Widgets personnalisés avec classes Tailwind

### 2.3 Section FAQ (Lignes 560-608)

**Actuel :** 4 éléments FAQ codés en dur avec accordéon

**Rendre dynamique :**

- Texte de la question
- Texte de la réponse
- Ordre d'affichage
- Statut actif/inactif

**Besoins base de données :**

- Modèle FAQ (question, réponse, ordre, est_actif)
- Enregistrements multiples ordonnés par champ ordre

---

## 3. Exigences Backend

### Modèles à Créer

1. **ContactInfo** - Tous les détails de contact
2. **ContactMessage** - Soumissions de formulaire
3. **FAQ** - Questions fréquemment posées

### Formulaire à Créer

- **ContactForm** - ModelForm pour soumissions de contact avec validation

### Vue à Créer

- **contact()** - Gérer GET (afficher formulaire) et POST (traiter soumission)
- Envoyer notification email à la soumission
- Gérer inscription newsletter si case cochée

### Fonctionnalité Email

- Créer modèle email pour notifications admin
- Configurer paramètres email (SMTP)
- Envoyer notification quand formulaire soumis

### URL à Ajouter

- `/contact/` - Page de contact

### Interface Admin

- Enregistrer tous les modèles
- Admin ContactMessage : vue liste avec filtres (sujet, lu, date)
- Marquer messages comme lus
- Voir détails soumission
- Admin FAQ : ordonnancement inline

---

## 4. Configuration Email

### Paramètres à Ajouter

- EMAIL_BACKEND
- EMAIL_HOST (ex: smtp.gmail.com)
- EMAIL_PORT (587)
- EMAIL_USE_TLS
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- DEFAULT_FROM_EMAIL
- ADMIN_EMAIL

### Modèle Email

- Créer `templates/email/contact_notification.html`
- Inclure infos expéditeur, sujet, message
- Formatage professionnel

---

## 5. Étapes d'Implémentation

1. Mettre à jour contact.html pour étendre base.html
2. Utiliser les includes d'en-tête et pied de page
3. Créer tous les modèles requis
4. Créer ContactForm
5. Exécuter les migrations
6. Créer vue contact (GET et POST)
7. Implémenter fonction notification email
8. Créer modèle d'email
9. Configurer paramètres email
10. Mettre à jour les URLs
11. Enregistrer modèles dans admin
12. Mettre à jour template pour utiliser données dynamiques et formulaire
13. Ajouter framework messages Django pour feedback
14. Tester soumission formulaire et email
15. Tester fonctionnalité accordéon FAQ

---

## 6. Flux de Gestion Formulaire

1. Utilisateur remplit formulaire contact
2. Formulaire soumis via POST
3. Serveur valide données
4. Si valide :
   - Sauvegarder ContactMessage en base
   - Si case newsletter : ajouter/mettre à jour enregistrement Newsletter
   - Envoyer notification email à l'admin
   - Afficher message succès
   - Rediriger vers page contact
5. Si invalide :
   - Afficher messages erreur
   - Ré-afficher formulaire avec données utilisateur

---

## 7. Considérations de Sécurité

- Jeton CSRF dans formulaire
- Validation email
- Limitation de débit (éviter spam)
- Aseptiser entrées utilisateur
- Stocker adresse IP pour suivi
- Champ Honeypot (anti-spam optionnel)
