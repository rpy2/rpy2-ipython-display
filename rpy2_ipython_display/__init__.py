from .gif import gif
from .htmlwidget import htmlwidget


def auto(out, args):
    """Idea: have an auto display which will choose gif/htmlwidget or any future display function automatically

    based on inspection of the out object; it highlights that we could implement displays as classes, draft:

    class GifDisplay(Display):

        def __init__(self, default_args):
            # this would likely go to parent Display
            self.default_args = default_args

        def __call__(self, out, args):
            pass

        def is_supported(self, obj) -> bool:
            'Check if the R obj can be displayed with GifDisplay'
            pass
    to be implemented as classes
    """
    ...
