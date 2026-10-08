# Circuitpython on the Raspberry Pico 2 - rp2350


## Prime calculation

Check Frequency:

``` py
import microcontroller
print(microcontroller.cpu.frequency)
```

It is twice as fast as the rp2040 while still running at 150 MHz (vs. 133 MHz)

### Result of 200 MHz

| Arduino C     |   rp2040   |   rp2350   |
|---------------|:----------:|:----------:|
| primes to     | Cortex M0+ | Cortex M33 |
|           100 |      0.000 |      0.000 |
|         1,000 |      0.001 |      0.001 |
|        10,000 |      0.017 |      0.007 |
|       100,000 |      0.235 |      0.105 |
|     1,000,000 |        3.7 |        1.7 |
|    10,000,000 |         67 |         32 |
|    25,000,000 |        220 |        107 |
|   100,000,000 |       1381 |        680 |
| 1,000,000,000 |      31283 |      16655 |
| 2,147,483,647 |      89314 |      48246 |
| 4,294,967,295 |     232324 |     125061 |
|               |     64h    |     35h    |
|               |    2days   |    1day    |
