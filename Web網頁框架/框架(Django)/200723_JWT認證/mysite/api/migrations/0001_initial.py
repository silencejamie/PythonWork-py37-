# Generated by Django 2.0 on 2020-07-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='創建時間')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
                ('username', models.EmailField(max_length=255, unique=True, verbose_name='用戶名')),
                ('fullname', models.CharField(max_length=64, null=True, verbose_name='中文名')),
                ('phonenumber', models.CharField(max_length=16, null=True, unique=True, verbose_name='電話')),
                ('is_active', models.BooleanField(default=True, verbose_name='激活狀態')),
            ],
            options={
                'permissions': (('select_user', '查看用戶'), ('change_user', '修改用戶'), ('delete_user', '刪除用戶')),
                'default_permissions': (),
            },
        ),
    ]
