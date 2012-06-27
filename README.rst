py-reqcache: Caching for Python's Request Package
=========================

py-reqcache is a Python_ package that provides caching for
the Requests_ HTTP library.  It's based on the wonderful
Requests-Cache_ libary by Roman Haritonov and uses the
backends from that project.  The main difference is that
this package uses the Requests_ API hooks instead of
monkeypatching.


Example usage
----------

    import requests
    import reqcache

    c = reqcache.ReqCache("foo", "memory")

    r = requests.get('http://github.com', hooks=c.hooks)
    print getattr(r, "from_cache", False)

    r = requests.get('http://github.com', hooks=c.hooks)
    print getattr(r, "from_cache", False)


Contribute
----------

#. Fork the project on github to start making your changes
#. Send pull requests with your bug fixes or features
#. Submit and create issues on github


References
----------
.. _Python: http://www.python.org/
.. _Requests: http://www.python-requests.org
.. _Requests-Cache: https://github.com/reclosedev/requests-cache
