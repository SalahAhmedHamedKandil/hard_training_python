# decorator - spead test
from time import time
def spead_test(func):
  def wrapper():
    start=time()
    func()
    end= time()
    print(f'{end-start}')
  return wrapper

@spead_test
def gig_loop():
  for num in range(1,20000):
    print(f"{num}")


gig_loop()