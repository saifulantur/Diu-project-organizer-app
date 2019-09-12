# Generated by Django 2.0 on 2019-09-11 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='adminprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='admin/img')),
                ('details', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100, unique=True)),
                ('department_nickname', models.CharField(max_length=20, unique=True)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship_no', models.CharField(max_length=50, unique=True)),
                ('internship_title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('internship_report', models.FileField(upload_to='internship/report')),
                ('student_id_1', models.CharField(max_length=50)),
                ('student_id_2', models.CharField(default=True, max_length=50)),
                ('student_id_3', models.CharField(default=True, max_length=50)),
                ('student_id_4', models.CharField(default=True, max_length=50)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('department', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='faculty', chained_model_field='facultyName', on_delete=django.db.models.deletion.CASCADE, to='projectapp.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.faculty')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.adminprofile')),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_no', models.CharField(max_length=50, unique=True)),
                ('project_title', models.CharField(max_length=100)),
                ('project_details', models.TextField()),
                ('project_file', models.FileField(upload_to='project/file')),
                ('project_report', models.FileField(upload_to='project/report')),
                ('student_id_1', models.CharField(max_length=50)),
                ('student_id_2', models.CharField(default=True, max_length=50)),
                ('student_id_3', models.CharField(default=True, max_length=50)),
                ('student_id_4', models.CharField(default=True, max_length=50)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('department', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='faculty', chained_model_field='facultyName', on_delete=django.db.models.deletion.CASCADE, to='projectapp.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.faculty')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.adminprofile')),
            ],
        ),
        migrations.CreateModel(
            name='projectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_project', models.CharField(max_length=50)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.department')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.adminprofile')),
            ],
        ),
        migrations.CreateModel(
            name='questionAndAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, unique=True)),
                ('answer', models.CharField(max_length=300)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.adminprofile')),
            ],
        ),
        migrations.CreateModel(
            name='supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('initial', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='supervisor/img')),
                ('details', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('department', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='faculty', chained_model_field='facultyName', on_delete=django.db.models.deletion.CASCADE, to='projectapp.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.faculty')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.adminprofile')),
            ],
        ),
        migrations.CreateModel(
            name='thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thesis_no', models.CharField(max_length=50, unique=True)),
                ('thesis_title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('thesis_file', models.FileField(upload_to='thesis/file')),
                ('student_id_1', models.CharField(max_length=50)),
                ('student_id_2', models.CharField(default=True, max_length=50)),
                ('student_id_3', models.CharField(default=True, max_length=50)),
                ('student_id_4', models.CharField(default=True, max_length=50)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('department', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='faculty', chained_model_field='facultyName', on_delete=django.db.models.deletion.CASCADE, to='projectapp.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.faculty')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.adminprofile')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.supervisor')),
            ],
        ),
        migrations.CreateModel(
            name='thesisCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_thesis', models.CharField(max_length=50)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.department')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.adminprofile')),
            ],
        ),
        migrations.AddField(
            model_name='thesis',
            name='thesis_category',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='department', chained_model_field='department', on_delete=django.db.models.deletion.CASCADE, to='projectapp.thesisCategory'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_category',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='department', chained_model_field='department', on_delete=django.db.models.deletion.CASCADE, to='projectapp.projectCategory'),
        ),
        migrations.AddField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.supervisor'),
        ),
        migrations.AddField(
            model_name='internship',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.supervisor'),
        ),
        migrations.AddField(
            model_name='department',
            name='facultyName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.faculty'),
        ),
    ]
