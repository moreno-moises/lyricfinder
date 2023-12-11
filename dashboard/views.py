from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse  
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .models import Song, Lyrics, SearchHistory, SongLyrics, FavLyrics
import lyricsgenius
from datetime import datetime
from django.contrib.auth import get_user_model
from .backends import CustomUserBackend


User = get_user_model()


@login_required
def profile(request):
    fav_lyrics = request.user.fav_lyrics.all()
    return render(request, 'profile.html', {'fav_lyrics': fav_lyrics})


@login_required
def search_song(request):
    query = None

    if request.method == 'POST':
        query = request.POST.get('song_title')

        try:
            song_title, artist = map(str.strip, query.split(' by ', 1))
        except ValueError:
            messages.error(request, "Invalid query format. Please enter the query as '<song title> by <artist>'.")
            return render(request, 'search.html')

        genius = lyricsgenius.Genius("M8pSOVuFCPTDx1OQBfHIhOX9BB2MKoZqqaJZeMnoB-lolHevNQDK0juBdJeKcbG6")
        song = genius.search_song(title=song_title, artist=artist)

        if song:
            print(f"Search successful: {song.title} by {song.artist}")
        else:
            print("No results found for the song.")

        existing_song = Song.objects.filter(TITLE=song.title, ARTIST=song.artist).first()
        print(f"Existing Song: {existing_song}")

        if not existing_song:
            new_song = create_song_from_genius(song)
            print(f"New song created: {new_song.TITLE} by {new_song.ARTIST}, ID: {new_song.SONG_ID}")
        else:
            new_song = existing_song
            print(f"Existing song found: {new_song.TITLE} by {new_song.ARTIST}, ID: {new_song.SONG_ID}")

        new_song_id = new_song.SONG_ID if new_song else None
        print(f"New Song ID: {new_song_id}")

        if song.lyrics:
            new_lyrics = Lyrics.objects.filter(lyrics=song.lyrics).first()

            if not new_lyrics:
                new_lyrics = Lyrics(lyrics=song.lyrics)
                new_lyrics.save()

            song_lyrics = SongLyrics.objects.filter(song_id=new_song_id, lyrics_id=new_lyrics.lyrics_id).first()

            if not song_lyrics:
                song_lyrics = SongLyrics(song_id=new_song_id, lyrics_id=new_lyrics.lyrics_id)
                song_lyrics.save()

            return render(
                request,
                'search_results.html',
                {'song': new_song, 'lyrics': new_lyrics, 'song_id': new_song_id}
            )

    messages.error(request, f"No results found for the song: {query}" if query else "Please submit a valid form.")
    return render(request, 'search.html')

@login_required
def search_results(request, song_id):
    try:
        song = get_object_or_404(Song, SONG_ID=song_id)
        lyrics = Lyrics.objects.get(songlyrics__song_id=song_id)
    except Song.DoesNotExist:
        messages.error(request, "No valid song ID available for bookmarking.")
        return redirect('home')

    return render(request, 'search_results.html', {'song': song, 'lyrics': lyrics, 'song_id': song_id})


def create_song_from_genius(song):
    title = song.title
    artist = song.artist

    # Check if the song already exists
    existing_song = Song.objects.filter(TITLE=title, ARTIST=artist).first()

    if not existing_song:
        new_song = Song(TITLE=title, ARTIST=artist)
        new_song.save()  # Save the new song to get the SONG_ID
        print(f"New song created: {new_song.TITLE} by {new_song.ARTIST}, ID: {new_song.SONG_ID}")
    else:
        new_song = existing_song
        print(f"Existing song found: {new_song.TITLE} by {new_song.ARTIST}, ID: {new_song.SONG_ID}")

    return new_song

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Login the user or redirect as needed
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def select_song(request, song_id):
    selected_song = get_object_or_404(Song, id=song_id)
    lyrics = Lyrics.objects.get(songlyrics__song_id=song_id)


    return render(request, 'select_song.html', {'song': selected_song, 'lyrics': lyrics})


@login_required
def bookmark_song(request):
    if request.method == 'POST':
        song_id = request.POST.get('song_id')

        # Handle the case where song_id is 'None'
        if song_id is None or song_id == 'None':
            return render(request, 'error.html', {'message': 'Invalid song ID'})

        try:
            song_id = int(song_id)
        except ValueError:
            # Handle the case where song_id is not a valid integer
            return render(request, 'error.html', {'message': 'Invalid song ID'})

        song = get_object_or_404(Song, SONG_ID=song_id)


    # Handle the case when the request method is not POST
    return render(request, 'error.html', {'message': 'Invalid request method'})

def custom_logout(request):
    from django.contrib.auth import logout
    logout(request)

    # Redirect the user to the home page
    return redirect('home')

class CustomLoginView(LoginView):
    authentication_backend = CustomUserBackend 

    def form_invalid(self, form):
        messages.error(self.request, 'User not found. Please check your username and password.')
        return super().form_invalid(form)