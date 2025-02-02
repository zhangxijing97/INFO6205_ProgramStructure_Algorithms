# INFO6205_ProgramStructure_Algorithms

# LaTeX Overview

Basic Document Structure
```
\documentclass{article} % Specifies the type of document (e.g., article, report, book)
\usepackage{amsmath}    % Include extra features like advanced math formatting
\begin{document}        % Start of the document content

Hello, World!           % Your content goes here

\end{document}          % End of the document
```

Sections and Subsections
```
\section{Section Title}
\subsection{Subsection Title}
\subsubsection{Sub-subsection Title}
```

Mathematical Equations
```
\[
a^2 + b^2 = c^2
\]
```

Lists (Bulleted & Numbered)
```
\begin{itemize}
  \item First item
  \item Second item
\end{itemize}

\begin{enumerate}
  \item First item
  \item Second item
\end{enumerate}
```

Tables
```
\begin{tabular}{|c|c|c|}
\hline
Header 1 & Header 2 & Header 3 \\ \hline
Cell 1   & Cell 2   & Cell 3   \\ \hline
Cell 4   & Cell 5   & Cell 6   \\ \hline
\end{tabular}
```

Adding Images
```
\usepackage{graphicx}

\begin{figure}[h]
\centering
\includegraphics[width=0.5\textwidth]{image.jpg} % Adjust width as needed
\caption{A sample image}
\end{figure}
```