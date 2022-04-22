# Generated by Django 4.0.4 on 2022-04-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_visitor_rename_user_id_solution_vis_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='vis_id',
        ),
        migrations.AddField(
            model_name='visitor',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='visitor',
            name='vis_problem_attempted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='vis_problem_solved',
            field=models.IntegerField(default=0),
        ),
    ]
