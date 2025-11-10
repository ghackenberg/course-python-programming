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

The slides for the individual sessions are made with Latex Beamer. Here is the general template for the Latex source files:

```latex
\documentclass[aspectratio=169,8pt]{beamer}

% Loading the custom Beamer theme
\newcommand{\basepath}{../../../latex-beamer-theme-fhooe/sources}
\usepackage{\basepath/beamerthemefhooe}

\renewcommand{\sectiontocframesubtitle}{Table of Contents}
\renewcommand{\subsectiontocframesubtitle}{Table of Contents}

\title{Programming with Python}
\subtitle{Session X: ...}
\author[Dr. Georg Hackenberg, Professor for Industrial Informatics (\href{mailto:georg.hackenberg@fh-wels.at}{georg.hackenberg@fh-wels.at})]{Dr. Georg Hackenberg BSc MSc\\Professor for Industrial Informatics\\(\href{mailto:georg.hackenberg@fh-wels.at}{georg.hackenberg@fh-wels.at})}
\institute[Subject Area Information Technology, School of Engineering, University of Applied Sciences Upper Austria]{Subject Area Information Technology\\School of Engineering\\University of Applied Sciences Upper Austria}
\date{\today}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

\section{Section Title}

\subsection{Subsection Title}

...

\end{document}
```

The actual content slides are made using the custom frame environment `cframe` and the custom column environment `ccolumn`. The custom frame environment `cframe` takes four arguments:

1. the **slide title** (if left blank, the default slide title is used, which includes the document title and subtitle as well as the section/subsection names),
2. the **slide subtitle** (if left blank, the default slide subtitle is used, which shows a placeholder in the output),
3. the **number of columns** (used for calculating the column widths),
4. and the **vertical column aligment** (`c` for center):

Here are some examples of how to use the custom environments:

```latex
% Template for a one-column slide
\begin{cframe}{}{Slide Title}{1}{c}
    \begin{columns}
        \begin{ccolumn}
            Slide Content
        \end{ccolumn}
    \end{columns}
\end{cframe}

% Template for a two-column slide
\begin{cframe}{}{Slide Title}{2}{c}
    \begin{columns}
        \begin{ccolumn}
            First Column Content
        \end{ccolumn}
        \begin{ccolumn}
            Second Column Content
        \end{ccolumn}
    \end{columns}
\end{cframe}

% Template for a three-column slide
\begin{cframe}{}{Slide Title}{3}{c}
    \begin{columns}
        \begin{ccolumn}
            First Column Content
        \end{ccolumn}
        \begin{ccolumn}
            Second Column Content
        \end{ccolumn}
        \begin{ccolumn}
            Third Column Content
        \end{ccolumn}
    \end{columns}
\end{cframe}
```

Visualizations are scripted with `tikz` and code listings are made with `minted`.

## Folder Structure

- The folder `./Materials` contains the materials for the individual sessions
- The folder `./Materials/Session_XX` contains the slide set for session `XX`
- The file `./Materials/Session_XX/Slides.tex` contains the Latex source code for the slide set of session `XX`
- The folder `./Materials/Session_XX/Homework_Sheets` contains the homework sheets for session `XX`
- The file `./Materials/Session_XX/Homework_Sheets/Homework_Sheet__YY.tex` contains homework sheet `YY` for session `XX`
- The folder `./Materials/Session_XX/Exam_Sheets` contains the exam sheets for session `XX`
- The file `./Materials/Session_XX/Exam_Sheets/Exam_Sheets_YY.tex` contains exam sheet `YY` for session `XX`