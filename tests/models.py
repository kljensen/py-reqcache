import testify
import requests
from reqcache.models import ReqCache


class ReqCacheTestCase(testify.TestCase):

    @testify.setup
    def create_cache(self):
        self.rcache = ReqCache("test", "memory")

    @testify.teardown
    def clear_cache(self):
        self.rcache = None

    def test_basic_caching(self):

        r = requests.get('http://github.com', hooks=self.rcache.hooks)
        self.assertFalse(getattr(r, "from_cache", False))

        r = requests.get('http://github.com', hooks=self.rcache.hooks)
        self.assertTrue(getattr(r, "from_cache", False))
