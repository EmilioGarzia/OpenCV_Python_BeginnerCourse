# <font color="red">Convolution</font>
The application of filters involves a simple stellar convolution between the mask *(or kernel)* with the image, everything happens in the domain of space and conceptually we can see it as a simple tile *(usually 3x3)* which is scrolled on each individual pixel taking into account the central pixel of the mask, however it is always possible to change the point of origin with a different pixel of the mask from the central one.

## <font color="blue">Operazione effettuata dalla convoluzione</font>
Quando facciamo scorrere il kernel su ogni singolo pixel della immagine nella immagine di output quello specifico pixel avrà come nuovo valore la somma dei prodotti di ogni pixel del kernel per il corrispettivo pixel sull'immagine di input.

![convolution](images/convolution.png)

In the image above it is clear that the first pixel at the coordinates `(0,0)` has been assigned the value `114` due to the following calculation:  

$$
0\bullet0 + 0\bullet(-1) + 0\bullet0 + 0\bullet(-1) + 60\bullet5 + 113\bullet(-1) + 0\bullet0 + 73\bullet(-1) + 121\bullet0 =
$$

$$
= 0 + 0 + 0 + 0 + 300 - 113 + 0 - 73 + 0 = 300-113-73 = \color{red}114
$$

This is the general mechanism of applying stellar convolution, so changing the values of the kernel matrix you can get various types of effects on the image.

## <font color="blue">Filters</font>
We now want to see some of the most used *(kernel)* filters

#### Mean Filter (Blurring)
| | | |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 1 | 1 |
| 1 | 1 | 1 |

#### Prewitt Filter (Vertical Edge Detection)
| | | |
|---|---|---|
| -1 | 0 | 1 |
| -1 | 0 | 1 |
| -1 | 0 | 1 |

#### Prewitt Filter (Horizontal Edge Detection)
| | | |
|---|---|---|
| -1 | -1 | -1 |
| 0 | 0 | 0 |
| 1 | 1 | 1 |

#### Laplacian Filter invariant at 90° rotations (Edge Detection)
| | | |
|---|---|---|
| 0 | 1 | 0 |
| 1 | -4 | 1 |
| 0 | 1 | 0 |

#### Laplacian Filter invariant at 45° rotations (Blurring)
| | | |
|---|---|---|
| 1 | 1 | 1 |
| 1 | -8 | 1 |
| 1 | 1 | 1 |

#### Sharpening Filter (Sharpness)
| | | |
|---|---|---|
| 0 | -1 | 0 |
| -1 | 5 | -1 |
| 0 | -1 | 0 |

#### Sobel Filter (Horizontal Edge Detection)
| | | |
|---|---|---|
| -1 | -2 | -1 |
| 0  | 0 | 0 |
| 1 | 2 | 1 |

#### Sobel Filter (Vertical Edge Detection)
| | | |
|---|---|---|
| -1 | 0 | 1 |
| -2  | 0 | 2 |
| -1 | 0 | 1 |

## <font color="blue">Gradients Operator</font>
This class of filters is useful for detecting diagonal edges, the easiest ones to use are **Roberts**

#### Roberts filter ($g_x$)
| | |
|---|---|
| -1 | 0 |
| 0  | 1 |

#### Roberts filter ($g_y$)
| | |
|---|---|
| 0 | -1 |
| 1 | 0 |

However, there are also gradient operators based on **Prewitt** and **Sobel**:

#### Prewitt Filter ($g_x$)
| | | |
|---|---|---|
| 0 | 1 | 1 |
| -1  | 0 | 1 |
| -1 | -1 | 0 |

#### Prewitt Filter ($g_y$)
| | | |
|---|---|---|
| -1 | -1 | 0 |
| -1  | 0 | 1 |
| 0 | 1 | 1 |

#### Sobel Filter ($g_x$)
| | | |
|---|---|---|
| 0 | 1 | 2 |
| -1  | 0 | 1 |
| -2 | -1 | 0 |

#### Sobel Filter ($g_y$)
| | | |
|---|---|---|
| -2 | -1 | 0 |
| -1  | 0 | 1 |
| 0 | 1 | 2 |

You can apply more complex filters *(always based on gradients)* like the famous **LoG** *(Laplacian of Gaussian)* also known as *the sombrero operator*:

#### Filtro LoG
| | | | | |
|---|---|---|---|---|
| 0 | 0 | -1 | 0 | 0 |
| 0 | -1 | -2 | -1 | 0 |
| -1 | -2 | 16 | -2 | -1 |
| 0 | -1 | -2 | -1 | 0 |
| 0 | 0 | -1 | 0 | 0 |

## <font color="blue">Apply filters with filter2D() method</font>

This method allows us to apply a 2D filter to an image by applying a stellar convolution between the kernel and the image.  
The prototype of this function is:

```python
#filter2D prototype
import cv2
cv2.filter2D(src, ddepth, kernel, dst, anchor, delta, borderType)
```

As regards the parameters of the method:

* `src` &rarr; The source image to apply the kernel to.

* `ddepth` &rarr; The output image depth is usually set to `-1` so that the output image can have the same depth as the input image, with the term depth refers to the image matrix data type *(for example, "uint8")*.

* `kernel` &rarr; The mask *(filter)* that we want to apply to the image.

* `dst` *(optional)* &rarr; The array in which the filtered image will be contained.

* `anchor` *(optional)* &rarr; The point in the image where the convolution with the filter is to be applied, usually the kernel center point is chosen, that is by setting this value with `(-1,-1)`

* `delta` *(optional)* &rarr; An additional value that is added after convolution to the input image, changing this value may result in changes in the brightness of the resulting image, by default `delta = 0`.

* `borderType` *(optional)* &rarr; How edges are handled during convolution.
