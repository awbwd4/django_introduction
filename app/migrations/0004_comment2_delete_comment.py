# Generated by Django 4.0 on 2022-08-13 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_tag_comment_post_tag_set'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
