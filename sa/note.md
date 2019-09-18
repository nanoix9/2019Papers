---
bibliography: [sa.bib]
---

## Quality attributes

- QA scenario
  + stimulate
  + environment
  + response
  + response measurement
  
# Questions

- form a overview understand the fundamental of SA
  - basic ideas about SA
  - main sub areas about SA

- connections and difference with related concepts


# Notes

## [@vliet2008km]

Going one step further, we may even claim that a software architecture is the set of design decisions

The shift in attention from a solution-oriented view to a decision-oriented view of software architecture has spawn new lines of research.

 A lot of knowledge of a software
development organization is kept in unstructured forms:
FAQs, mailing lists, email repositories, bug reports, lists of
open issues, and so on. Lightweight tools like wikis, weblogs, and yellow pages are other examples of relatively
unstructured repositories to share information in global
projects.

In the knowledge management literature, a distinction
is often made between the personalization strategy and the
codification strategy. The personalization strategy emphasizes interaction between knowledge workers. The knowledge itself is kept by its creator. One personalization strategy is to record who knows what, as in yellow pages. Each
person then has his own way to structure the knowledge.
The threshold to participate is usually low, but the effort to
find useful information is higher. In the codification strategy, the knowledge is codified and stored in a repository.
The repository may be unstructured, as in wikis, or structured according to some model. In the latter case, the structure of the repository can be used while querying.

So the software architecture can be used to reduce the
need or communication in a multi-site development project.



https://en.wikipedia.org/wiki/Software_architecture_description#Architecture_description_via_decisions
https://en.wikipedia.org/wiki/Software_architecture
http://www.informit.com/articles/article.aspx?p=2738304&seqNum=4



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




## Logical View

1. Primary presentation

> box & line - try to use UML

2. Element catalog

> explain each box & line

  - Elements and their properties
  - Relations
  - Element interfaces
  - Element behavior

3. Context diagram

4. Variability guide

5. Architecture background
  - Rationale
  - Analysis results
  - Assumptions

6. Other information

7. Related view packets

