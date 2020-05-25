---
title: Self-supervised Image Denoising with Deep Neural Networks
author: "Stone Fang (Student ID: 19049045)" 
date: 25 May 2020

# theme: Darmstadt
# theme: Copenhagen
# theme: Montpellier
# theme: Singapore
# theme: Rochester
# theme: metropolis

# colortheme: seahorse

fontsize: 12pt
fontenc: T1
# fontenc: "LGR,OT1"
# fonttheme: professionalfonts
# linestretch: 1.5

# mainfont: Futura Medium
# mainfontoptions: |
#     ```{=latex}
#         ItalicFont={Futura Medium Italic}
#     ```
# mainfont: Flama-Light

biblio-style: apa
biblio-title: References
bibliography: [dl.bib]
biblatexoptions:
    - backend=biber

toc-title: Outline

bibfont: \tiny

header-includes:
    - \usepackage{bm}
    - \usepackage{../style/beamer/beamerthemeaut}
    # - \metroset{sectionpage=none}
    # - \usepackage{ptsans}
    # - \usepackage{libertine}
    # - \usepackage[sfdefault,lf]{carlito}
    # - \usepackage[sfdefault,lining]{FiraSans}
    # - \usepackage[defaultsans]{droidsans}
    # - \usepackage[sfdefault]{roboto}
    # - \usepackage{epigrafica}
    # - \usepackage[sfdefault]{FiraSans} \usepackage{newtxsf}
    # - \usepackage[default]{gillius}
    - \usepackage{lmodern}
    # - \usepackage{sfmath}

    # - \setmainfont{Flama-Light}
    # - \setmathfont{Fira Math}

    # - \newcommand*{\bm}[1]{\symbfit{#1}}

    - \let\realcite\autocite
    - \renewcommand*{\autocite}[1]{{\color{gray}\scriptsize\realcite{#1}}}

---

# Introduction

## Introduction

- Image denoising: a fundamental task in computer vision (CV)

- Degradation model: $\bm{y} = \bm{x} + \bm{n}$ 
  + $\bm{x}$: uncorrupted image, ground truth
  + $\bm{y}$: degraded image, model input
  + $\bm{n}$: additive noise

- Key challenge: highly ill-posed problem: loss of information during degradation

- General idea of solution: Prior knowledge for either
  + Image modelling
  + Noise modelling
  

# Literature Review

## Literature Review

- Traditional methods: BM3D (popular benchmark), WNNM
- RED-Net: Deep CNN + skip connection [@mao2016] 
- DnCNN: Deep CNN + residual learning + batch normalisation [@zhang_beyond_2017]
- FFDNet: Noise map for noise level. Flexible to spatially variant noise [@zhang_ffdnet_2018]
- GCBD: GAN for noise modelling [@chen2018]
- Self-supervision: Noise2Noise [@lehtinen2018noise2noise], Noise2Void [@Krull_2019_CVPR]
- Meta-learning: fast inference adpation [@lee2020meta] 

# Methodology 

## Methodology {.allowframebreaks}

- Neural Network Architecture
  - CNN-based model: suitable for image processing
  - Residual learning and batch normalisation (DnCNN [@zhang_beyond_2017])
  - Noise map: flexible to noise levels and variant noise (FFDNet [@zhang_ffdnet_2018])
    - improvement: GAN-based noise level estimator

- Self-supervision
  - Still supervised learning, i.e. with labels, but autonomously generated 
    rather than human annotated.
  - Patch-based: learn on patches of a single input
  - Meta-learning: learns a better prior model on large collection of data.

\framebreak

\begin{figure}[htbp]
\newcommand{\gan}{A \\text that}
  \centering
  \fontsize{7}{7}\selectfont
  \def\svgwidth{\columnwidth}
    \resizebox{\textwidth}{!}{\input{model.pdf_tex}}
  \caption{Overall architecture of image denoising model}
\end{figure}

<!-- # Methodology: Dataset & Evaluation -->
\framebreak

- Dataset:
  - Common datasets: Set14, BSD500, DIV2K, etc
  - Real noisy images: DND, SIDD

- Evaluation: PSNR: Peak Signal to Noise Ratio

    $$PSNR = 10 \log_{10} \left( \frac{R^2}{MSE} \right)$$

  + $R$ is the maximum fluctuation
  + $MSE$ is the Mean Squared Error between model output and ground-truth

# Timetable

## Timetable

\small

  Task                                                     | Deadline
 ----------------------------------------------------------|-----------
  Final decision on the topic & research questions         | 1 week
  Literature review	                                       | 3 weeks
  Research proposal draft                                  | 1 week
  Prototyping                                              | 4 weeks
  First round of testing and analysis                      | 4 weeks
  Model improvement                                        | 4 weeks
  Second round of testing and analysis                     | 4 weeks
  Write and present final results                          | 4 weeks

