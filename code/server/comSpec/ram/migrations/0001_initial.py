# Generated by Django 2.0.4 on 2018-05-26 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mem_brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mem_form_factor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mem_tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Memory_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('fr', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Frequency | GHz')),
                ('moduel_name', models.CharField(max_length=50, verbose_name='Moduel Name')),
                ('data_rate', models.PositiveIntegerField()),
                ('capacity', models.PositiveSmallIntegerField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('mem_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ram.Mem_brand', verbose_name='Memory Brand')),
                ('mem_form_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ram.Mem_form_factor', verbose_name='Memory Form Factor')),
                ('mem_tech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ram.Mem_tech', verbose_name='Memory Technology')),
            ],
        ),
        migrations.CreateModel(
            name='Memory_market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=2000)),
                ('prize', models.DecimalField(decimal_places=2, max_digits=7)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Market_info')),
                ('memory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ram.Memory_info')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='ram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ram.Memory_info'),
        ),
    ]