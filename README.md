# Library Orders : gestion de bibliothèque pour Odoo

Module **Odoo** de gestion de bibliothèque : catalogue de livres, auteurs, catégories, adhérents, employés et **suivi des prêts** (émission, retard, retour) avec facture PDF, envoi d'e-mail et partage WhatsApp.

## Fonctionnalités

- **Livres** : titre, ISBN, éditeur, année, nombre de pages, langue, note, prix, image, priorité, nombre d'exemplaires et disponibilité (mise à jour automatique)
- **Auteurs** et **catégories** avec contrainte d'unicité du nom et duplication d'un auteur
- **Adhérents** : coordonnées, date d'adhésion, référence automatique, compteur de prêts en cours
- **Employés** : poste, date d'embauche (la date ne peut pas être dans le futur)
- **Prêts (`library.invoice`)** :
  - référence générée automatiquement par séquence
  - date de retour calculée à partir de la date d'émission et de la durée (et inversement)
  - workflow **Brouillon → Confirmé → En retard → Terminé**, avec contrôle de la date avant de passer en retard
  - décrémentation automatique du nombre d'exemplaires à la création du prêt
  - suppression autorisée uniquement en brouillon
- **Facture PDF** (rapport QWeb) imprimable depuis le prêt
- **E-mail** au membre via un modèle de message, et **partage WhatsApp** du rappel de retour
- **Suivi et historique** des modifications (chatter et activités Odoo) sur tous les modèles
- **Trois groupes d'accès** : *Library Admin*, *Library Employee*, *Library Member*, avec des menus visibles selon le rôle

## Modèles de données

| Modèle | Description |
|---|---|
| `library.books` | Livres et stock d'exemplaires |
| `library.authors` | Auteurs (lien one2many vers les livres) |
| `library.categories` | Catégories de livres |
| `library.member` | Adhérents de la bibliothèque |
| `library.employees` | Employés de la bibliothèque |
| `library.invoice` | Prêts / factures (adhérent, livre, dates, statut, employé) |

## Droits d'accès

| Menu | Admin | Employé | Membre |
|---|:---:|:---:|:---:|
| Member | oui | oui | non |
| Books | oui | oui | oui |
| Invoice | oui | oui | oui |
| Employees, Authors, Categories | oui | non | non |

## Structure du module

```
library_orders/
├── __manifest__.py
├── models/        # authors, books, categories, employees, member, invoice
├── views/         # vues et menus de chaque modèle
├── security/      # groupes et droits d'accès (ir.model.access.csv)
├── data/          # séquences (membres, prêts) et modèle d'e-mail
├── report/        # rapport PDF de la facture (QWeb)
├── controllers/
└── static/description/icon.png
```

## Installation

**Prérequis** : Odoo 15 ou supérieur (à adapter selon votre version) et les modules `base`, `mail`, `calendar`, `web`.

1. Cloner le dépôt dans le dossier des add-ons Odoo, sous le nom `library_orders` :
   ```bash
   git clone https://github.com/Hasnae112/library-orders-odoo.git library_orders
   ```
2. Vérifier que ce dossier figure dans `addons_path` du fichier `odoo.conf`.
3. Redémarrer Odoo et mettre à jour la liste des applications (mode développeur : **Apps → Update Apps List**).
4. Rechercher **Library Management** et cliquer sur **Install**.
5. Attribuer à chaque utilisateur un groupe *Library* dans **Settings → Users**.

## Utilisation

1. Créer des **catégories**, des **auteurs**, puis des **livres** (avec le nombre d'exemplaires).
2. Enregistrer les **adhérents** et les **employés**.
3. Créer un **prêt** : choisir l'adhérent, le livre, la durée et l'employé, puis le confirmer.
4. Suivre le statut (En retard, Terminé), imprimer la **facture PDF**, envoyer un **e-mail** ou un message **WhatsApp**.

## Pistes d'amélioration

- Restaurer automatiquement le stock d'exemplaires quand un prêt passe à *Terminé*
- Droits d'accès par groupe et règles d'enregistrement (un membre ne voit que ses propres prêts)
- Pénalités de retard et rappels automatiques par tâche planifiée
- Tests unitaires et traduction en français

## Auteure

**Hasnae Elballaoui**, élève-ingénieure en Intelligence Artificielle et Transformation Digitale (ENSAH)
[LinkedIn](https://linkedin.com/in/hasnae-elballaoui-312209256) · [GitHub](https://github.com/Hasnae112)
