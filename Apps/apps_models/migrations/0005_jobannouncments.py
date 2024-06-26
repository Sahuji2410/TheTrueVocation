# Generated by Django 5.0.4 on 2024-06-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_models', '0004_jobdescription_experience_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobAnnouncments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announment_title', models.CharField(blank=True, default='No Announcements!', max_length=150, null=True)),
                ('description', models.TextField(blank=True, default=True, max_length=500)),
                ('youtube_link', models.URLField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
