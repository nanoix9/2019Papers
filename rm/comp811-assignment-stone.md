---
title: Global Trends and Practical Concerns in Transition from Agile to DevOps
author: "Stone Fang (Student ID: 19049045)" 
bibliography: [rm.bib]
abstract: |
    DevOps is an emerging trend of software development in recent years, and is closely related to Agile software development method. In this study, the trend of transition from agile to DevOps and practical issues concerned by practitioners are studied from both global and regional viewpoints. Following a qualitative approach, data collected from four websites are analysed by thematic analysis. The findings are classified into seven categories. It is discovered that collaboration, organisation, goals and values are more concerned over knowledge, technology and tools. This study is expected to be an in-depth understanding of the movement from agile to DevOps.
    

papersize: a4
# mainfont: Arial
fontsize: 12pt
linestretch: 1.25
geometry:
    - margin=25mm
tblPrefix: table
secPrefix: section
---

# Introduction

## Background

DevOps, commonly accepted as a combination of development and operation, is dramatically gaining its popularity among both academic researchers and industrial practitioners in recent years [@Jabbari:2016:what-is-devops] [@erich:2017:devops-practice]. It is described as a culture or set of principles to improve the collaboration between developers and operators. The development team contains programmers, testers, and quality assurance (QA) engineers in agile approaches, while operators includes system administrators (SysAdmins), database administrators (DBAs), and network technicians [@huttermann2012devops-Developers]. It is usually empowered by cloud computing, containerization, automatic testing, continuous integration or continuous delivery [@Jabbari:2016:what-is-devops]. DevOps aims at bridging the gap between developer and operation teams [@huttermann2012devops-Developers]. The goal of DevOps is also defined as accelerating the speed and reducing the effort from development to operation without sacrificing software quality [@erich:2017:devops-practice].

DevOps is not a standalone concept or method, but closely related to other concepts or methodologies in software engineering (SE), especially agile, lean, continuous delivery and continuous deployment [@lwakatare2016:relationship]. They are based on different ideas but can be combined in practice and benefit from each other. Though these concepts have overlaps, similarities and differences, it is important to clarify these concepts to better understand and practice DevOps in both academic and industrial area. Furthermore, different methodologies can be used simultaneously in real world software development activities and benefit each other [@Jabbari:2016:what-is-devops]. 

Agile development method[@beck:2001:agile-Manifesto] has been widely adopted by software industry and is accepted as the mainstream development method by software industry. Recently it is shown to have a close relationship with DevOps and a trend of adoption of DevOps by Agile Team[@lwakatare2016:relationship]. Therefore, it is important to reveal the world wide trends in practice. Furthermore, software development, especially global software engineering, is proved to be significantly affected by cultural factors [@Deshpande:2010], such as individualism versus collectivism, and task- or relationship-oriented [@olsen:2003], so it is also important to find out whether there is any significant regional characteristic in the world.

## Purpose of study {#sec:rq}

The purpose of this study is to investigate the practice of introducing DevOps into Agile development. To be more specific, this study will address the following two research questions:

  + *RQ1: What important aspects are the software development practitioners concerned about in the adoption of DevOps by Agile teams?* The goal of this research question is to achieve a generalised view from industrial and practical perspective, which is expected to provide an in-depth understanding of the practice of DevOps in agile environment, as well as to aid practitioners from industry in the transition from agile to DevOps.
  + *RQ2: Is there any significant difference among different regions or cultures? If yes, what are the differences?* This study will briefly investigate the regional characteristics on the adoption of DevOps by agile teams, which is expected to contribute to the studies of culture factors on software engineering from DevOps and agile perspectives, and to aid the practitioners from global teams in DevOps practice.

## Structure of the report

The rest of this report is organised as follows. In [@sec:liter] the background and related work are described. [@Sec:meth] explains in detail the research method used in this study, and [@sec:result] presents the main findings. Thereafter, [@Sec:discu] discusses and interprets the findings in previous section, followed by the examination of assumptions and limitations in [@sec:ass], and conclusions of the report and outlooks of the possible future works in [@sec:concl].
   

# Literature Review {#sec:liter}

This section provides an overview of studies related to DevOps and agile, reviewing on both their findings and research methods.

## Related Findings

There are a few publications focusing on or including the topic of DevOps and agile. In [@huttermann2012devops-Developers] DevOps is described as a broadened usage of agile. In this book, project development often contains five phases, namely inception, elaboration, construction, transition, and operations. While agile software development process spans from inception to transition, DevOps covers the stages from elaboration to operations, and may include other departments such as finance and human resource (HR). In [@Jabbari:2016:what-is-devops] various aspects of the relationship between agile and DevOps was revealed by systematic mapping study. DevOps can be described as an extension of agile method and can achieve agile goals in software delivery and operation stages. From the overall point of view, agile and DevOps are complementary and DevOps can benefit from agile method, though DevOps cannot satisfy all principles in agile manifesto [@Jabbari:2016:what-is-devops]. This study employs systematic literature review so it does not directly reflect the practical viewpoints, and this study also explicitly listed the consideration of practitioner perspectives as one of future works. Another similar idea that DevOps is an evolution or extension of agile software development is also identified In [@lwakatare2016:relationship], where DevOps is compared to agile, lean and continuous deployment was studied by multivocal literature review. Further more, the authors also claim that DevOps and agile are related with respect to four topics, that is, 1) origin and background, 2) adoption, 3) implementation, and 4) goals and values. It is also described that DevOps and agile software development share some common principles and are motivated by similar goals and values. This study only partly focus on DevOps and agile so the findings are limited. In [@erich:2017:devops-practice] the DevOps usage in practice is studied by qualitative methods, in which the term DevOps is referred by some organisations introducing agile and lean software development methods into the operational activities. 

Some researches pay attention to more realistic problems. [@Elberzhager:2017:agile-to-devops] presents a study focusing on the strategy, organisation, goal, and benefit of introducing DevOps into agile development, by detailed investigating the practical experience at two companies. Another case study is also conducted to explore the mechanism of  collaboration and particular dependency management in large-scale agile DevOps teams [@stray:2019:dm-large]. These two case studies rely on data of specific organisations so does not reflect a wide range of viewpoints from industry. Practical issues about the reason, approach and benefits of introducing DevOps are studied by interview with practitioners from a range of software companies from European and the US that already follow agile processes [@erich:2017:devops-practice]. This study mainly focus on the adoption of DevOps and are lack of the investigations on the relationship between agile and DevOps. From the profession and employment point of view, the Knowledge, Skills and Abilities (KSA) for modern web application development are discovered and how these KSAs support DevOps are investigated [@bang2013ksa] from three real life web projects. In another paper [@hussain2017nz], the Knowledge, Skills and Capabilities (KSCs) required for DevOps is discovered from local job advertisements in New Zealand, as well as the Global Software Engineering (GSE) is revealed. These two studies focus on the perspective of KSA/KSC required for practitioners and do not directly reflect the practice and opinions of engineers in industrial environment. In [@Hemon2019:smart][@hemon:2019:Conceptualizing-smarter] the authors studied the skills including both hard and soft skills, roles, and pattern of collaborations in transition from agile to DevOps. It is identified three levels of automation or maturity in such transition: agile, continuous integration, and continuous delivery.

## Related Methods

In a few papers literature review is conducted as the research method or one of the research methods. In [@Jabbari:2016:what-is-devops] systemic mapping study is conducted among academic publications. Some studies are based on primary data. In [@bang2013ksa], grounded theory, as one of the most popular qualitative research method, is conducted by examining the documentations of three real life web application development projects. Case study is also used as the primary research method in some papers [@erich:2017:devops-practice] [@stray:2019:dm-large]. In [@Hemon2019:smart] [@hemon:2019:Conceptualizing-smarter] an in-depth case study with combination of interviews, observations and documentation is conducted. Data is collected from 12 teams at a large European IT service company which has already adopted agile and DevOps approaches for years, followed by thematic data analysis.

More than one methods can be used for studies on this topic. In [@erich:2017:devops-practice] the authors employ literature review as a starting point, followed by collecting and analysing data from interviews with experienced employees at a variety of organisations of different size, from different country, and participated in different industries. In [@lwakatare2016:relationship] a multi-vocal study is conducted based on both primary and secondary data from three sources: 1) non-scientific articles, for example, blog posts; 2) scientific publications; 3) records of DevOps workshops. Another paper [@hussain2017nz], employs a combination of qualitative and interpretive methods, and a mixed approach of induction and deduction, utilizing three sources of primary data, including: 1) online job advertisement, 2) practitioner interviews and 3) practitioner presentations. 


# Methodology {#sec:meth}

In this study, qualitative approach [@Creswell:2014:mixed] [@Holliday:2002:doing-writing-qual] is followed to investigate the research questions identified in [@sec:rq]. This study is based on primary data collected from discussions and comments people posted at online forums and communities. Then the data is filtered to make sure all records are related to our research questions. Then thematic analysis is conducted following the six-step approach described in [@braun:2006:thematic-psy]. The detailed steps of this research is described as follows.

## Data Collection

### Data Source

Online forums and communities are selected as the data source for this study because with these approach we can collect more data from a diverse set of practitioners from different locations around the world and lower the data acquisition cost. In practice, data are collected from three English websites and one Chinese website:

- Quora[^q]: general Question and Answer (QnA) site
- StackExchange[^se]: QnA community focusing on DevOps and related topics
- Reddit[^r]: general interest-based online community
- Zhihu[^z]: largest Chinese QnA site

[^q]: [quora.com](quora.com)
[^se]: [devops.stackexchange.com](devops.stackexchange.com)
[^r]: [reddit.com](reddit.com)
[^z]: [zhihu.com](zhihu.com)

Most users on Stackexchange and Quora usually have their location specified in profile, and such information are also recorded for regional analysis. Users for data collected from Zhihu are from China. Users on Reddit and some users on Stackexchange and Quora do not have the location information in their profile, so the amount of data for regional analysis are less than the total amount of that.

### Data Searching

All three English sites are searched by keywords "agile" and "DevOps". For Chinese data collection, the search keywords "agile" is translated into Chinese but "DevOps" are used literally because it is used so instead of translated in Chinese software development community.

## Data Analysis

### Data Filtering

The data collected are filtered at two steps to make sure all of them are closely related to our research scope.

At the first step, the search result are initially filtered based on the title (for Reddit) or question (for Stackexchange, Quora, and Zhihu), and the description of it. In the initial filtering, only questions or discussion threads which are clearly related to both agile and DevOps are preserved.

At the second step, each comment (for Reddit) or answer (for Stackexchange, Quora, and Zhihu) is examined manually, and only genuine contents are preserved. Any post that is too short, not reflecting any idea or experience in agile or DevOps, or obviously for advertising or business purpose is removed from the data set.

### Thematic analysis

Data was analysed following the widely used six-step thematic analysis [@braun:2006:thematic-psy] [@Maguire:2017]. Though themes are expected to emerge from codes, the coding schemes used in [@bang2013ksa], [@Jabbari:2016:what-is-devops] and [@hussain2017nz] are good starting points. The six steps followed by this report are detailed as follows. Though it is presented as an ordered list, it is important to notice that this analysis is a recursive rather than linear approach which requires moving back and forth [@braun:2006:thematic-psy]. 

1. Become familiar with the data

    It is crucial to be familiar with the data before beginning any analysis. Though the data was collected and filtered by the author so some prior knowledge of the data has already been acquired, it is still strongly recommended to re-read the data, search for meanings, and take notes [@braun:2006:thematic-psy].

2. Generate initial codes

    In this step, meaningful texts were highlighted and assigned by initial codes. Open coding is used, which means codes are not pre-set [@Maguire:2017]. However, coding schemes created by existing works are referred. For example, in [@bang2013ksa] the codes are categorised into four perspectives revealed by [@Humble:2011]: 1) collaboration, 2) automation, 3) measurement, and 4) sharing. Results in [@hussain2017nz] are categorised into the following themes: 1) knowledge area, 2) DevOps technologies, 3) language and frameworks, 4) capabilities, and 5) job titles and roles. In [@lwakatare2016:relationship] the relationship between agile and DevOps are categorised into four main topics: 1) origin and background, 2) adoption, 3) implementation, and 4) goals.

    The codes generated in this step is quite primitive and not precise. They requires further refinement and modification.

3. Search for themes

    A theme is defined as a pattern "that captures something significant or interesting about the data and/or research question" [@Maguire:2017]. To identify themes, the codes generated in previous step are organised into topics to form initial themes. Codes with similar meanings or discussing on the same topic are placed under the same category for further investigation. Though the coding is preliminary and some are ambiguous, the theme starts to emerge. For example, a large amount of attention are paid to collaboration, as well as team responsibility. 

4. Review themes

    During this stage, preliminary themes identified in previous step are reviewed, improved and modified. Each theme is carefully examined whether it is meaningful and has sufficient significance.
    All the data under the theme are reviewed and check whether the coding is appropriate and supports the theme. Themes with overlaps are clarified and separated, or merged if they are actually the same thing.

5. Define themes

    During this phase, themes are further refined and finalised by identifying the essence of each theme. Each theme is conceptualised with its meaning well described. Differences and relations between themes are also clarified. In this step, it is usually to find inappropriate or incorrect codings when trying to make meanings of theme, so requires back to previous steps and searching for themes iteratively.

6. Write-up

    The final step of the analysis is writing this research report.

# Result {#sec:result}

## Data overview

The data from online forums and QnA websites are originally organised into discussion threads or questions as topics. The replies, comments or answers posted by different users are referred as posts. In this study 139 posts form 17 topics are analysed. Number of records from each website are listed in [@Tbl:data-overview].

Table: data overview {#tbl:data-overview}

  | data source              | Number |
  |--------------------------|-------:|
  | Quora                | 73      |
  | Reddit | 44      |
  | StackExchange | 17      |
  | Zhihu | 5      |

## Main Findings

### Global Trends {#sec:trends}

The analysis shows that practical issues and practitioners' concerns on agile and DevOps can be categorised into the following topics: 

1. collaboration and sharing
2. organisation, functionality and responsibility
3. motivation, goal and value
4. concept and principles
5. process and methodology
6. knowledge and skills
7. technical tools

#### Collaboration and Sharing

The most significant finding is that DevOps is interpreted as a culture of collaboration rather than a job title or technical tools. They claim that DevOps is driven by the lack of collaboration between developer and operator teams, and is targeted at bridging such gap. Some people even define DevOps as collaboration. They argue that tools are useless if the principles and culture are not understood and followed by team members. Some practitioners clearly put it, 

> "DevOps is not about tools and automation but building culture that allow faster feedback. This is not possible without having system thinking and collaboration between dev and ops." [^culture-ff]

> "DevOps equals COLLABORATION. It's not the toolchain!"  [^equals]

[^culture-ff]: From: <https://www.quora.com/How-are-DevOps-and-Agile-different/answers/47169430>, retrieved September 21, 2019
[^equals]: From: <https://www.reddit.com/r/devops/comments/94bc47/how_does_your_devops_members_interact_with/e3knbd1>, retrieved September 21, 2019

Though sharing is less mentioned, it is believed by some people as an important factor of collaboration. It is a culture of collaboration by sharing knowledge, experience, and tools to prevent duplicated and unnecessary works. Developers should write tools to help operators doing operation tasks and vice versa. As one practitioner pointed out, 

> "All of these opportunities for collaboration keep engineers from re-inventing the wheel. It's a cultural of sharing knowledge and ideas much like the Open Source community." [^wheel]

[^wheel]: From: <https://www.reddit.com/r/devops/comments/94bc47/how_does_your_devops_members_interact_with/e3oo6h2>, retrieved September 21, 2019

#### Organisation, Functionality and Responsibility

The topic of organisation also attracts many attentions at online forums. Typical contents in this topic are: 1) team organisation, 2) team functionality, 3) role and responsibility of team members.

There are two controversial opinions on how team should be organised. Most people claim that developers and operators teams should be unified into one agile team, in which the role and responsibilities of every team member are the same. In other words, every team member is responsible for the whole software development lifecycle from requirement analysis to deployment, so they will take responsibility on their own work instead of throwing it to other teams. Typical sayings are as follows:

> "According to the DevOps culture, end to end responsibility of the application has taken by a single group of engineers. Right from the phase of requirements to testing to monitoring to feedback to implementing changes, all done by same group of engineers." [^e2e]

> "You don't have agile engineers or agile teams, because if you're implementing them properly, everyone is agile. Same thing applies to DevOps." [^everyone]

[^e2e]: From: <https://www.quora.com/How-are-DevOps-and-Agile-different/answer/James-Lee-1583>, retrieved September 21, 2019
[^everyone]: From: <https://www.reddit.com/r/devops/comments/94bc47/how_does_your_devops_members_interact_with/e3kuk8v?utm_source=share&utm_medium=web2x>, retrieved September 21, 2019

Though this is the opinion of majority, there are still some people claiming that the developers and operation team should not be merged. The two teams should both follow agile approach but keep separated. They argue that developers would spend most of the time on development and only a little time on operation works. Therefore, a separated operation team is the solution to this time allocation problem.

#### Motivation, Goal and Value

DevOps is motivated by the gap between development team and operation team, and consequently aims at bridging such gap. The goal of DevOps is to provide fast, easy, repeatable, reliable, safe and secure deployment. DevOps automates repetitive work and brings maintainability in operation phase. As a practitioner pointed out:

> "DevOps goal is to build a common culture across teams so that we can deliver fast, high quality, fast feedback, and continuous improvement." [^goal]

[^goal]: From: <https://www.quora.com/How-are-DevOps-and-Agile-different/answer/Murughan-Palaniachari>, retrieved September 21, 2019

In a more basic level, the goal and value of DevOps and agile are consistent. They both aim at building a solid loop for fast feedback from customers, thus more "agile" reacting and adapting to changes. This benefits will ultimately result in the improvement of product quality.

#### Concept and Principles

People hold two kinds of opinions on agile-DevOps relationship at the level of basic concepts and principles. These opinions are similar with subtle differences. Some people hold the idea that DevOps is an extension of agile, which is consistent with some academic publications [@huttermann2012devops-Developers] [@Jabbari:2016:what-is-devops] [@lwakatare2016:relationship]. People holding this idea take DevOps as managing end-to-end software develop process, including both development and operation. On the other hand, some other people claim that DevOps and agile are complimentary. They incline DevOps on the "Ops" part because they think most developer teams have already established agile culture but operators do not. Such people relate DevOps particularly on the deployment and operation phases, and take DevOps as applying agile methods and principles in such phases. As explained in comment from a practitioner:

> "When companies applied Agile to team, things were good but not great as it was not applied across all the teams. Operation team were still following waterfall or some traditional way. ... So to achieve greater success we adopt DevOps where both development team and operation team follows agile. By this both Dev and Ops team follows same culture." [^op-waterfall]

[^op-waterfall]: From: <https://www.quora.com/How-are-DevOps-and-Agile-different/answer/Murughan-Palaniachari>, retrieved September 21, 2019

There are some attempts of introducing agile methods such as Scrum or Kanban into IT operations. For example, there is some practice of managing infrastructure change by stories in sprint, along with application change.

#### Process and Methodology

While agile method breaks the development process into small and manageable pieces, such as sprints in Scrum, the most significant characteristic of DevOps process is automation. Every main respect in operation is automated, such as testing, delivery, deployment, monitoring, and so on. With automated pipelines engineers can deliver software as frequent as many times per day, so they can verify how their changes work in the real world more promptly.

Monitoring and measurement is another important part in DevOps methodology. However they are rarely considered in agile approach, and this is believed by some people to be the source of many problems in agile development.

#### Knowledge and Skills

Unlike in [@hussain2017nz] that knowledge areas especially cloud infrastructure, AWS, or Azure are much more appreciated by the employers on job market, practitioners at the online forums care much less on the knowledge and skills of DevOps, especially the hard skills. People pay much more attention on collaboration, responsibility, and fast feedback than concrete knowledge and skills.

#### Technical Tools

In contrast with agile, DevOps are more strongly backed by technical tools such as Jenkins, Docker, Puppet, and Ansible. These are important means but less important than culture and collaboration. Tools are considered as manners to implement DevOps, but not placed at the essence or core values.

### Regional Variations

#### Overview of regional data

In total, there are 73 posts which the author clearly stated their locations. Most posts are from North America including the US and Canada. The second largest data source is India. The third one is Europe including the UK, Finland, Lithuania, Poland, Hungary, Ukraine, and Belarus. The fourth and fifth ones are China and Australia. The other posts are from Israel, Southeast Asia (Malaysia and Vietnam), and Latin America (Mexico and Brazil). The regional data is summarised as shown in [@Tbl:regional].

Table: regional overview {#tbl:regional}

  | Region           | Number  | Percentage |
  |------------------|--------:|-----------:|
  | North America    | 29      |      39.7% |
  | India            | 16      |      21.9% |
  | Europe           | 13      |      17.8% |
  | China            | 5       |      6.8%  |
  | Australia        | 4       |      5.5%  |
  | Other            | 6       |      8.2%  |

#### Regional findings

From the analysis it is clear that the movement of agile to DevOps is global wide and practitioners all over the world pay attention to or has already been practicing it.

Some primitive tendencies can be seen from the data, for example, while practitioners in North America and Europe discuss DevOps and Agile on a variety range of topics, in India they particularly care about collaboration and organisation, and in China they tend to value more on process and automation.

However, it it hard to tell the significance of these tendencies from the data. People from different parts of the world all care about all seven aspects described in [@sec:trends], and not enough data was collected for some regions so statistical significance cannot be drawn from such data. Furthermore, it is necessary to introduce quantitative or mixed method into the study if want to obtain statistical significance. 


# Discussion {#sec:discu}

This study is from the viewpoint of practitioners from industry, and it would be beneficial to compare the findings to existing results from other perspectives. 

## Collaboration

The primary concern on the adoption of DevOps in agile is collaboration, which is consistent with the first value of Agile's Manifesto [@beck:2001:agile-Manifesto]: "Individuals and interactions over processes and tools". From this respective, DevOps can be considered as an agile method. A team or organisation following agile principles would value and rely on individuals rather than process or rules, and that also applies to DevOps. As a valuable principle for practitioners, in the adoption of DevOps, it is essential to build a culture and mechanism for effective collaboration between individuals and teams.

## Organisation

Most practitioners think it is a correct way of implementing DevOps to build a team in which every one has the same responsibility for end to end process. This is an extension of agile approach to the operation stage. However, there are reasonable argument that developers should not take operation jobs because they would spent most of their time on application development rather than infrastructure change. As some practitioner argues,

> (My team) "do a mixture of SRE, tool development, platform architecture and process automation. Most of our platform & toolchain work is open for anyone to contribute to but most developers simply don't care, they just want to write product code, which is why my division and team exists." [^dev-dont-care]

[^dev-dont-care]: From: <https://www.reddit.com/r/devops/comments/94bc47/how_does_your_devops_members_interact_with/e3ktxi7>, retrieved September 21, 2019

However, some people think this kind of idea is "totally backwards". Though this is a potential problem in adoption of DevOps, it should be solved by improving the culture and methodologies instead of simply slicing developers and operators into two separated teams.

## Absence of Cloud Computing

Though cloud and network infrastructure is the most important knowledge area for DevOps jobs valued by employers [@hussain2017nz], and cloud computing is considered as an enabler of DevOps [@Jabbari:2016:what-is-devops], it is much less concerned by practitioners. This may implies that the principles and methodologies of DevOps are not necessarily applied in cloud computing environment. Therefore, it is reasonable to think that any approach can be categorised as a DevOps approach if it increases collaboration between development and operation teams, provides quicker, easier and reliable deployment, and enables fast feedback from customer.

## Regional Difference and Culture

Though significant findings are not clearly drawn in this study, some further discussions is useful. Software development is an activity affected by culture especially at global scale among teams across different cultures [@olsen:2003]. DevOps or agile, with collaboration as its most important value, will naturally affected by cultural factors. For example, agile method values individuals over process, which is a conflict to some countries with a collectivism culture such as China. On the other hand, emphasizing on cohesiveness could be beneficial for removing friction from collaboration.

# Assumptions and Limitations {#sec:ass}

In this study the main assumption is that posts at online forums or QnA websites are a valid representation and reflection of the movement from agile to DevOps in real world industry. It is acknowledged that some posts are lack of valuable ideas or real experience on the account that the author may compose the content from some others without deep thinking. 

The data is collected from four websites, the users of which are not evenly distributed among different locations, and most of the data is in English. However, considering that English is the dominate language in software development area and most knowledge in this area are written in English, it is reasonable to believe that such data could uncover some patterns in the transition from agile to DevOps at global scale.  

In terms of the analysis on regional differences, the location information is acquired from the profiles of authors and it is assumed that the data with available location information is a valid sampling. However, with this approach the size of data with valid locations is less than a half of the overall amount.


# Conclusions and Future Works {#sec:concl}

To conclude, the report of this study provides a snapshot of global trends and practical issues to gain in-depth overview and understanding in the movement of transiting from agile to DevOps. In this study, such movement is investigated from both global and regional views as two research questions. To this aim, a qualitative research is designed and conducted. Data is collected from four online forums or QnA websites by searching for topics related to both agile and DevOps. According to the data at hand, the main findings are at the former facet. This study reveals that the most important topics concerned by practitioners are collaboration, organisation and responsibility. Though there are some diverse in different opinions, it is commonly believed that collaboration is the core of DevOps. In addition, people pay much more attention to collaboration, organisation, responsibility, and fast feedback over process, tools and technologies. In terms of the regional difference, though the data source is proved to be global wide, only some tendencies can be conjectured without solid evidence due to insufficient data and statistical analysis.

There are some future research directions worthwhile. First, the result would be more reliable if more data with higher diversity can be collected. For example, data can be collected from other online resources. More reliable and higher quality data can be acquired from interviews. Regional data can be collected from local groups such as Meetup [^meetup]. Second, study on the teams or projects at large company can provide more in-depth insight on this problem at large scale from more realistic and practical point of view. This can be done by interviews with employees of different roles from large companies. Third, as software development is an activity influenced by culture, it would be valuable to understand this topic from culture viewpoints, and improve the performance of introducing DevOps into agile development under different culture background.

[^meetup]: [meetup.com](meetup.com)

\pagebreak