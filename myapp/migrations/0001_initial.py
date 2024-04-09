# Generated by Django 5.0.2 on 2024-04-02 09:02

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='folders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='groups_folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.CharField(default='none', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(blank=True, max_length=10, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='file_uplode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.FileField(upload_to='image/')),
                ('file_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.folders')),
            ],
        ),
        migrations.AddField(
            model_name='folders',
            name='folder_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.groups_folder'),
        ),
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Phone_Number', models.IntegerField(blank=True, null=True)),
                ('Gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=30, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Aadhar_Number', models.IntegerField(blank=True, null=True)),
                ('Father_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Mother_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Father_Occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('Mother_Occupation', models.CharField(blank=True, max_length=30, null=True)),
                ('Father_Phone_Number', models.IntegerField(blank=True, null=True)),
                ('mother_Phone_Number', models.IntegerField(blank=True, null=True)),
                ('Annual_Income', models.IntegerField(blank=True, null=True)),
                ('Religion', models.CharField(blank=True, max_length=50, null=True)),
                ('Caste', models.CharField(blank=True, max_length=50, null=True)),
                ('Community', models.CharField(blank=True, max_length=50, null=True)),
                ('Mother_Language', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
