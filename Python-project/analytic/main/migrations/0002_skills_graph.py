from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='graph',
            field=models.ImageField(default=None, upload_to='skills', verbose_name='График'),
        ),
    ]
