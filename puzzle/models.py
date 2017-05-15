import random
from typing import Tuple

from django.contrib.gis.db.models import MultiPointField
from django.db import models
from django.urls import reverse

from maps.models import Game, GameTranslation


class Puzzle(Game):
    default_positions = MultiPointField(geography=True)

    class Meta:
        verbose_name = 'Puzzle'
        verbose_name_plural = 'Puzzles'

    def __init__(self, *args, **kwargs):
        self.__default_positions = []
        super(Puzzle, self).__init__(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse('puzzle_map', args=(self.slug,))

    def load_translation(self, lang):
        result, _ = PuzzleTranslation.objects.get_or_create(language_code=lang, master=self)
        return result

    def pop_position(self) -> Tuple:
        if len(self.__default_positions) == 0:
            self.__default_positions = self.default_positions[:]
            random.shuffle(self.__default_positions)
        return self.__default_positions.pop().coords


class PuzzleTranslation(GameTranslation):
    master = models.ForeignKey(Puzzle, related_name='translations', editable=False)

    class Meta:
        unique_together = ('language_code', 'master')
        db_table = 'puzzle_puzzle_translation'
