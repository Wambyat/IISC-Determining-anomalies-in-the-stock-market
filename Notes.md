# Determining anomalies in a stock exchange though a combination of information from social media and information from order book

*These are just notes for myself. Ignore it.*

### CNN

---

| Parameter  | Use                                                                |
|:---------- |:------------------------------------------------------------------ |
| F          | Kernel/ Filter. This is the matrix that we will be sliding.        |
| K          | This is the number of different filters/ kernels we will be using. |
| S          | Stride. This is by how much the filter moves.                      |
| P          | Padding. This is padding of values around the input.               |
| W,D,H      | Width, Depth, Height                                               |
| Parameters | This is the number of things we will be using for the computation  |

$$
Wo = {Wi - F +2P \over S }+1
$$

$$
Ho = {Hi - F +2P \over S }+1
$$

$$
Do = K
$$

$$
Parameters = K * F * F * D
$$

Pooling layer is pretty much a compression type of layer. Depth usually remains the same. So we say the parameters is 0.

Fully Connected Layer is the last few layers. Here we will be "flattening" the last output. Eventually if  it is a classification type thing then we will make it into a layer with the number of classes as a dimension. These layers are usually the largest.

<img src="file:///C:/Users/Anirudha/AppData/Roaming/marktext/images/2023-06-12-12-51-41-image.png" title="" alt="" data-align="center">

This is AlexNet. This has 8 layers. % convolutional and 3 fully connected. We do not count the pooling layers as they have 0 parameters.



### Inception Module

<img src="file:///C:/Users/Anirudha/AppData/Roaming/marktext/images/2023-06-12-13-12-45-image.png" title="" alt="" data-align="center">

Here we will be using kernels of different sizes parallelly. We will do a 1x1 convolution and a 3x3 pooling+1x1 convolution. Along with this we will do a 1x1 convolution + 3x3 convolution and 1x1 convolution + 5x5 convolution. After this we will use a filter to concatenate the outputs.



The number of 1x1 is varied and the sizes of convolution are varied (3x3 and 5x5).



We know that the FCI is usually very large. To reduce its size we will do average pooling on the last layer. So if the last layer is 7x7x512 we will convert it to only 512. 



![](C:\Users\Anirudha\AppData\Roaming\marktext\images\2023-06-12-13-20-06-image.png)

This is GoogLeNet.





![](C:\Users\Anirudha\AppData\Roaming\marktext\images\2023-06-12-13-27-19-image.png)

What are these :,(
