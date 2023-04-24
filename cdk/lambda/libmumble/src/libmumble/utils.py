# -*- coding: utf-8 -*-

"""Provides miscellaneous utilities.
"""

from datetime import datetime, timezone


def to_urlsafe_base64(b64: str) -> str:
    """Converts a standard Base64-encoded string into a URL-safe string.

    Replaces '+' with '-', and '/' with '_'.
    Removes trailing '='.
    """
    return b64.rstrip('=').replace('+', '-').replace('/', '_')


def format_yyyymmdd_hhmmss_ssssss(time: datetime) -> str:
    """Formats a given datetime into "yyyy-mm-ddTHH:MM:ss.SSSSSSZ" form.

    The timzone is adjusted into UTC.

    :raises ValueError: if ``time`` is naive.
    """
    if time.tzinfo is None:
        raise ValueError('datetime must be timezone-aware')
    offset = time.tzinfo.utcoffset(time)
    if offset is None:
        raise ValueError('datetime must be timezone-aware')
    if offset != 0:
        time = time.astimezone(timezone.utc)
    return time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


def current_yyyymmdd_hhmmss_ssssss() -> str:
    """Returns the current timestamp in the form: "yyyy-mm-ddTHH:MM:ss.SSSSSSZ".
    """
    return format_yyyymmdd_hhmmss_ssssss(datetime.now(tz=timezone.utc))