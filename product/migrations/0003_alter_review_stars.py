from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], null=True),
        ),
    ]