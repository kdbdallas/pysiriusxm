from __future__ import unicode_literals

import threading


__version__ = '0.1.0'


# Global reentrant lock to be held whenever libspotify functions are called or
# libspotify owned data is worked on. This is the heart of pyspotify's thread
# safety.
_lock = threading.RLock()


# Reference to the spotify.Session instance. Used to enforce that one and only
# one session exists in each process.
_session_instance = None


def _setup_logging():
    """Setup logging to log to nowhere by default.

    For details, see:
    http://docs.python.org/3/howto/logging.html#library-config

    Internal function.
    """
    import logging

    logger = logging.getLogger('siriusxm')
    handler = logging.NullHandler()
    logger.addHandler(handler)


def serialized(f):
    """Decorator that serializes access to all decorated functions.

    The decorator acquires pysiriusxm's single global lock while calling any
    wrapped function. It is used to serialize access to:

    - All calls to functions on :attr:`siriusxm.lib`.

    - All code blocks working on pointers returned from functions on
      :attr:`siriusxm.lib`.

    - All code blocks working on other internal data structures in pysiriusxm.

    Together this is what makes pyspotify safe to use from multiple threads and
    enables convenient features like the :class:`~siriusxm.EventLoop`.

    Internal function.
    """
    import functools

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        with _lock:
            return f(*args, **kwargs)
    if not hasattr(wrapper, '__wrapped__'):
        # Workaround for Python < 3.2
        wrapper.__wrapped__ = f
    return wrapper


_setup_logging()

from siriusxm.audio import *  # noqa
from siriusxm.config import *  # noqa
from siriusxm.connection import *  # noqa
from siriusxm.error import *  # noqa
from siriusxm.eventloop import *  # noqa
from siriusxm.offline import *  # noqa
from siriusxm.session import *  # noqa
from siriusxm.track import *  # noqa
from siriusxm.version import *  # noqa