from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class Song(models.Model):
    SONG_ID = models.AutoField(primary_key=True)
    TITLE = models.TextField(db_column='TITLE', blank=True, null=True)
    GENRE = models.TextField(db_column='GENRE', blank=True, null=True)
    ARTIST = models.TextField(db_column='ARTIST', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SONG'

class FavLyrics(models.Model):
    FAV_ID = models.AutoField(primary_key=True)
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fav_lyrics', db_column='USER_ID')
    song = models.ForeignKey('dashboard.Song', on_delete=models.CASCADE, db_column='SONG_ID')

    class Meta:
        managed = False
        db_table = 'FAV_LYRICS'


class Lyrics(models.Model):
    lyrics_id = models.IntegerField(db_column='LYRICS_ID', primary_key=True)  # Field name made lowercase.
    lyrics = models.TextField(db_column='LYRICS', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'LYRICS'


class SearchHistory(models.Model):
    search_id = models.IntegerField(db_column='SEARCH_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)
    keywords = models.TextField(db_column='KEYWORDS', blank=True, null=True)
    timestamp = models.DateField(db_column='TIMESTAMP', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'SEARCH_HISTORY'




class SongLyrics(models.Model):
    song_id = models.IntegerField(db_column='SONG_ID', blank=True, null=True)
    lyrics_id = models.IntegerField(db_column='LYRICS_ID', blank=True, null=True)
    song_lyrics_id = models.IntegerField(db_column='SONG_LYRICS_ID', primary_key=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'SONG_LYRICS'




class User(models.Model):
    USER_ID = models.IntegerField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    FIRST_NAME = models.TextField(db_column='FIRST_NAME', blank=True, null=True)
    LAST_NAME = models.TextField(db_column='LAST_NAME', blank=True, null=True)
    PASSWORD = models.TextField(db_column='PASSWORD', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'USER'




class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)


    class Meta:
        managed = False
        db_table = 'auth_group'




class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)




class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)


    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)




class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()


    class Meta:
        managed = False
        db_table = 'auth_user'




class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)




class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)




class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'django_admin_log'




class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)




class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()


    class Meta:
        managed = False
        db_table = 'django_migrations'
