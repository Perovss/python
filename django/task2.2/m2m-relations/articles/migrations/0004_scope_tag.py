# Generated by Django 4.1 on 2022-09-24 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_scope_article_scope_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag', verbose_name='Раздел'),
            preserve_default=False,
        ),
    ]