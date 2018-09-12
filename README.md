# Usage
```shell
$ python -m pip install -r requirements.txt
$ python app.py --in path/to/input/file --out path/to/output/file --colors number_of_colors --size size --rstate rstate
```

where
- paths point to image files, input and output respectively
- `number_of_colors` sets number of colors of which color palette will be composed
- `size` sets the number of pixels on the longer rectangle edge
- `rstate` sets random number generator state, used to obtain repeatable results

## Example
```shell
$ python app.py --in .readme/sunrise.jpg --out .readme/sunrise_pixel.jpg --colors 4 --size 128 --rstate 123432
```

Input:
![input](https://raw.githubusercontent.com/dominik-zeglen/pixelbrush/master/.readme/sunrise.png)

Output:
![output](https://raw.githubusercontent.com/dominik-zeglen/pixelbrush/master/.readme/sunrise_pixel.png)
