# LIS-Pepper

In this project, the Pepper robot is used to reproduce some words of the Italian sign language. In order to simulate the robot, the simulation tool qiBullet is used (more information [here](https://developer.softbankrobotics.com/blog/qibullet)).

The videos from which the signs were taken can be found [here](https://www.spreadthesign.com/it.it/search/).

# Prerequisites

To run the code, first install qiBullet with:

    pip install --user qibullet
    
Then, install Spacy with:
    
    pip install -U pip setuptools wheel
    pip install -U spacy
    python -m spacy download it_core_news_sm

And PyAudio for the Automatic Speech Recognition module with:

    sudo apt-get install libespeak1 libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
    pip install PyAudio
    
If any problem occurs with the installation of PyAudio, check [here](https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error/35593426#35593426).
