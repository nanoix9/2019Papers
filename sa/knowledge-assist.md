---
title: A Knowledge Extraction and Presenting System
author: "Stone Fang (ID: 19049045)" 
bibliography:
    - sa.bib
---

# Overview

My topic is a system for knowledge extraction, presenting, and searching. The ultimate goal of this system is to help people to find and learn knowledge more efficiently.

# Motivation

We are living in a data explosion time. We have numerous and rapid-growing amount of data, which makes it harder to extract useful information from it, and even more difficult to acquire real knowledge. For example, when I get started to do research on a new topic (that happens all the time), first I need to get familiar with the basic concepts in that topic, how its position in a bigger background, and how it relates to or different from similar concepts. To do this, the researcher usually collects surveys in this topic or simply go to the Wikipedia page for a quick review. However, the researcher needs to go through the articles, select important parts and key concepts, and form a mental representation in the brain. I think we can do something better: what if there is a system which displays the knowledge, not in the plain sequential text, but a more intuitive and structured way? If so, we can get familiar with new areas and learn new things in a shorter time.


# Features

This system will have the following features:

- extracting and structuring knowledge from a variety of sources mainly text or semi-structured data, e.g. Wikipedia

- visualization of knowledge, i.e. display knowledge in more intuitive, fast-and easy-reading ways

- effective searching for specific knowledge or concept with its preceding and related concepts


# Why new

So far as I know, though there are existing knowledge graph systems similar to this, my system is different. First, knowledge graph is, obviously, a graph, but my system is not necessarily a graph, though I admit graph is a more intuitive and fast-reading way than text. Second, knowledge graph is created mainly to improve search engine or other natural language processing models, but my system focus on helping people in processing knowledge. In addition, we have Wikipedia or other encyclopedias as knowledge bases, but they are mainly organized in natural language and slightly structured. In this sense, my system is new.


# Why large scale

My system is about knowledge, and obviously, the amount of knowledge and the data to be processed is large. Even just limit to Wikipedia as the source, it is still very large. Therefore, a system to process, store, and present knowledge is inherently large-scaled.

# Comments

Actually, I prefer the knowledge gathering process to be automatic by say some machine learning approach because we already have some high-quality, well-organized human-edited knowledge sources such as Wikipedia and extracting from them are feasible and time-saving. However, it's also reasonable to provide the function of manual correction of mistakes made by machines.

Since it's machine learning approaches for knowledge extraction, we will probably not get an algorithm with high accuracy at the beginning.  Therefore I want my system to be extensible in supporting improvements or even completely new algorithms. In addition, I think this is also the case for knowledge representation and storage as you mentioned, i.e. the form or data structure which stores and represents knowledge might be improved or even replaced if a better one were invented. 

Obviously, this system must involve some machine learning or knowledge engineering algorithms, but this architectural design focuses on the system & engineering aspects instead of the machine learning aspect. Since the data structures and algorithms for knowledge extraction and representation might evolve over time, the system architecture will provide some feasibility and extensibility to fit this requirement. E.g. the system will not simply use graph or tree as knowledge representation, but support a range of representations and storages and even future changes. 

# Architectual Drivers

## Stakeholders' Concerns

### Stakeholders

These models provide a set of quality characteristics relevant to a wide range of stakeholders, such as: software developers, system integrators, acquirers, owners, maintainers, contractors, quality assurance and control professionals, and users.[@isoiec25010]

1. Primary user: person who interacts with the system to achieve the primary goals.
2. Secondary users who provide support, for example
    a) content provider, system manager/administrator, security manager;
    b) maintainer, analyzer, porter, installer.
3. Indirect user: person who receives output, but does not interact with the system.[@isoiec25010]

### Functional
### Qualities

system/software product quality properties into eight characteristics: functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability and portability.[@isoiec25010]

## Business and technical constraints

---

## Business goals and constraints

what value would this system add to a company/business/community/government? Note any business considerations and constraints.

## Technical goals, assumptions and constraints

any technical decisions and assumptions that will not change throughout the project should be explained and justified in this section.

## Primary functional requirements

What system features require explicit support from or can impact on its architecture? Explain how you identified these.

## Quality attributes

Explain the most important quality attributes for the system, along with the process you followed to identify and prioritise them.

## Evaluation criteria

Explain how you will evaluate an architecture based on the drivers identified in sections 2-5.