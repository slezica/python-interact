import inspect, code

frame   = inspect.currentframe().f_back
module  = frame.f_globals['__file__']

banner  = 'Interacting at %s:%d' % (module, frame.f_lineno)
context = dict(frame.f_globals.items() + frame.f_locals.items())

code.interact(banner = banner, local = context)