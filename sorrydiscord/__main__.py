"""Entry point for `python -m sorrydiscord`."""

import sys

if "--timer-mode" in sys.argv:
    from .timer import run_timer
    run_timer()
else:
    from .main import main
    main()
