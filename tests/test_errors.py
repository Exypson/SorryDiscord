"""Tests for errors.py – exception hierarchy."""

import pytest
from sorrydiscord.errors import (
    SorryDiscordError,
    NetworkError,
    SteamNotFoundError,
    DatabaseLoadError,
)


def test_network_error_is_sorrydiscord_error():
    assert issubclass(NetworkError, SorryDiscordError)


def test_steam_not_found_is_sorrydiscord_error():
    assert issubclass(SteamNotFoundError, SorryDiscordError)


def test_database_load_error_is_sorrydiscord_error():
    assert issubclass(DatabaseLoadError, SorryDiscordError)


def test_can_catch_all_with_base():
    with pytest.raises(SorryDiscordError):
        raise NetworkError("test")
