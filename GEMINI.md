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
- Homework after each in-person session
- Exam at the beginning of each subsequent in-person session
- The type of exam is a multiple-choice test
- The duration of the exam is 20 minutes
- No aids are allowed for the exam

## Presentation Technology

The slides for the individual sessions are made with Latex Beamer. Here is the template for the Latex source files:

```latex
\documentclass[aspectratio=169,8pt]{beamer}

% Loading the custom Beamer theme
\newcommand{\basepath}{../../../latex-beamer-theme-fhooe/sources}
\usepackage{\basepath/beamerthemefhooe}

\renewcommand{\sectiontocframesubtitle}{Table of contents}

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

The actual content slides are made using custom commands for one-, two- and three-column slide layouts:

```latex
% Template for a one-column slide
\frameOneColumn{}{Slide Title}{c}{
    Slide Content
}

% Template for a two-column slide
\frameTwoColumn{}{Slide Title}{c}{
    First Column Content
}{
    Second Column Content
}

% Template for a three-column slide
\frameOneColumn{}{Slide Title}{c}{
    First Column Content
}{
    Second Column Content
}{
    Third Column Content
}
```

## Folder Structure

- The folder `./Materials` contains the materials for the individual sessions
- The folder `./Materials/Session_XX` contains the slide set for session `XX`
- The file `./Materials/Session_XX/Slides.tex` contains the Latex source code for the slide set of session `XX`
- The folder `./Materials/Session_XX/Homework_Sheets` contains the homework sheets for session `XX`
- The file `./Materials/Session_XX/Homework_Sheets/Homework_Sheet__YY.tex` contains homework sheet `YY` for session `XX`
- The folder `./Materials/Session_XX/Exam_Sheets` contains the exam sheets for session `XX`
- The file `./Materials/Session_XX/Exam_Sheets/Exam_Sheets_YY.tex` contains exam sheet `YY` for session `XX`