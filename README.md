# rp2350

![GitHub Release](https://img.shields.io/github/v/release/kreier/rp2350)
![GitHub License](https://img.shields.io/github/license/kreier/rp2350)

Example programs in CircuitPython and C for the Raspberry Pico 2350.

## Benchmark prime

``` py
import math
import time

last = 1000
found = 4
start = time.monotonic()
print('Prime numbers to {}'.format(last))

for number in range(11, last, 2):
    prime = 1
    if number % 3 == 0:
            prime = 0
    elif number % 5 == 0:
            prime = 0
    elif number % 7 == 0:
            prime = 0
    
    if prime == 1:
        for divider in range(11, int(math.sqrt(number))+1, 2):
            if number % divider == 0:
                prime = 0
                break

    if prime == 1:
        found += 1


end = time.monotonic()
print('\nThis took:', (end - start), 'seconds.')
print('Found: ',found)
```

## CoreMark

This has do be adjusted. And test the two RISC cores!

## CPU Frequency

Easy tested with Circuitpython, has only 150 MHz instead of 200. Why?

``` py
import microcontroller
print(microcontroller.cpu.frequency)
```
