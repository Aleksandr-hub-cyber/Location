import os

from django.db import models


class Pass(models.Model):
    coordinates = models.TextField()
    elevation = models.FloatField()
    name = models.CharField(max_length=255)
    photos = models.TextField()
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=[
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], default='new')

    def __str__(self):
        return self.name





class PassManager(models.Manager):

    def create_pass(self, coordinates, elevation, name, photos, user_name, user_email, user_phone):
        pass = self.model(
            coordinates=coordinates,
            elevation=elevation,
            name=name,
            photos=photos,
            user_name=user_name,
            user_email=user_email,
            user_phone=user_phone,
            status='new'
        )
        pass.save()
        return pass



    def get_db_info(self):
        db_host = os.environ.get('FSTR_DB_HOST')
        db_port = os.environ.get('FSTR_DB_PORT')
        db_login = os.environ.get('FSTR_DB_LOGIN')
        db_pass = os.environ.get('FSTR_DB_PASS')

        print(f'Database host: {db_host}')
        print(f'Database port: {db_port}')
        print(f'Database login: {db_login}')
        print(f'Database password: {db_pass}')
