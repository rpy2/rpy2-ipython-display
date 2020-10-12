from IPython.display import Image, display
from rpy2.robjects.packages import importr


gganimate = importr('gganimate')


def gif(animation, args):
    path = gganimate.animate(
        animation, renderer=gganimate.gifski_renderer(),
        width=args.width, height=args.height, res=args.res
    )
    with open(list(path)[0], 'rb') as f:
        display(Image(data=f.read(), format='gif'))
