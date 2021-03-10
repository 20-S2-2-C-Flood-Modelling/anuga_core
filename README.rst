.. image:: https://travis-ci.org/GeoscienceAustralia/anuga_core.svg?branch=master
    :target: https://travis-ci.org/GeoscienceAustralia/anuga_core
    :alt: travis ci status

.. image:: https://ci.appveyor.com/api/projects/status/ws836mwk6j5brrye/branch/master?svg=true
    :target: https://ci.appveyor.com/project/stoiver/anuga-core/branch/master
    :alt: appveyor status


.. image:: https://img.shields.io/pypi/v/anuga.svg
    :target: https://pypi.python.org/pypi/anuga/
    :alt: Latest Version


======================================
ANUGA Community TechLauncher Project
======================================



.. contents::

Overview
--------------
------------------

The existing ANUGA Hydro software has been used to model floods for more than a decade, with excellent results. But for smaller floods, it has a tendency to over estimate the flood area, due to being unable to model underground drainage systems.

This project will extend the ANUGA Hydro software, which is capable of hydrodynamic modelling, by coupling with the US EPA's Storm Water Management Model (SWMM), thus adding to it the ability to model the effects of underground drainage systems.

Team
------
------------

Stakeholders
--------------
-------------------

- **The sponsors:**
    - Professor Stephen Roberts, ANU
    - Dr Ole Nielsen, Geoscience Australia
- **The user representatives (flood modellers):**
    - Rudy Van Drie, Balance Research and Development
    - Dr Petar Milevski, Civil Engineer Urban Drainage, Wollongong City Council


Documentation
----------------
--------------------

Google Docs Folder
^^^^^^^^^^^^^^^^^^^^

    `All Materials <https://drive.google.com/drive/folders/16Z4aiFDwxBb5qRQU78bVDZmsvFZOTPmk?usp=sharing>`_

Statement of Work
^^^^^^^^^^^^^^^^^^^

    `SoW_2020_S2 <https://drive.google.com/file/d/1Hb2j2KeJzwX2FM4dNMCTmS8V8kXxqOQD/view?usp=sharing>`_

    `SoW_2021_S1 <https://drive.google.com/file/d/1d2Pmq4ShnWwFyCtPxR9tJLyTk23iW4mc/view?usp=sharing>`_

Sprint Stories
^^^^^^^^^^^^^^^

    `Trello <https://trello.com/b/Z45C7crP/agile-sprint-board>`_

Communication
^^^^^^^^^^^^^^^

    `Slack <https://anu-flood-modelling.slack.com>`_

    Email
    
    Zoom

Meeting Minutes
^^^^^^^^^^^^^^^^^


Development Artefacts
^^^^^^^^^^^^^^^^^^^^^^^


Reflection
^^^^^^^^^^^^


Client-Provided Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    `All Materials <https://drive.google.com/drive/folders/1j-Ex4TJj_q8MZ6cUNJItfzBr-FuQCQ7A?usp=sharing>`_
    
    `Ideas shared on Slack <https://docs.google.com/document/d/1uRRW0dEOZgfzpxXeJTrC4DeBQovkaaz06gjDWiu8CeQ/edit?usp=sharing>`_

Decisions
^^^^^^^^^^^

    `Log for Small Decisions <https://docs.google.com/spreadsheets/d/1uPZlRMNaRBlZnUdfNPVQ4e_S48npiRRkqP9GHJUyXS4/edit?usp=sharing>`_
    
    `Template for Large Decisions <https://docs.google.com/document/d/11qM3a2_Abr2oGtYLgIPA4QjgSELj9RFD4IboVFuBqEg/edit?usp=sharing>`_
    
    `2020-08-05 Continuous Integration Tool Selection <https://docs.google.com/document/d/1xt46NBabq5xelkVywf4NLt9Su33GicAFldKurt747fs/edit?usp=sharing>`_
    
    `2020-09-14 Decision on how to modify SWMM <https://docs.google.com/document/d/1oXyEDcNLuEXH-2n9xcsxBRuCfLxSPdgJ_H7j2IfxP_E/edit?usp=sharing>`_


Timeline
-----------
----------------

We are doing two-week sprints, with client meetings to close each sprint on Wednesday 5:00PM Canberra time, and team meetings for sprint retrospectives and sprint planning on Wednesday 7:00PM Canberra time.

The first sprint will be a bit longer, so that the rest of the sprints will end just before the Week 6 and Week 10 audits. This means the first sprint will end Wednesday of Week 4.

- **2020-s2-timeline**

- **2021-s1-timeline**


Risks
--------
--------------



Tools and Client Requirements
--------------------------------
------------------------------------

- **The project should be developed in Github**
    - Each member is able to test in a branch
    - Using pull request to get the task review from others    
    - Only tested and review code should be merged into the main branch

- **The project is mainly developed on Ubuntu 20.04**
    - This means that team members will need to install a virtual machine or dual boot. All members have already done so.

- **Setup Continuous Integration (CI) tools to test on three platforms (Windows, MacOS and Ubuntu) automatically.**
    - This was a Sprint 1 task for two members of the team. They have already set up Appveyor and TravisCI to handle this.

- **Software standards**
    - The Python code should follow the `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ standard apart from agreed exceptions.  
    - All code, apart from the most trivial, should have corresponding unit tests.    
    - Model behaviour should be tested end to end with real data.    
    - Tests should be integrated with a CI server.

- **The standard official version of SWMM from the US EPA website is only available for Windows, so we will use another open-source project called PySWMM by Open Water Analytics.**


Technical Constraints
-----------------------
---------------------------

The end modelling software must be a coupling between ANUGA and SWMM. There are no other open-source options for this type of software. And even if there were, the team was commissioned by the clients to improve the existing ANUGA Hydro software in a specific way.


