import time
from pysolace import SolClient


sess = SolClient()
sess.connect("218.32.76.102:80", "sinopac", "shioaji", "shioaji111")
sess.subscribe("L/>")
time.sleep(5)