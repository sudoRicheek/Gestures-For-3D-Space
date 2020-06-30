# Gestures For 3D Space

<img align="left" src="https://www.wncc-iitb.org/images/wncc.jpg" title="WnCC IITB" width="250" height="141"/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
A **Summer of Code** project under **WnCC IITB** for designing both the front and back-end of a real-time gesture detection module. Everything related to the project including notes/implementations and related links to those will be hosted here.

&nbsp;&nbsp;&nbsp;&nbsp;
**Final Task** of One Shot Learning can be found [here](https://github.com/sudoRicheek/Siamese-Net-One-Shot-Learning)

&nbsp;&nbsp;&nbsp;&nbsp;
**Real Application** of Gesture Model can be found [here](https://github.com/sudoRicheek/Gestures-For-3D-Space/tree/master/Notes%20And%20Basic%20Implementations/Gesture%20Application%20Model)

## Related Links

### **[Progress Report](https://docs.google.com/document/d/1UUgWrgOsen2bv99KKsDdN1S9QIDGQYNN3X7IKYqO13c)**

  This is the link to the **detailed progress report** that will be maintained by me throughout the entire duration of this project, as a roadmap of requirements for this project and also, to keep a track of the resources and references that I'm using in this project. Most of the stuff that are not mentioned in this README can be found in the link above.

### **[Finger Count Recogniser](https://github.com/sudoRicheek/Finger-Count-Recogniser-OpenCV)**
  
  This is a preliminary model of a Finger Count Recogniser, using the direct video feed of the webcam. This model has been kept simple,     with OpenCV as its only dependency, so as to study the comparative improvements in the future models which will be utilising **CNN**s and other Machine Learning techniques.
  
### **[Summary Of A Paper Exploring DeConvolutional Networks](https://github.com/sudoRicheek/Gestures-For-3D-Space/blob/master/Notes%20And%20Basic%20Implementations/DeConvolutional%20Networks%20Summary.pdf)**
  
  Here, you can find my summarized version of this [paper](https://www.google.com/url?sa=t&source=web&rct=j&url=https://cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf&ved=2ahUKEwjcsrbOzPToAhVt7nMBHV9GAlYQFjAQegQIBxAB&usg=AOvVaw3ga-MmEmZLvVUSuQhiPog8&cshid=1587303221548), by **Matthew D. Zeiler and Rob Fergus from the Dept. of Computer Science, New York University, USA** which mainly explores the novel way of **Visualizing and Understanding Convolutional Networks** through *DeConvNets*.
  
### **[Dataset Creator For Hand Gestures](https://github.com/sudoRicheek/Dataset-Creator-For-Hand-Gestures)**

  I wrote this *OpenCV* code to easily and quickly create my own hand-gesture image datasets for this project. It implements background subtraction and binary thresholding and saves both the original colour image with 3 channels and the processed single channel image.
  
### **[Gesture Detection CNN Models Using Transfer Learning](https://github.com/sudoRicheek/Gestures-CNN-Model-Creation-And-FineTuning)**

  The above, repo hosts some of the notebooks and stuff that I had created while making the **CNN** Transfer Learning models for this project.
  
### **[Trained CNN Model](https://drive.google.com/open?id=1yq6uEnXjBGXjME-CNTskK3_gB2tdBPIk)**

  Here you can find the **CNN Model** trained for gesture recognition. The notebooks created for training the neural net can be found in the last bullet point.
  
### **[Gesture Application Model](https://github.com/sudoRicheek/Gestures-For-3D-Space/tree/master/Notes%20And%20Basic%20Implementations/Gesture%20Application%20Model)**

  The above piece of code is an implementation of an on-the-go gesture recognizer using a continuous video input through the webcam feed. To check the practical implications of this model, I added some basic fun-features like using gestures to play and pause videos, change current working application window and some volume modulation features as well. It has **PyAutoGUI**, **OpenCV**, **Keras** and **My CNN Model** in the last *Google Drive Link* as its dependencies.

### **[Image Enhancer](https://github.com/sudoRicheek/Image-Enhancer)**

  This is a PyQt5 based open-source, cross-platform app, developed for **upscaling low resolution images upto 4x its initial resolution** using *SOTA Super Resolution GANs*.
  
### **[Summary Of A Paper Exploring Sliding Windows For Making SOTA CNNs Usable In Real-Time Gesture Detection Module](https://github.com/sudoRicheek/Gestures-For-3D-Space/blob/master/Notes%20And%20Basic%20Implementations/Real-Time%20Hand%20Gesture%20Classification%20using%20SOTA%20CNN.pdf)**

  This is a review of a quite recent [paper](https://arxiv.org/abs/1901.10323) of 2019 titled “Real-time Hand Gesture Detection and Classification using Convolutional Neural Networks” and it aims to address issues faced by real-time recognition of
dynamic hand gestures using *state-of-the-art* CNNs.

### **[SRS Siamese NN One Shot Learning](https://github.com/sudoRicheek/Gestures-For-3D-Space/blob/master/SRS%20One%20%20Shot%20Learning.pdf)**

  This is the SRS Document for the **Siamese Neural Network** training codes for detecting Hand Gestures with minimal dataset(One Shot Learning).
  
### **[Siamese Networks for One Shot Learning of Hand Gestures](https://github.com/sudoRicheek/Siamese-Net-One-Shot-Learning)**

  This repo will house the model training codes and explanations, for building a **Siamese Neural Network** for **Hand Gesture Classification using minimal datasets**.

### **[Neural Networks and Deep Learning](https://github.com/sudoRicheek/NeuralNetworks-And-DeepLearning-SoS)**

  This is the link to the heavily related **Summer Of Science** project that I've taken up alongside my **SoC** project. It will house all the notes and implementations that I'll create throughout the summer break of 2020 on this topic.

## Author

Learning with :heart: Richeek Das . Copyright 2020
