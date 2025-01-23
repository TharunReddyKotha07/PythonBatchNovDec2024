def hello(name="world!"):
    """
    >>> hello()
    Hello world!

    >>> hello()
    Hello ...

    >>> hello('Michel')
    Hello Michel
    """
    print(f"Hello {name}")


if __name__ == "__main__":
    import doctest

    # doctest.testmod()
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    # doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)


## Assignment : research to know how to pass elipsis operator in commandline
# python -m doctest -o ELLIPSIS c_example.py 
# The -o flag in the doctest command-line interface allows you to pass additional options.
# ELLIPSIS tells doctest to enable ... for partial output matching.