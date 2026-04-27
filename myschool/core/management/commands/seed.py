from django.core.management.base import BaseCommand
from faker import Faker
import uuid
from accounts.models.user import User
from accounts.models.student import Student
from accounts.models.teacher import Teacher
from accounts.models.parent import Parent
from academics.models.field import Field
from academics.models.level import Level

fake = Faker('fr_FR')


class Command(BaseCommand):
    help = 'Seed la base de données avec de fausses données'

    def handle(self, *args, **kwargs):
        self.seed_fields()
        self.seed_levels()
        self.seed_teachers()
        self.seed_students()
        self.seed_parents()
        self.stdout.write(self.style.SUCCESS('Seeding terminé !'))

    def seed_fields(self):
        if Field.objects.exists():
            self.stdout.write('Filières déjà seedé')
            return
        fields = [
            {'name': 'Cybersecurité', 'description': 'Securité des systèmes'},
            {'name': 'Developpement Web', 'description': 'Conception web'},
            {'name': 'Communication Digitale','description': 'Communication numérique'},
            {'name': 'Création Digitale', 'description': 'Design numérique'},
        ]
        for f in fields:
            Field.objects.create(**f)
        self.stdout.write('Filières crées')

    def seed_levels(self):
        if Level.objects.exists():
            self.stdout.write('Niveau déjà seedé')
            return
        levels = ['Licence 1', 'Licence 2', 'Licence 3', 'Master 1', 'Master 2']
        for field in Field.objects.all():
            for name in levels:
                Level.objects.create(name=name, field=field)
        self.stdout.write('Niveaux crées')

    def seed_teachers(self):
        if Teacher.objects.exists():
            self.stdout.write('Enseignant deja seedé')
            return
        specialities = [
            'Informatique', 'Mathematiques',
            'Reseaux', 'Design', 'Communication'
        ]
        for i in range(5):
            user = User.objects.create_user(
                email=fake.unique.email(),
                password='Teacher1234!',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                role='teacher',
            )
            Teacher.objects.create(
                user=user,
                speciality=specialities[i],
                phone_number=fake.numerify('0# ## ## ## ##'),
                gender=fake.random_element(['M', 'F']),
                address=fake.city(),
            )
        self.stdout.write('Enseignants crées')

    def seed_students(self):
        if Student.objects.exists():
            self.stdout.write('Etudiant déjà seedé')
            return
        levels = list(Level.objects.all())
        for _ in range(20):
            user = User.objects.create_user(
                email=fake.unique.email(),
                password='Student1234!',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                role='student',
            )
            Student.objects.create(
                user=user,
                level=fake.random_element(levels),
                birthdate=fake.date_of_birth(minimum_age=18, maximum_age=25),
                gender=fake.random_element(['M', 'F']),
                phone_number=fake.numerify('0# ## ## ## ##'),
                student_number=f"STU-{uuid.uuid4().hex[:8].upper()}",
                address=fake.city(),
            )
        self.stdout.write('Etudiants crées')

    def seed_parents(self):
        if Parent.objects.exists():
            self.stdout.write('Parent deja seedé')
            return
        students = list(Student.objects.all())
        for _ in range(10):
            user = User.objects.create_user(
                email=fake.unique.email(),
                password='Parent1234!',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                role='parent',
            )
            parent = Parent.objects.create(
                user=user,
                phone_number=fake.numerify('0# ## ## ## ##'),
                address=fake.city(),
                parent_type=fake.random_element(['father', 'mother', 'guardian']),
            )
            enfants = fake.random_elements(
                elements=students,
                length=fake.random_int(min=1, max=2),
                unique=True
            )
            parent.students.set(enfants)
        self.stdout.write('Parents crées')