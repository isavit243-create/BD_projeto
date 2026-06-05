import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciberseguranca', '0009_tickets_data_fecho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='data_upload',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
