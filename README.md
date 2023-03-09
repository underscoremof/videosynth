# Videosynth

A little interactive Videosynthesizer that simulates videofeedback, the process of pointing a camera at its own playback monitor.

The videosynth is split into two parts: 

Preprocessing stage: the actual self-modulating image synthesis containing:

* Random Noise Generator
* Color Generator
* Feedback Simulation

Postprocessing:does not influence videosynthesis:

* BGR-Filter


## Prerequisites

(Asuming you already have [pip](https://pip.pypa.io/en/stable/), [python](https://www.python.org/downloads/) and [git](https://git-scm.com/downloads) installed)

To run the script please first install the follwoing libraries:
* [opencv](https://docs.opencv.org/4.x/index.html)
* [numpy](https://numpy.org/)

if not installed please run:
```bash
pip install "name of library"
```
in your terminal.



## How to use

1. Clone repositiry

```bash
git clone https://github.com/underscoremof/videosynth.git
```
2. Navigate to folder
```bash
cd .\videosynth\
```
3. Run script
```bash
python videosynth.py
```
### Controls:
Once the script is running you should see two windows. One called "Video" displaing the actual synthesized video and one called "Processing" which contains the trackbars giving you controll over pre- and post processing of the video. Additionally you can always press the "r" key on your keyboard to reset the synthesis, the"s" key to save a screenshot of the video or the "q" key to terminate the script.

This is a work in progress and might change in the future.

## Acknowledgements

This project was inspired by several reddit posts on r/videosynthesis by user [u/STEEDOE](https://www.reddit.com/user/STEEDOE/).

