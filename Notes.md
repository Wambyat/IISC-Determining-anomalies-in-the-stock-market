# Determining anomalies in a stock exchange though a combination of information from social media and information from order book

*These are just notes for myself. Ignore it.*

### CNN

---

| Parameter | Use                                                                |
|:--------- |:------------------------------------------------------------------ |
| F         | Kernel/ Filter. This is the matrix that we will be sliding.        |
| K         | This is the number of different filters/ kernels we will be using. |
| S         | Stride. This is by how much the filter moves.                      |
| P         | Padding. This is padding of values around the input.               |
| W,D,H     | Width, Depth, Height                                               |

$$
Wo = {Wi - F +2P \over S }+1
$$

$$
Ho = {Hi - F +2P \over S }+1
$$

$$
Do = K
$$

##### Pooling layer is pretty much a compression type of layer. Depth usually remains the same.


