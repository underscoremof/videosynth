# Videosynth - WIP
<p>A little interactive Videosynthesizer that simulates videofeedback, the process of pointing a camera at its own playback monitor.</p>
<br>
<p>The videosynth is split into two parts: </p>
<p>Preprocessing stage: the actual self modulating image synthesis containing:</p>
<ul>
    <li> Random Noise Generator </li>
    <li> Color Generator </li>
    <li> Feedback Simulator </li>
</ul>
<br>
<p> Postprocessing stage: does not influence videosynthesis:</p>
<ul>
    <li> BGR Filter </li>
</ul> 


## Prerequisites

<p>(Asuming you already have <a hreaf="https://pip.pypa.io/en/stable/"> pip </a>, <a hreaf="https://www.python.org/downloads/">python</a> and <a hreaf="https://git-scm.com/downloads"> git </a> installed)</p>
<br>
<p>To run this script please first install the following libraries:</p>
<ul>
    <li><a hreaf="https://docs.opencv.org/4.x/d0/d3d/tutorial_general_install.html">opencv</a><br> if not installed please run: <br>
    ''' pip install opencv'''<br>
    in your terminal</li>
    <li><a>numpy</a></li>
</ul>


## How to use
Clone Repository
navigate to folder 
run videosynth.py
controls:

## Acknowledgements
<p>This project was inspired by several reddit posts on r/videosynthesis by user u/STEEDOE.</p>
