Efficient CNN based summarization of surveillance videos for resource-constrained devices
==================
Paper
=========
https://www.sciencedirect.com/science/article/pii/S0167865518303842

Repository Details
=========
This repository contains two root folders: 1) VS-Python and 2) VS-Matlab. This paper has been implemented in both these languages.

VS-Python (1)
=======
The python implementation of this paper has some prerequisites that are necassary for running the code.
The two most important dependencies are: OpenCV >= 3.4 and Caffe (deep learning framework).

OpenCV can be easily installed by following the below links:
- https://jeanvitor.com/cpp-opencv-windonws10-installing/
- https://docs.opencv.org/3.4.3/d3/d52/tutorial_windows_install.html

These are links for pre-built OpenCV libraries.

Caffe building is a little bit hard and you need to follow up a straight forward tutorial from YouTube. 

Here is the official caffe installation page, which you may find hard to follow, but do not worry I will also share a tutorial link
- https://caffe.berkeleyvision.org/installation.html
- https://github.com/BVLC/caffe/tree/windows

Here is the YouTube link:

- https://www.youtube.com/watch?v=nrzAF2sxHHM

Furthermore, you need to install scikit-learn, tkinter, and numpy which are easy to install and can be done through just pip command.

Executing/Running the Code
=========
Running Video
- https://www.youtube.com/watch?v=deqwQ-7sumU&feature=youtu.be


Once you have all the dependencies installed and the models are downloaded, then running the code is pretty easy.

1. Open file "main.py" in any of your favourite editor [I would recommend spyder IDE]
2. Run the file "main.py" or type in command prompt "python main.py"
3. After running the program will ask you about the input video, select any video with format supported by OpenCV.
4. If everything is fine, programming will start running and will save the candidate keyframes in folder as "keyframes\temp\" (you can change the path according to your requirement
5. After this process is completed, run "postprocessing.py" which will remove redundant frames.
6. You can change the threshold for shot segmentation on line number 77 and path of the output frames at line number 88.

Downloading Caffe models (weights)
==========
Caffe models can be downloaded from the link below:

- https://drive.google.com/drive/folders/1p8M3rjWF8h5km7uyQkYaxwo0ELx4OFsb?usp=sharing


VS-Matlab (2)
=======
These codes will be uploaded soon.


Contact Me
========
If you feel any difficulty or errors, please refer to tanveerkhattak37973[at][gmail]


Citation
=======
<pre>
<code>
@article{muhammad2020efficient,
  title={Efficient CNN based summarization of surveillance videos for resource-constrained devices},
  author={Muhammad, Khan and Hussain, Tanveer and Baik, Sung Wook},
  journal={Pattern Recognition Letters},
  volume={130},
  pages={370--375},
  year={2020},
  publisher={Elsevier}
}
</code>
</pre>
If you are interested in Multi-view Video Summarization domain you may want to read our recent survey:

<pre>
<code>
@article{hussain2020comprehensive,
  title={A comprehensive survey of multi-view video summarization},
  author={Hussain, Tanveer and Muhammad, Khan and Ding, Weiping and Lloret, Jaime and Baik, Sung Wook and de Albuquerque, Victor Hugo C},
  journal={Pattern Recognition},
  volume={109},
  pages={107567},
  year={2020},
  publisher={Elsevier}
}
</code>
</pre>

### My further research [sorted year-wise] on Video Summarization (single- and multi-view video summarization) domain is as follows:
#### Multi-view Video Summarization
<pre>
<code>
@ARTICLE{9208765,
  author={T. {Hussain} and K. {Muhammad} and A. {Ullah} and J. {Del Ser} and A. H. {Gandomi} and M. {Sajjad} and S. W. {Baik} and V. H. C. {de Albuquerque}},
  journal={IEEE Internet of Things Journal}, 
  title={Multi-View Summarization and Activity Recognition Meet Edge Computing in IoT Environments}, 
  year={2020},
  volume={},
  number={},
  pages={1-1},
  doi={10.1109/JIOT.2020.3027483}}
@article{hussain2019intelligent,
  title={Intelligent Embedded Vision for Summarization of Multiview Videos in IIoT},
  author={Hussain, Tanveer and Muhammad, Khan and Del Ser, Javier and Baik, Sung Wook and de Albuquerque, Victor Hugo C},
  journal={IEEE Transactions on Industrial Informatics},
  volume={16},
  number={4},
  pages={2592--2602},
  year={2019},
  publisher={IEEE}
}
@article{hussain2019cloud,
  title={Cloud-assisted multiview video summarization using CNN and bidirectional LSTM},
  author={Hussain, Tanveer and Muhammad, Khan and Ullah, Amin and Cao, Zehong and Baik, Sung Wook and de Albuquerque, Victor Hugo C},
  journal={IEEE Transactions on Industrial Informatics},
  volume={16},
  number={1},
  pages={77--86},
  year={2019},
  publisher={IEEE}
}
@article{후세인2018구조적인,
  title={구조적인 유사성에 기반한 다중 뷰 비디오의 효율적인 키프레임 추출},
  author={후세인 and 탄베르 and 칸살만 and 이미영 and 백성욱 and others},
  journal={한국차세대컴퓨팅학회 논문지},
  volume={14},
  number={6},
  pages={7--14},
  year={2018}
}
</code>
</pre>


#### Single-view Video Summarization
<pre>
<code>
@article{muhammad2020efficient,
  title={Efficient and Privacy Preserving Video Transmission in 5G-Enabled IoT Surveillance Networks: Current Challenges and Future Directions},
  author={Muhammad, Khan and Hussain, Tanveer and Rodrigues, Joel JPC and Bellavista, Paolo and de Macedo, Antonio Roberto L and de Albuquerque, Victor Hugo C},
  journal={IEEE Network},
  year={2020},
  publisher={IEEE}
}
@article{muhammad2020efficient,
  title={Efficient CNN based summarization of surveillance videos for resource-constrained devices},
  author={Muhammad, Khan and Hussain, Tanveer and Baik, Sung Wook},
  journal={Pattern Recognition Letters},
  volume={130},
  pages={370--375},
  year={2020},
  publisher={Elsevier}
}
@article{muhammad2019deepres,
  title={DeepReS: A Deep Learning-Based Video Summarization Strategy for Resource-Constrained Industrial Surveillance Scenarios},
  author={Muhammad, Khan and Hussain, Tanveer and Del Ser, Javier and Palade, Vasile and De Albuquerque, Victor Hugo C},
  journal={IEEE Transactions on Industrial Informatics},
  volume={16},
  number={9},
  pages={5938--5947},
  year={2019},
  publisher={IEEE}
}
@article{muhammad2019cost,
  title={Cost-effective video summarization using deep CNN with hierarchical weighted fusion for IoT surveillance networks},
  author={Muhammad, Khan and Hussain, Tanveer and Tanveer, Muhammad and Sannino, Giovanna and de Albuquerque, Victor Hugo C},
  journal={IEEE Internet of Things Journal},
  volume={7},
  number={5},
  pages={4455--4463},
  year={2019},
  publisher={IEEE}
}
</code>
</pre>

