try:
    import cythonbench
except ImportError:
    import pyximport
    pyximport.install()
    import cythonbench

class TestSuite:
    def time_loop(self):
        cythonbench.loop()
    def time_fibonacci(self):
        cythonbench.fibonacci()
    def time_primes(self):
        cythonbench.primes(20)

