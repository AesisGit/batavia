from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class ListTests(TranspileTestCase):
    pass


class BuiltinListFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["list"]
