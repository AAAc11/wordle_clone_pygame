import pygame
import random
from gamestate.playstate import PlayState
from gamestate.summarystate import SummaryState
import settings


class AIPlayerState(PlayState):
    def __init__(self, game):
        super().__init__(game)
        self.is_ai = True

        #użycie słownika
        self.all_words = [w.upper() for w in self.list_of_words]
        self.possible_words = self.all_words.copy()
        self.used_words = set()

        #zmienna dla ai
        self.greens = {}
        self.yellows = {}
        self.grays = set()

        #sterowanie
        self.current_guess = ""
        self.next_action_time = pygame.time.get_ticks()
        self.delay = 450

        self.last_guess_letters = set()

    def handle_events(self, events):
        now = pygame.time.get_ticks()
        if now >= self.next_action_time:
            self.next_action_time = now + self.delay
            return self.ai_step()
        return self

    def ai_step(self):
        #wybór nowego słowa
        if not self.current_guess:
            self._filter_possible_words()

            self.current_guess = self._choose_next_word()

            self.used_words.add(self.current_guess)
            self.users_word = []

        #wpisywanie liter
        if len(self.users_word) < 5:
            if self.click_sound:
                self.click_sound.play()
            letter = self.current_guess[len(self.users_word)]
            self.board.change_letter(letter)
            self.users_word.append(letter)
            return None

        #enter
        if len(self.users_word) == 5:
            #sprawdzenie kafelków
            self.board.check_tiles(self.users_word, self.word_to_guess)
            self.last_guess_letters = set(self.users_word)

            #pobranie kolorów z planszy
            results = self.board.get_last_row_results()

            #aktualizacja klawiatury
            current_tiles = self.board.rows[self.board.current_row].tiles
            self.keyboard.change_color(current_tiles)

            #analizowanie
            self._analyze_results(results)

            attempt = "".join(self.users_word)
            win = attempt == self.word_to_guess
            lose = self.board.current_row == 5

            if win or lose:
                summary = SummaryState(self.game)
                summary.is_ai = True
                summary.word_to_guess = self.word_to_guess
                summary.used_rows = self.board.current_row + 1
                summary.won = win
                return summary

            #przejście do następnego rzędu
            self.board.next_row()
            self.users_word = []
            self.current_guess = ""

        return None

    def _analyze_results(self, results):
        #analizowanie kolorów
        for r in results:
            i = r["index"]
            letter = r["letter"]
            color = r["color"]

            #zielony
            if color == settings.GREEN:
                self.greens[i] = letter

            #żółty
            elif color == settings.YELLOW:
                if letter not in self.yellows:
                    self.yellows[letter] = set()
                self.yellows[letter].add(i)

            #szary
            else:
                if letter not in self.greens.values() and letter not in self.yellows:
                    self.grays.add(letter)

    def _filter_possible_words(self):
        #filtrowanie słów
        filtered = []

        green_positions = set(self.greens.keys())

        for word in self.all_words:
            #zakaz powtarzania słów
            if word in self.used_words:
                continue

            valid = True

            #zielone-litera musi być na tym samym miejscu
            for i, letter in self.greens.items():
                if word[i] != letter:
                    valid = False
                    break
            if not valid:
                continue

            #szare
            for letter in self.grays:
                if letter in word:
                    valid = False
                    break
            if not valid:
                continue

            #żółte-litera musi się pojawić
            for letter, banned_positions in self.yellows.items():
                if letter not in word:
                    valid = False
                    break

                found_valid_position = False

                for i in range(5):
                    #na innym miejscu niż poprzednio
                    if i in banned_positions:
                        continue

                    #na innym miejscu niż zielone
                    if i in green_positions and self.greens[i] != letter:
                        continue

                    if word[i] == letter:
                        found_valid_position = True
                        break

                if not found_valid_position:
                    valid = False
                    break

            if valid:
                filtered.append(word)

        self.possible_words = filtered

    def _choose_next_word(self):
        def pick_from(words):
            words = [w for w in words if w not in self.used_words]
            return random.choice(words) if words else None

        #zastosowanie normalnego filtru
        self._filter_possible_words()
        choice = pick_from(self.possible_words)
        if choice:
            return choice

        candidates = [
            w for w in self.all_words
            if w not in self.used_words and self._word_fits_constraints(w)
        ]
        choice = pick_from(candidates)
        if choice:
            return choice

        #tylko zielone + żółte (bez szarych)
        candidates = []
        for w in self.all_words:
            if w in self.used_words:
                continue

            ok = True
            for i, l in self.greens.items():
                if w[i] != l:
                    ok = False
                    break
            for l in self.yellows:
                if l not in w:
                    ok = False
                    break

            if ok:
                candidates.append(w)

        choice = pick_from(candidates)
        if choice:
            return choice

        #cokolwiek innego
        candidates = [w for w in self.all_words if w not in self.used_words]
        return random.choice(candidates)

    def _word_fits_constraints(self, word):
        #zielone
        for i, l in self.greens.items():
            if word[i] != l:
                return False

        #szare
        for l in self.grays:
            if l in word:
                return False

        #żółte
        for l, banned in self.yellows.items():
            if l not in word:
                return False

            allowed = False
            for i in range(5):
                if i in banned:
                    continue
                if i in self.greens and self.greens[i] != l:
                    continue
                if word[i] == l:
                    allowed = True
                    break

            if not allowed:
                return False

        return True