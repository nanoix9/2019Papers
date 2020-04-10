---
topic: 5. Noise removal using deep learning
documentclass: article
title: Self-supervised image denoising with deep neural networks
# author: "Stone Fang (Student ID: 19049045)" 
header: "COMP825: Deep Learning Research Proposal"
# footer: "Stone Fang (19049045)"
pagestyle: "empty"
biblio-style: apa
biblio-title: Reference
bibliography: [dl.bib]
biblatexoptions:
    - backend=biber
papersize: a4
# mainfont: Times New Roman
# mainfontoptions:
#     - Mapping=tex-text
fontsize: 12pt
linestretch: 1.5
geometry:
    - margin=25mm

header-includes:
    - \let\Phi\varPhi
    - \fancypagestyle{plain}{\pagestyle{fancy}}
    - \usepackage{txfonts}
    # - \usepackage{newtxtext,newtxmath}

# - \usepackage{txfonts}
# - \usepackage{mathptmx}

tblPrefix: table
secPrefix: section

abstract: |
    This project studies deep learning based image denoising approaches without the requirement of clean targets in the same domain for model training. For this purpose, self-supervised and meta-learning methods will be conducted. This study will reach effective and practical image denoiser, being evaluated on a few datasets especially those containing real-world images.

---

# Introduction

<!-- > (research problems, existing solutions, novel solutions or creative contributions, significance, etc.) -->

Removing noise from degraded images to recover high quality ones, known as image denoising, is a fundamental task in computer vision. It has been a classic research area yet remains active nowadays [@gu2019]. It not only greatly affects user experience in practical applications, but also plays a very important role for subsequent computer vision tasks such as classification and recognition [@gu2019].

A widely accepted yet simple image degradation model is $\boldsymbol{y} = \boldsymbol{x} + \boldsymbol{n}$ where $\boldsymbol{x}$ refers to the uncorrupted image, $\boldsymbol{y}$ represents the degraded image and $\boldsymbol{n}$ is the additive noise [@gu2019; @zhang2017]. Several kinds of noises has been widely studied, including additive white Gaussian noise (AWGN), Poison noise, and salt-and-pepper noise [@gu2019]. 

The biggest challenge in image denoising is the loss of information during degradation, making this problem highly ill-posed [@lee2020meta; @gu2019]. As a result, prior knowledge is required to compensate the lost information to recover high quality image [@gu2019]. This can be the prior modelling of either the images or noise [@chen2018].

<!-- 
Based on the information used in modelling, image denoising methods can roughly be divided into two categories [@gu2019]:

- Internal: only use the noisy images
- External: use both noisy and clean (ground truth) images

The two kinds of approaches can be combined or mixed to reach better performance [@gu2019].  -->

A variety of models have been proposed for image prior representation, including some state-of-art ones such as non-local self-similarity-based methods BM3D or WNNM [@zhang2017; @Valsesia2019]. The most popular and classic one is BM3D, which serves as a benchmark in image denoising [@chen2018]. However, there are some major disadvantage of these models. First, they mostly rely on human knowledge. Second, they only utilise the information of a single input image [@chen2018].

In recent years, deep neural networks (DNNs) have revolutionised traditional methods and became the state-of-art technology on most tasks of computer vision [@gu2019]. In terms of image denoising, a variety of DNN models have been proposed, attracting increasing attentions attributed to its performance. Models based on Convolutional Neural Networks (CNNs) achieved significance, such as RED [@mao2016] or DnCNN [@zhang2017]. More recent technologies are also introduced to image denoising, such as Generative Adversarial Networks (GANs) [@chen2018], Graph Neural Networks (GNNs) [@Valsesia2019], and meta-learning [@lee2020meta].

# Related work 

<!-- > (existing work organized in categories, critical summery and analysis, and statement of contributions, etc.) -->

There are several CNN-based image denoising models. RED-Net was proposed in [@mao2016] for denoising in different noise levels with a single model. It is a very deep architecture (up to 30 layers in experiment) which consists of convolutional and deconvolutional layers, with skip connections between each convolutional layer and its symmetric deconvolutional one. The skip connections helps passing gradients in back-propagation to alleviate gradient vanishing problem. <!-- This model outperforms existing state-of-art models in image denoising, and is claimed to be the first approach with good metrics working at different noise levels with a single model. --> DnCNN [@zhang2017] combines residual learning strategy and batch normalisation into feed-forward convolutional neural network to improve the final model metrics and also to accelerate the training process. DnCNN learns the residual (i.e. difference between the noisy and clean image) instead of the clean image itself. This model outperforms state-of-art methods such as BM3D, WNNM and TNRD, and can be effectively extended to more general image denosing tasks such as blind Gaussian denoising. A recent study [@Valsesia2019] introduced graph neural networks to CNN-based image denoising architecture. Because of the local nature of convolutional operation, CNN-based model is unable to exploit non-local similarity patterns which had been proven to be significant by previous model-based methods. As a response, GraphCNN was proposed by incorporating the Edge Conditioned Convolution (ECC), a graph convolutional layer, to create non-local receptive field. This method improved the metrics on average, but did not beat existing methods on some categories in their experiment.

Some attempts has been made to loosen the requirement for training data. @chen2018 proposed a GAN-CNN Based Blind Denoiser (GCBD) model, arguing that in real world applications noise is not ease to obtain and is usually more complex than Gaussian noise, thus the models trained for knowing noises might significantly decrease in performance. To solve this problem, the GCBD utilise a two-stage model. First, a GAN is trained to model the noise distribution. Second, the noise sampled from previous step are paired with real images, resulting in a proper training dataset for deep CNN based denoising models. Though this method does not require noisy and clean image pairs for training, it still needs clean images. Another method named Noise2Noise [@lehtinen2018noise2noise] learns a denoising model with noisy data only, based on an basic observation that the loss function will not be affected by the change of distribution of targets as long as it remains the same expectation. This model can be trained in the absence of clean images yet achieves comparable performance, if not better, of models trained from dataset with clean targets. The capability of Noise2Noise was demonstrated by experiments with various noises and images, but they only covered synthetic noises. Another drawback of this method is that it needs different noisy observations of the same image. Going one step further, Noise2Void [@Krull_2019_CVPR] implements image denoising with only a single noisy input, and can be applied to many existing neural network architectures. In this approach, the author introduce the blind-spot network, trained by patches extracted from noisy image with the center pixel masked. Experiments were carried out on both synthetic and real noisy images, however, the results on real data were evaluated by human vision due to the absence of ground truth. A latest research [@lee2020meta] proposed a two-phase denoiser which first utilised an arbitrary pre-trained denoiser $g$ and augmented the available patches at self-supervision stage by adding random noise to the output of $g$. To gain benefit from supervised learning on large labelled datasets, a meta-learning approach was employed for fast adaptation to test inputs. <!-- The distribution of training dataset was not necessarily be identical to the test input, enabling this model to utilise large amount of available image datasets to learn general knowledge. -->

Many image datasets can be used for denoising model evaluation with synthetic noises, such as Set14 [@zeyde2010] <!--, BSD300 [@Martin01] --> and <!-- its newly extended version --> BSD500 [@bsd500]. <!-- It is worth noticing that --> Some real world data are available as benchmark. For example, Darmstadt Noise Dataset (DND) [@Plotz_2017_CVPR] contains 50 pairs of images captured by consumer cameras at different ISO values, with the low-ISO ones as ground truth.

# Methodology

<!-- > (research design, research methods, modelling and algorithms, etc.) -->

This research will be conducted based on several state-of-art approaches and experiments. Several existing studies have given us useful guidelines in choosing model architecture. First of all, CNN has been proved to be effective and successful in image denoising [@mao2016], so this study will focus on CNN-based approach. Second, residual learning and batch normalisation are great methods to improve the final model metrics [@zhang2017], so they will be included in this study. Finally, graph neural network, as one of the newest technology, has been successfully introduced into image denoising recently [@Valsesia2019]. GNN has great potential capability of exploiting non-local features, and will be studied with special attentions in this research.

Training strategy is another important aspect of this research. This study aims to effective and practical image denoising method without dependency on large in-domain labelled training dataset. For this purpose, self-supervised approaches such as Noise2Noise [@lehtinen2018noise2noise] and Noise2Void [@Krull_2019_CVPR] are promising candidates. Moreover, meta-learning has been proved to be effective to improve the model metrics and speed up model inference [@lee2020meta], and thus will be investigated in this study. GAN-based noise modelling [@chen2018] is another measure to alleviate the lack-of-data problem, which can be introduced to the two-phase denoiser [@lee2020meta] for patch generation with more realistic noise distributions.

# Timeline and milestones

  Task                                                     | Deadline
 ----------------------------------------------------------|-----------
  Final decision on the topic, create research questions   | 1 week
  Literature review	                                       | 3 weeks
  Research proposal draft                                  | 1 week
  Prototyping                                              | 4 weeks
  First round of testing and analysis                      | 4 weeks
  Model improvement                                        | 4 weeks
  Second round of testing and analysis                     | 4 weeks
  Write and present final results                          | 4 weeks

# Research resources

Deep learning models are computational intensive, and recent models to be studied such as GAN, GNN, meta-learning are even more so. Proper hardware sets includes Intel i7 series CPU, an Nvidia Titan X series or 2080Ti GPU, and 1T disk storage. Tensorflow or Pytorch will be chosen as the modelling framework in consideration of many existing works having been implemented in either framework.

# Planned outcomes and risks

The expected outcomes of this research are practical image denoising systems that are effective on real world environments and applications. It will utilise state-of-art technologies for novel solutions at this aim, and will improve the metrics (PSNR) on particularly real world image datasets such as DND [@Plotz_2017_CVPR].

The biggest risk of this research is that the expected improvement cannot be achieved for certain methods. To reduce such risk, more methods could be included and combined, and flexibility of up to 4 weeks will be introduced into schedule.

