# Standard Libraries
from abc import ABC
from typing import Callable, Optional

# Third Party Packages
from django.core.management.base import BaseCommand as DjangoCommand


class BaseCommand(DjangoCommand, ABC):
    """BaseCommand that can be inherited and customized."""

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout=stdout, stderr=stderr, no_color=no_color, force_color=force_color)

    def _print_s(
        self,
        txt,
        ending=None,
    ):
        """
        Print given `txt` in SUCCESS style to `self.stdout` (generally green).
        """
        self._print(txt=txt, style=self.style.SUCCESS, ending=ending)

    def _print_w(
        self,
        txt,
        ending=None,
    ):
        """
        Print given `txt` in WARNING style to `self.stdout` (generally yellow).
        """
        self._print(txt=txt, style=self.style.WARNING, ending=ending)

    def _print_e(self, txt, ending=None):
        """
        Print given `txt` in ERROR style to `self.stdout` (generally red).
        """
        self._print(txt=txt, style=self.style.ERROR, ending=ending)

    def _print_n(self, txt, ending=None):
        """
        Print given `txt` in NOTICE style to `self.stdout` (generally red, but lighter).
        """
        self._print(txt=txt, style=self.style.NOTICE, ending=ending)

    def _print(self, txt, style: Optional[Callable] = None, ending=None):
        if style is not None:
            self.stdout.write(style(txt), ending=ending)
        else:
            self.stdout.write(txt, ending=ending)
