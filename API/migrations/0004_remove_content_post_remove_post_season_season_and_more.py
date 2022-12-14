# Generated by Django 4.0 on 2022-09-08 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_content_download_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='season',
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=216)),
                ('season', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.post')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='season',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='API.season'),
            preserve_default=False,
        ),
    ]
