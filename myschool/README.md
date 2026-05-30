# 🏫 School Management System — Backend

API REST pour la gestion d'un établissement scolaire, développée avec Django et Django REST Framework.

## 🛠️ Stack technique

- **Python** 3.x
- **Django** 6.x
- **Django REST Framework**
- **PostgreSQL**
- **JWT** (SimpleJWT)
- **Swagger / Redoc** pour la documentation API

## ⚙️ Installation

### 1. Cloner le projet
```bash
git clone https://github.com/AdamLonewolf/Django_Student_management_backend
cd school_management
```

### 2. Créer et activer l'environnement virtuel
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement
Crée un fichier `.env` à la racine du projet :
```env
SECRET_KEY ='django-insecure-*l&(5=-dt!2+^@w5g(#4s=cdaac6449kc#i1g@oatf_f)udas-'
DB_NAME='school_management_db'
DB_USER='postgres'
DB_PASSWORD='admin'
DB_HOST='localhost'
DB_PORT='5432'
```

### 5. Appliquer les migrations
```bash
python manage.py migrate
```

### 6. Créer un super utilisateur
```bash
python manage.py createsuperuser
```

### 7. Lancer le serveur
```bash
python manage.py runserver
```

Le serveur tourne sur **http://127.0.0.1:8000**

## Documentation API

| URL | Description |
|-----|-------------|
| http://127.0.0.1:8000/swagger/ | Documentation Swagger |
| http://127.0.0.1:8000/redoc/ | Documentation Redoc |
| http://127.0.0.1:8000/admin/ | Interface d'administration |

## Authentification

L'API utilise **JWT (JSON Web Token)**.

```http
POST /api/accounts/auth/login/
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "motdepasse"
}
```

La réponse contient un `access` token à inclure dans les headers :
```
Authorization: Bearer <access_token>
```

## Structure du projet

```
myschool/
├── accounts/        # Gestion utilisateurs (admin, prof, étudiant, parent)
├── academics/       # Cours, niveaux, filières, notes, absences, inscriptions
├── assignments/     # Devoirs et soumissions
├── base/           # Modèles de base
├── core/           # Configuration centrale
└── myschool/       # Settings et URLs principales
```

## Rôles utilisateurs

| Rôle | Description |
|------|-------------|
| `admin` | Accès total |
| `teacher` | Gestion de ses cours et étudiants |
| `student` | Accès à ses données personnelles |
| `parent` | Accès aux données de son enfant |