def capture(f):
    return type(f)(
        code=f.__code__,
        argdefs=f.__defaults__,
        globals={
            k: f.__globals__[k] 
            for k in f.__globals__.keys() & f.__code__.co_names
        },
        closure=tuple(
            (lambda x: lambda: x)(c.cell_contents).__closure__[0]
            for c in f.__closure__ or ()
        )
    )
