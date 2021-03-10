# ANUGA Community TechLauncher Project

## Table of Contents

1. [Overview](#overview)
2. [Team](#team)
3. [Stakeholders](#stakeholders)
4. [Documentation](#documentation)
5. [Timeline](#timeline)
6. [Risks](#risks)
7. [Tools and Client Requirements](#tools-and-client-requirements)
8. [Technical Constraints](#technical-constraints)

## Overview

The existing ANUGA Hydro software has been used to model floods for more than a decade, with excellent results. But for smaller floods, it has a tendency to over estimate the flood area, due to being unable to model underground drainage systems.

This project will extend the ANUGA Hydro software, which is capable of hydrodynamic modelling, by coupling with the US EPA's Storm Water Management Model (SWMM), thus adding to it the ability to model the effects of underground drainage systems. 

## Team

|  Name          | UID    | Principal Role | Secondary Role |
|:--------------:|:------:|:---------------|:---------------|
| **Zheyuan Zhang** | u6870923 | ANUGA developer<br> ANUGA Viewer supporter| Documentation (grammar) reviewer<br>Code reviewer (ANUGA & SWMM) |
| **Xingnan Pan** | u6744662 | ANUGA developer<br>client manager | Test developer<br>Code reviewer (ANUGA & SWMM)<br>Minutes taker |
| **Chen Huang** | u6735118 | SWMM developer<br>Spokesperson | Code reviewer (ANUGA)<br>Landing page maintainer<br>Minutes taker |
| **Lixin Hou** | u6456457 | ANUGA developer<br> ANUGA tester<br>Deputy spokesperson <br>Client Manager |Document author<br>Minutes taker| 
| **Mingda Zheng** | u6686733 | SWMM developer<br>Quality manager | Code reviewer (SWMM&ANUGA)<br>Test developer|
| **Yijie Liu** | u6890141 | ANUGA developer<br>Quality manager | Test developer<br>Documentation author |
| **Zijun Zhang** | u6904534 | SWMM developer<br>Documentation author | Code reviewer (ANUGA) |
| Zhixian Wu (Past member, graduated) | u5807060|||
## Stakeholders
* **The sponsors:**
   * Professor Stephen Roberts, ANU
   * Dr Ole Nielsen, Geoscience Australia
* **The user representatives (flood modellers):**
   * Rudy Van Drie, Balance Research and Development
   * Dr Petar Milevski, Civil Engineer Urban Drainage, Wollongong City Council

## Documentation

### Google Docs Folder

> [All Materials](https://drive.google.com/drive/folders/16Z4aiFDwxBb5qRQU78bVDZmsvFZOTPmk?usp=sharing)

### Statement of Work

> [SoW_2020_S2](https://drive.google.com/file/d/1Hb2j2KeJzwX2FM4dNMCTmS8V8kXxqOQD/view?usp=sharing)

> [SoW_2021_S1](https://drive.google.com/file/d/1d2Pmq4ShnWwFyCtPxR9tJLyTk23iW4mc/view?usp=sharing)

### Sprint Stories

> [Trello](https://trello.com/b/Z45C7crP/agile-sprint-board)

### Communication

> [Slack](https://anu-flood-modelling.slack.com)

> Email

> Zoom

### Meeting Minutes
<details>
  <summary>2020 meeting minutes</summary>

Sprint 1 (start of semester - 19/08/2020)

> [2020-08-04 Team Meeting](https://docs.google.com/document/d/1SW3PUsRs-9bc1CYlVkW6fHQLiOQ0cm0w_jzSKu37Gpw/edit?usp=sharing)

> [2020-08-06 Client Meeting](https://docs.google.com/document/d/1J_kqxAhOHSAh3xWV8enVu0XkZSba1jQchf01azwkgvg/edit?usp=sharing)

> [2020-08-06 Team Meeting](https://docs.google.com/document/d/1TSrCJVN6h5WFBfUl96gyvOTVphKCoR4-Ap0t-zANyf0/edit?usp=sharing)

> [2020-08-11 Team Meeting](https://docs.google.com/document/d/1Y9Rpm179KeMyxmN4nzFfLMplG6DxY44MxcMesnc1g28/edit?usp=sharing)

> [2020-08-12 Client Meeting](https://docs.google.com/document/d/1xuQi6PqbxpRX6mbUkZXvexbnCZzglCLeXB2ugw3vM3I/edit?usp=sharing)

> [2020-08-12 Team Meeting](https://docs.google.com/document/d/1DDAFtIT_7RpGpm0CvSyJl2uucRn036oh8wrYwniZzAA/edit?usp=sharing)

Sprint 2 (19/08/2020 - 02/09/2020)

> [2020-08-19 Client Meeting (sprint end / start)](https://docs.google.com/document/d/1pkxORBpc-0SfU_oyCqxczmxs7KlaVyPZL7RJfRDCR48/edit?usp=sharing)

> [2020-08-19 Team Meeting (sprint review / sprint start)](https://docs.google.com/document/d/1ZnBXNOj-Jqx6SO_uYdZPlars6H0JniCilBfcoA9xI2M/edit?usp=sharing)

> [2020-08-26 Client Meeting](https://docs.google.com/document/d/1A9OFPDastLef0VJmBKX0fM5QJeeLZsB5PRbd-QajyNI/edit?usp=sharing)

> [2020-08-26 Team Meeting](https://docs.google.com/document/d/1DlJlfKMPyyqoO_YJeZl6Aey1x4eywT6jdjrGmDLA3MM/edit?usp=sharing)

Sprint 3 (02/09/2020 - 16/09/2020)

> [2020-09-02 Team Meeting (sprint review / start)](https://docs.google.com/document/d/1ZnBXNOj-Jqx6SO_uYdZPlars6H0JniCilBfcoA9xI2M/edit?usp=sharing)

> [2020-09-09 Client Meeting](https://docs.google.com/document/d/1DfLF25yYnrMsEEs7hfgxwOJLJauWV1SG8EkrmsuiGJI/edit?usp=sharing)

> [2020-09-09 Team Meeting](https://docs.google.com/document/d/1zlJZFkdhDrTZV2k31DUxPXyjwjmosxrcUnzit6wgIgU/edit?usp=sharing)

> [2020-09-16 Client Meeting (sprint end / start)](https://docs.google.com/document/d/1RnVdcKazuPcUvlOWpppkFktT4iBV74ietcgBF9oYuRU/edit?usp=sharing)

Sprint 4 (16/09/2020 - 30/09/2020)

> [2020-09-16 Client Meeting (sprint review / start)](https://docs.google.com/document/d/1noYPr9gOLzWIK26JZeXJfn5a9hDOlRFKqAXDuNBH9_I/edit?usp=sharing)

> [2020-09-23 Client Meeting](https://docs.google.com/document/d/1HS-tL2l-eucJe-CigrFuaxHfc5SK3qZPL8ZVrjUhhps/edit?usp=sharing)

> [2020-09-23 Team Meeting](https://docs.google.com/document/d/1Mup1fkuuTh_Seiyl5hatD0x7yu8xm2BrIRYfc8OXqYo/edit?usp=sharing)

> [2020-09-30 Client Meeting (sprint end / start)](https://docs.google.com/document/d/1nKjNaIwO5UaDU5hRM0d8p8jzIV_UcxFmQvWS6TxX89o/edit?usp=sharing)

Sprint 5 (30/09/2020 - 14/10/2020)

> [2020-09-30 Client Meeting (sprint review / start)](https://docs.google.com/document/d/1zZ1CAanbMxjSQRJ3EzLSul8ew3cga8fRaFBevxe1tY4/edit?usp=sharing)

> [2020-10-07 Client Meeting](https://docs.google.com/document/d/1J4boyEtVzbsoLnc0TiBc0nuD1A3BfXMOohLfNNjnyzM/edit?usp=sharing)

> [2020-10-07 Team Meeting](https://docs.google.com/document/d/11V6t5q_Nd5PYIO7EqqC1iCGF4E8ZV1WNAomvZi08ocE/edit?usp=sharing)

> [2020-10-14 Client Meeting (sprint end)](https://docs.google.com/document/d/1Z3TEZisl3SOwWadyyjJx8ul4Fm9F5VySaPPQTACzcMg/edit?usp=sharing)
</details>

<details>
  <summary>2021 meeting minutes</summary>

Sprint 1 (start of semester - 10/03/2021)

> [2021-02-24 Client Meeting](https://docs.google.com/document/d/1tlAb2cCmxQuTGya8f3YNSQieG8ebsSQfv_pd375Gjx0/edit?usp=sharing)

> [2021-02-25 Team Meeting](https://docs.google.com/document/d/1CbNG8xcdKbR5MTqaRrjgpwpSMjHulHrIOBFyywPpWQc/edit?usp=sharing)

> [2021-03-03 Client Meeting](https://docs.google.com/document/d/140zjvChWzgg-UkGh2leowSyUIkO-NT8p289_fg2Viag/edit?usp=sharing) 

> [2021-03-04 Team Meeting](https://docs.google.com/document/d/1m4uDIB91wyEdHaYlwV-_yp1zULucCR1GoFj8F4SHr4s/edit?usp=sharing)

</details>

### Development Artefacts

<details>
  <summary>2020 artefacts</summary>

> [Sprint 1](https://drive.google.com/drive/folders/1vmBj6LaNh856jAEzvsyGWSGuSnovIyRs?usp=sharing)

> [Sprint 2](https://drive.google.com/drive/folders/1F4Q5Iqexq1BnQAzWQfQ3h0j9jsK95sl5?usp=sharing)

> [Sprint 3](https://drive.google.com/drive/folders/16FuZxkii7Zbye6nQ--5SRjwLIQtY2AeA?usp=sharing)

> [Sprint 4](https://drive.google.com/drive/folders/1n2aCdY96LGSJd7TsodW_KLTlw4zo7RU-?usp=sharing)

> [Sprint 5](https://drive.google.com/drive/folders/1U98A_bse0_Ww5gdgPW2vMbLV4Y6KDDa9?usp=sharing)
</details>

<details>
  <summary>2021 artefacts</summary>
</details>

### Reflection

<details>
  <summary>2020 reflection</summary>

> [Sprint 1 Reflection (a.k.a. reflection on audit 1 feedback)](https://docs.google.com/document/d/16xBJXXnX3MSNlGU8p7AD8YrlXbIl53kUddITZu9re3k/edit?usp=sharing)

> [Sprint 2 Reflection (a.k.a. reflection on audit 2 feedback)](https://docs.google.com/document/d/158qZOpPC_K8xF1pFweSavP5oiXoaP0sn9ZlicJNDWio/edit?usp=sharing)
</details>

<details>
  <summary>2021 reflection</summary>
</details>

### Client-Provided Resources

> [All Materials](https://drive.google.com/drive/folders/1j-Ex4TJj_q8MZ6cUNJItfzBr-FuQCQ7A?usp=sharing)

> [Ideas shared on Slack](https://docs.google.com/document/d/1uRRW0dEOZgfzpxXeJTrC4DeBQovkaaz06gjDWiu8CeQ/edit?usp=sharing)

### Decisions

> [Log for Small Decisions](https://docs.google.com/spreadsheets/d/1uPZlRMNaRBlZnUdfNPVQ4e_S48npiRRkqP9GHJUyXS4/edit?usp=sharing)

> [Template for Large Decisions](https://docs.google.com/document/d/11qM3a2_Abr2oGtYLgIPA4QjgSELj9RFD4IboVFuBqEg/edit?usp=sharing)

> [2020-08-05 Continuous Integration Tool Selection](https://docs.google.com/document/d/1xt46NBabq5xelkVywf4NLt9Su33GicAFldKurt747fs/edit?usp=sharing)

> [2020-09-14 Decision on how to modify SWMM](https://docs.google.com/document/d/1oXyEDcNLuEXH-2n9xcsxBRuCfLxSPdgJ_H7j2IfxP_E/edit?usp=sharing)

## Timeline

We are doing two-week sprints, with client meetings to close each sprint on Wednesday 5:00PM Canberra time, and team meetings for sprint retrospectives and sprint planning on Wednesday 7:00PM Canberra time.

The first sprint will be a bit longer, so that the rest of the sprints will end just before the Week 6 and Week 10 audits. This means the first sprint will end Wednesday of Week 4.

* **2020-s2-timeline**
<img src="https://github.com/rachelwu21/anuga_core/blob/master/20-s2%20timeline.jpg" alt="20-s2-TL" align=center />

* **2021-s1-timeline**
<img src="https://github.com/Chen-Huang-326/anuga_core/blob/master/21-s1%20timeline.png?raw=true" alt="21-s1-TL" align=center />

## Risks

|Risk ID|Risk points|Mitigation measures|
|:-----:|:---------:|:-----------------:|
|1|The new member may take a long time to learn the complex model and tools needs.|He would be given one to two weeks to get familiar with our project. Also, Other members would give him instructions and advise about the project. In addition, the clients are the original developers of the software and the team can ask them questions.|
|2|Team members may have some emergencies during the project, such as sick, exam which may interrupt the project progress.|We will never have any task that is only performed by one team member. Either the task will be performed by a small group, or if it is too small one team member will be assigned as the secondary person responsible for reviewing the code and taking over if the member principally responsible has an emergency situation|
|3|The time difference might be a cooperation barrier as the team consists of overseas and native members.|Most members are living in China, which merely has 2-3 hours lag with the Australian Eastern Standard Time. Therefore, the team or client meeting can be set at afternoon to mitigate the impact.|
|4|The system and equipment requirements may cause some difficulties to the team, as the project is required to design in Ubuntu 20.04, but some features can only run in Ubuntu 18.04.|Members can use virtual machine or install dual systems to have mathcing development environments. And some complex issues can be tested in lab machines by members in Canberra.|

## Tools and Client Requirements

* The project should be developed in Github
   * Each member is able to test in a branch
   * Using pull request to get the task review from others
   * Only tested and review code should be merged into the `main` branch
* The project is mainly developed on Ubuntu 20.04
   * This means that team members will need to install a virtual machine or dual boot. All members have already done so.
* Setup Continuous Integration (CI) tools to test on three platforms (Windows, MacOS and Ubuntu) automatically.
   * This was a Sprint 1 task for two members of the team. They have already set up Appveyor and TravisCI to handle this.
* Software standards
   * The Python code should follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) standard apart from agreed exceptions.
   * All code, apart from the most trivial, should have corresponding unit tests.
   * Model behaviour should be tested end to end with real data.
   * Tests should be integrated with a CI server.
* The standard official version of SWMM from the US EPA website is only available for Windows, so we will use another open-source project called PySWMM by Open Water Analytics.

## Technical Constraints

The end modelling software must be a coupling between ANUGA and SWMM. There are no other open-source options for this type of software. And even if there were, the team was commissioned by the clients to improve the existing ANUGA Hydro software in a specific way. 

## Build Status
[![Build Status](https://travis-ci.com/20-S2-2-C-Flood-Modelling/anuga_core.svg?branch=master)](https://travis-ci.com/20-S2-2-C-Flood-Modelling/anuga_core)

