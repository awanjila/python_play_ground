

def get_algorithm_result(numb):
  largest = numb[0]
  for Li in numb:
    if largest < Li:
      largest = Li
    if Li == numb[-1]:
      return largest
    else:
      continue

def prime_number(primes):
  if primes > 1:
    for i in range(3, primes):
      if (primes % i) == 0:
        return False
      else:
        return True
  else:
    return False

