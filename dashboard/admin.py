from django.contrib import admin
from .models import FavLyrics, Lyrics, SearchHistory, Song, SongLyrics, User

admin.site.register(FavLyrics)
admin.site.register(Lyrics)
admin.site.register(SearchHistory)
admin.site.register(Song)
admin.site.register(SongLyrics)
