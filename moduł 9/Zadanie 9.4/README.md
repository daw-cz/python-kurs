# Domowa Biblioteka (Home Library)

Aplikacja webowa napisana w języku Python z użyciem frameworka Flask. 
Umożliwia zarządzanie domowym księgozbiorem: przeglądanie listy książek, 
dodawanie nowych pozycji oraz edycję istniejących wpisów.

## Wymagania
* Python 3.x
* Biblioteki z pliku `requirements.txt`

## Instalacja

1. Pobierz pliki do jednego folderu.
2. Otwórz terminal w tym folderze i zainstaluj wymagane biblioteki:
   ```bash
   pip install -r requirements.txt
   ```

## Uruchomienie aplikacji

W folderze z plikami projektu otwórz terminal i uruchom serwer za pomocą poniższej komendy:
```bash
flask run
```

Aplikacja będzie dostępna w przeglądarce pod adresami:
* **Strona HTML**: `localhost:5000/books/`
* **REST API**: `localhost:5000/api/v1/books/`

## Jak używać aplikacji (Interfejs HTML)

* **Przeglądanie**: Główna strona wyświetla tabelę ze wszystkimi zapisanymi książkami.
* **Dodawanie**: Użyj formularza na dole strony głównej, wpisz dane książki i kliknij "Dodaj książkę".
* **Edycja**: Kliknij w tytuł dowolnej książki na liście, aby przejść do formularza edycji, zmień dane i kliknij "Zapisz zmiany".

## Interfejs REST API (v1)

Aplikacja udostępnia interfejs API. Wszystkie żądania przyjmują oraz zwracają dane w formacie JSON. 

### Dostępne punkty końcowe:

* **`GET /api/v1/books/`** – Pobiera listę wszystkich książek w bazie.
* **`POST /api/v1/books/`** – Tworzy nowy wpis książki. 
  * *Wymagany format JSON:* `{"title": "Tytuł", "author": "Autor", "year": 2026, "is_read": false}`
* **`GET /api/v1/books/<id>`** – Pobiera szczegółowe dane jednej książki o konkretnym identyfikatorze numerycznym. Zwraca błąd 404, jeśli obiekt nie istnieje.
* **`PUT /api/v1/books/<id>`** – Aktualizuje dane istniejącej książki (umożliwia pełną lub częściową modyfikację pól). Zwraca błąd 404 w przypadku braku książki lub 400 przy błędnych typach danych.
* **`DELETE /api/v1/books/<id>`** – Usuwa wybraną książkę z bazy danych i zapisuje zmiany. Zwraca błąd 404, jeśli obiekt nie istnieje.
