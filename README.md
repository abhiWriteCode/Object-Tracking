# Object Tracking using OpenCV



### dependencies
```python
pip install opencv-contrib-python==3.4.5.20
```


### Brief highlight of each object tracker below:

1. BOOSTING Tracker: Based on the same algorithm used to power the machine learning behind Haar cascades (AdaBoost), but like Haar cascades, is over a decade old. This tracker is slow and doesn’t work very well. Interesting only for legacy reasons and comparing other algorithms. 

2. MIL Tracker: Better accuracy than BOOSTING tracker but does a poor job of reporting failure. 

3. KCF Tracker: Kernelized Correlation Filters. Faster than BOOSTING and MIL. Similar to MIL and KCF, does not handle full occlusion well. ation Filter (with Channel and Spatial Reliability). Tends to be more accurate than KCF but slightly slower. 

4. CSRT Tracker: Discriminative Correlation Filter (with Channel and Spatial Reliability). Tends to be more accurate than KCF but slightly slower.

5. MedianFlow Tracker: Does a nice job reporting failures; however, if there is too large of a jump in motion, such as fast moving objects, or objects that change quickly in their appearance, the model will fail. 

6. TLD Tracker: I’m not sure if there is a problem with the OpenCV implementation of the TLD tracker or the actual algorithm itself, but the TLD tracker was incredibly prone to false-positives. I do not recommend using this OpenCV object tracker. 

7. MOSSE Tracker: Very, very fast. Not as accurate as CSRT or KCF but a good choice if you need pure speed. 

8. GOTURN Tracker: The only deep learning-based object detector included in OpenCV. It requires additional caffe model files to run.



### My personal suggestion is to:

1. Use CSRT when you need higher object tracking accuracy and can tolerate slower FPS throughput
2. Use KCF when you need faster FPS throughput but can handle slightly lower object tracking accuracy
3. Use MOSSE when you need pure speed