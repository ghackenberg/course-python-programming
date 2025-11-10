# System Instructions

## Context

- I am a *Professor of Industrial Informatics* at the *School of Engineering* of the *University of Applied Sciences Upper Austria* at *Campus Wels*.
- I teach in the Bachelor's degree program "Innovation, Product & Engineering Management", in which students are trained to become product managers.
- This repository contains my materials for the course *Programming with Python*, in which students learn the basics of programming.

## Learning Objectives

- Read and understand source code.
- Write simple source code themselves.
- Error analysis and debugging using a debugger.
- Document the structure and functionality of source code.

## Course Organization

- 10 in-person sessions
- Duration of in-person sessions is 2.5 hours
- Own set of slides for each in-person session
- About 40 slides for each session
- Homework after each in-person session
- Exam at the beginning of each subsequent in-person session
- The type of exam is a multiple-choice test
- The duration of the exam is 20 minutes
- No aids are allowed for the exam

## Presentation Technology

For the presentation slides (or the lecture script), I use the Markdown Presentation Ecosystem (MARP) with a custom theme for the University of Applied Sciences Upper Austria.

The basic structure of the MARP files for the presentation slides includes chapter and section headings as well as content slides as shown in the following example.

```md
---
marp: true
theme: fhooe
header: Chapter Title
footer: Dr. Georg Hackenberg, Professor for Computer Science and Industrial Systems
paginate: true
math: mathjax
---

<!-- Placeholder for chapter image description -->

![bg right](./ChapterImagePath)

# Chapter N: Chapter Title

This chapter includes the following sections:

- N.1: Section Title 1
- N.2: Section Title 2
- ...

---

<!-- Placeholder for section image description -->

![bg right](./SectionImagePath)

## N.M: Section Title

This section includes the following content:

- Content 1
- Content 2
- ...

---

### Content Slide Title

Content slide text
...
```

The custom theme supports the creation of multi-column slide layouts using a parent `<div class="columns">` and two or more nested `<div class="relative weight">`.

```md
<div class="columns">
<div class="one|two|three|four|five|six">

Content of the first column

</div>
<div class="one|two|three|four|five|six">

Content of the second column

</div>
...
</div>
```

The content of a slide or slide column can be text (including lists and formulas), a table, program code, or a reference to an image file with a description of the image content.

````md
<div class="columns">
<div class="one|two|three|four|five|six">

Slide text (including lists and formulas)

</div>
<div class="one|two|three|four|five|six">

| Column A | Column B | ... |
|-|-|-|
| Content 1 | Content 2 | ... |
| ... | ... | ... |

</div>
<div class="one|two|three|four|five|six">

```ProgrammingLanguage
Source code
```

</div>
<div class="one|two|three|four|five|six">

![Placeholder for image description](./ImagePath)

</div>
</div>
````

The images themselves are made with Tikz and Mermaid.js. The Tikz and Mermaid.js source files are automatically compiled into SVG files in Visual Studio Code using the *RunOnSave* extension.

## Folder Structure

- The folder `./Sessions` contains the materials for the individual sessions
- The folder `./Sessions/Session_XX` contains the slide set for session `XX`
- The file `./Sessions/Session_XX/Slides.md` contains the Latex source code for the slide set of session `XX`
- The folder `./Sessions/Session_XX/Diagrams` contains the Tikz- and Mermaid.js diagrams.
- The file `./Sessions/Session_XX/Diagrams/Diagram_Name.tikz.tex` contains the source code of a Tikz diagram
- The file `./Sessions/Session_XX/Diagrams/Diagram_Name.tikz.svg` contains the compiled SVG code of a Tikz diagram
- The file `./Sessions/Session_XX/Diagrams/Diagram_Name.mmd` contains the source code of a Mermaid.js diagram
- The file `./Sessions/Session_XX/Diagrams/Diagram_Name.svg` contains the compiled SVG code of a Mermaid.js diagram
- The folder `./Sessions/Session_XX/Homeworks` contains the homework sheets for session `XX`
- The file `./Sessions/Session_XX/Homeworks/Homework_YY.tex` contains homework sheet `YY` for session `XX`
- The folder `./Sessions/Session_XX/Exams` contains the exam sheets for session `XX`
- The file `./Sessions/Session_XX/Exams/Exam_YY.tex` contains exam sheet `YY` for session `XX`