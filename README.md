# Song Lyric Finder

## Overview

The Song Lyric Finder is a software system designed to provide users with a convenient tool for retrieving and displaying song lyrics. Users can input a song title, and the system will fetch and present the corresponding lyrics. The system also allows users to create accounts and bookmark their favorite lyrics, enhancing the user experience for music enthusiasts.

## Tech Stack

The chosen tech stack for the Song Lyric Finder includes:

- **Python3:** Primary programming language
- **PostgreSQL:** Database management system
- **pgAdmin:** Database administration tool
- **psycopg2:** PostgreSQL database connectivity library
- **LyricsGenius:** API for fetching song lyrics
- **Django:** Web framework for backend development
- **GitHub:** Version control and source code repository

## Tech Stack Details

- **Python3:** Provides a robust and versatile foundation for backend development.
- **PostgreSQL:** Ensures a reliable and scalable database solution.
- **pgAdmin:** User-friendly tool for managing the PostgreSQL database.
- **Django:** Simplifies web application development with ORM and built-in admin interface.
- **GitHub:** Primary platform for version control and source code repository.
- **`psycopg2`:** Facilitates seamless communication between Django and PostgreSQL.

## Intended Infrastructure

The Song Lyric Finder is intended to be hosted on a local machine, deployed and operated on a server or computer within a specific, controlled environment. This infrastructure choice contributes to the efficiency of the development process, minimizes potential issues, and ensures reliability when deployed in a production environment. The entire project, including the source code, will be hosted on a GitHub repository for centralized code management.

## Outside Data Sources

Data sources for the Song Lyric Finder include manual input for song titles and lyrics, as well as data scraping from the Genius website using the LyricsGenius API. Users can manually input song details through the application interface, and the LyricsGenius API will fetch lyric information based on the user-provided song details. Users also have the option to favorite lyrics by bookmarking them, with these bookmarks stored in the database.

The user interaction process involves logging into the system, using a search bar to discover new song lyrics, and inputting keywords or themes of interest. The system processes this input, generates an API call to the LyricsGenius API for relevant lyric searches, and integrates the API response, including song titles, lyrics, artist information, and metadata, into the database.
