# Meta Mountains

## Solution

Just running strings on the image and searching for the string "flag" returns some interesting results :

```bash
$ strings mountains_hsctf.jpg | grep "flag"
```

```
part 1/3: flag{h1dd3n_w1th1n_
  <tiff:Model>part 1/3: flag{h1dd3n_w1th1n_</tiff:Model>
```

So the next thing I checked for was the string "part"

```bash
$ strings mountains_hsctf.jpg | grep "part"
```

```
part 1/3: flag{h1dd3n_w1th1n_
part 2/3: th3_m0unta1ns_
part 3/3: l13s_th3_m3tadata}
  <tiff:Model>part 1/3: flag{h1dd3n_w1th1n_</tiff:Model>
```

Putting these results together gives us the flag.

Flag : `flag{h1dd3n_w1th1n_th3_m0unta1ns_l13s_th3_m3tadata}`
