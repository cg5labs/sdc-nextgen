#!/usr/bin/env python3

# create hostname random_host following pattern: xsrvNNN-NNN

import random

def random_digits():
  digits = random.randrange(0,999)

  # prefix '0' or '00' for all digits < 100
  if (digits < 100 and digits > 10):
      sdigits = "0" + str(digits)
  elif (digits < 100 and digits < 10):
      sdigits = "00" + str(digits)
  else:
      sdigits = str(digits)

  return sdigits

def main():
  digits1 = random_digits()
  digits2 = random_digits()

  print("random_host: xsrv%s-%s" % (digits1,digits2))

if __name__ == "__main__":
    main()

