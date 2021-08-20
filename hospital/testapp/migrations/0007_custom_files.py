# Generated by Django 3.2.6 on 2021-08-20 04:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import testapp.validation


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0006_alter_multi_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(upload_to='custom/images/', validators=[testapp.validation.validate_file_extension_image])),
                ('aadhar_pic', models.FileField(upload_to='custom/pdf/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('xl_file', models.FileField(upload_to='custom/xls/', validators=[testapp.validation.validate_file_extension_xls])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]