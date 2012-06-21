import unittest

from flask import Flask
from hip_pocket import Mapper


class MapperAppTests(unittest.TestCase):
    def setUp(self):
        self.app = Flask("mapper")
        self.app.debug = True
        self.app.testing = True
        self.mapper = Mapper(self.app)

    def test_endpoint_setup(self):
        self.assertEqual(self.mapper.endpoint_base_name, "mapper")

    def test_mapping_creates_route(self):
        self.mapper.add_url_rule("/", "mapper_index")
        routes = list(self.app.url_map.iter_rules())
        # Flask adds the static route for us automatically
        self.assertEqual(len(routes), 2)

    def test_import_prefixed(self):
        self.mapper.add_url_rule("/", "mapper_index")
        routes = list(self.app.url_map.iter_rules())
        our_route = [route for route in routes if route.rule == "/"][0]
        self.assertEqual(our_route.endpoint, "mapper.mapper_index")

    def test_import_resolves(self):
        self.mapper.add_url_rule("/", "mapper_index")
        with self.app.test_client() as tc:
            rv = tc.get("/")
            self.assertTrue("Mapper Index Page" in rv.data)

    def test_overriding_endpoint(self):
        self.mapper.add_url_rule("/", "overridden_endpoint", endpoint="endpoint_name")
        with self.app.test_client() as tc:
            rv = tc.get("/")
            self.assertTrue("The url for url_for('endpoint_name') is /" in rv.data)

    def test_url_kwarg_forwarding(self):
        self.mapper.add_url_rule("/", "post_only", methods=["POST"])
        with self.app.test_client() as tc:
            self.assertTrue("405" in tc.get("/").status)
            self.assertTrue("Only accessible via POST" in tc.post("/").data)


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(MapperAppTests)
    return suite
