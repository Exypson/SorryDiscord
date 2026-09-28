"""
Custom exceptions for Sorry Discord.

Keep it small — one base class + a few specific ones.
"""


class SorryDiscordError(Exception):
    """Base error for all Sorry Discord errors."""


class NetworkError(SorryDiscordError):
    """An API / HTTP call failed."""


class SteamNotFoundError(SorryDiscordError):
    """Steam installation could not be located."""


class DatabaseLoadError(SorryDiscordError):
    """Failed to load the games database from any source."""
