import inspect, code

code.interact(local = inspect.currentframe().f_back.f_locals)