---
topic: 5. Noise removal using deep learning
documentclass: article
title: COMP825 Deep Learning Research Proposal
subtitle: 
author: "Stone Fang (Student ID: 19049045)" 
header: "COMP825: Deep Learning"
footer: "Stone Fang (19049045)"
pagestyle: "empty"
bibliography: [dl.bib]
papersize: a4
mainfont: Times New Roman
fontsize: 12pt
linestretch: 1.5
geometry:
    - margin=25mm

header-includes:
    - \let\Phi\varPhi
    - \fancypagestyle{plain}{\pagestyle{fancy}}

tblPrefix: table
secPrefix: section

abstract: |
    project significance, project methods, contributions, and evaluations

---

# Introduction

> (research problems, existing solutions, novel solutions or creative contributions, significance, etc.)

Removing noise from degraded images to recover high quality ones, known as image denoising, is a fundamental task in computer vision. It has been a classic research area yet remains active nowadays [@gu2019]. In addition, it not only greatly affects user experience, but also plays a very important role for subsequent computer vision tasks such as classification and recognition [@gu2019].

A widely accepted yet simple image degradation model is

$$ \pmb{y} = \pmb{x} + \pmb{n} $$
{#eq:degrad}

where $\pmb{x}$ refers to the uncorrupted image, $\pmb{y}$ represents the degraded image and $\pmb{n}$ is the additive noise [@gu2019]. Several kinds of noises has been widely studied, including additive white Gaussian noise (AWGN), Poison noise, and salt-and-pepper noise [@gu2019]. 

The biggest challenge in image denoising is the loss of information during degradation, making this problem highly ill-posed [@gu2019]. As a result, prior knowledge is required to compensate the lost information to recover high quality image [@gu2019]. This can be the prior modelling of either the images or noise [@chen2018].

> internal (use solely the input noisy image) [7, 25, 40] and external (use external images with or without noise) [98, 54, 75, 93] denoising methods. Some works shown that the combination or fusion of internal and external information can lead to better denoising performance [9, 60, 78, 37].

Based on the information used in modelling, image denoising methods can roughly be divided into two categories [@gu2019]:

- Internal: only use the noisy images
- External: use both noisy and clean (ground truth) images

The two kinds of approaches can be combined or mixed to reach better performance [@gu2019].

In recent years, deep neural networks (DNNs) overtakes traditional methods and became the state-of-art technology on almost every task of computer vision [@gu2019]. In image denoising, a variety of DNN models have been proposed. DNN-based methods requires less human interactions and achieves better performance [@tian2019]. 

# Related work 

> (existing work organized in categories, critical summery and analysis, and statement of contributions, etc.)

DnCNN [@zhang2017]
RED [@mao2016]
MemNet [@mao2016]

> FDnet [38](Multi-bintrainablelinearunitforfastimagerestoration networks.)

GAN-CNN Based Blind Denoiser (GCBD) [@chen2018]
GraphCNN [@Valsesia2019]

# methodology

> (research design, research methods, modelling and algorithms, etc.)

# timeline and milestones (terms/quarters-based)

  Task                                                     | Deadline
 ----------------------------------------------------------|-----------
  Final decision on the topic, create research questions   | February 1st, 2020
  Literature review	                                       | March 1st, 2020

# research resources

> (hardware, software, budgets, settings, etc.)

# planned research outcomes and ways of quality assurance (avoiding risks)

# references

> (9 references at least in total). 

\pagebreak
