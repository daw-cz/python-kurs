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

Aplikacja będzie dostępna w przeglądarce pod adresem:
`127.0.0.1:5000/books/`

## Jak używać aplikacji

* **Przeglądanie**: Główna strona wyświetla tabelę ze wszystkimi zapisanymi książkami.
* **Dodawanie**: Użyj formularza na dole strony głównej, wpisz dane książki i kliknij "Dodaj książkę".
* **Edycja**: Kliknij w tytuł dowolnej książki na liście, aby przejść do formularza edycji, zmień dane i kliknij "Zapisz zmiany".
