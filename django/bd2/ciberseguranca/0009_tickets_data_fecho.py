from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciberseguranca', '0008_registos_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='data_fecho',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
