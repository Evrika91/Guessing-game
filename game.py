import random

start_game = input('Chcesz zagrać w grę? Y/N \n')
while start_game == 'Y' or start_game == 'y':
    # Konfiguracja gry
    print('***Konfiguracja gry:***\n')
    print('Wprowadź początek i koniec zakresu - dwie liczby całkowite większe od zera')
    min_number = int(input('Wprowadź początek zakresu: \n'))
    if min_number == 0:
        print('Liczba powinna być większa od zera:)')
        min_number = int(input('Wprowadź początek zakresu: \n'))
    max_number = int(input('Wprowadź koniec zakresu: \n'))
    if max_number < min_number:
        print('Koniec zakresu musi być większy od początku \n')
        max_number = int(input('Wprowadź koniec zakresu: \n'))


    print('\n ***Rozgrywka***:\n')
    # Utworzenie liczby do odgadnięcia
    guess_number = random.randint(min_number, max_number)

    count = 1
    # Rozgrywka
    player_guess = int(input("Zgadnij liczbę : "))
    while player_guess != guess_number:
        if player_guess > max_number or player_guess < min_number:
            player_guess = int(input("Liczba nie jest z ustalonego zakresu! Spróbuj jeszcze raz : "))
        elif player_guess != guess_number:
            player_guess = int(input("Spróbuj jeszcze raz : "))
            count = count+1
    # Zakończenie gry
    else:
        print("Gratulacje! Wygrałeś po", count ," próbach!")
        ask = input('Chcesz zagrać jeszcze raz? Y/N \n')
        if ask == 'n' or ask =='N':
            print('See ya!')
            break
