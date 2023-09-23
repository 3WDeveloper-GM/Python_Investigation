# Power Quality Event Detection Using the Stockwell Transform

![Alt Text](https://github.com/3WDeveloper-GM/Python_Investigation/blob/main/stock.png)


Welcome to the repository for my Bachelor's capstone project conducted at the Universidad Nacional Autónoma de Honduras. This project addresses the critical task of identifying Power Quality Events (PQE) in the power system network. Power Quality Events encompass a wide range of deviations within the power network, including sag, high-frequency harmonics, high-frequency transients, and noise from various connected elements. The objective of this project was to develop a robust solution for detecting these events.

## Project Overview

### Stockwell Transform Approach

To tackle the complexity of identifying PQE, I employed the Stockwell Transform. This mathematical tool served as the foundation for extracting meaningful features from signal data. By utilizing the Stockwell Transform, I aimed to represent the diverse deviations commonly encountered in the power system network in a more accessible format.

### Repository Structure

This repository is organized into three main components:

1. **Signal Deviation Modeling Library:** This library contains Python modules that model the different types of signal deviations encountered in power networks. Each deviation type, including sag, high-frequency harmonics, high-frequency transients, and noise, is represented using mathematical models.

2. **Feature Extraction Visualization Module:** The feature extraction process is crucial to understanding PQE. This module provides tools and visualizations to help you explore the raw feature extraction process, aiding in the comprehension of the Stockwell Transform's effectiveness.

3. **Real-Life Data:** I've included real-life power system data that I gathered during the project. This dataset can serve as a valuable resource for testing and experimentation.

## Methodology

Our Power Quality Event (PQE) detection methodology is designed to identify and classify various deviations in the power system network using a combination of signal processing techniques and machine learning. Below is an overview of the step-by-step approach we employed:

### 1. Data Acquisition

- We begin by acquiring data from the power system using an Analog-to-Digital Converter (ADC).
- The sampling time window is dynamically adjusted based on the nature of the phenomena under analysis.
- For transient events, we sample a specific number of cycles of the AC waveform to capture the event accurately.
- For modeling larger trends or deviations, we increase the number of cycles sampled to ensure comprehensive data collection.

### 2. Data Transformation: Stockwell Transform

- With raw data collected from the power company or utility, we apply the Stockwell Transform. This mathematical technique transforms the time-domain data into a matrix of amplitudes, where each amplitude corresponds to a specific frequency and time point.
- The Stockwell Transform provides us with a time-frequency representation of the signal, enabling us to capture variations over time and across different frequencies.

### 3. Feature Extraction

- We apply a series of statistical transformations to the resulting amplitude matrix. These transformations include measures such as the average, standard deviation, and other statistical metrics.
- These transformations generate a set of curves that encode valuable information about the waveform's characteristics. Each curve corresponds to a particular feature extracted from the signal.

### 4. Classification Using Decision Trees

- The extracted features are then fed into a simple decision tree classifier.
- The decision tree analyzes the characteristics of the waveform and classifies it based on predefined perturbation models.
- These models represent various types of PQE, such as sags, high-frequency harmonics, transients, and noise.
- The classification outcome categorizes the waveform and determines if it exhibits the characteristics of a specific perturbation model.

### 5. Result Analysis

- Post-classification, we analyze the results to identify and categorize Power Quality Events within the power system network.
- The methodology allows us to detect and classify various types of PQE, providing valuable insights into the stability and quality of the power supply.
