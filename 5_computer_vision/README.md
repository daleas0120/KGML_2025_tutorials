# From Data to Discovery: Applying Computer Vision for Scientific Image Analysis with Vascilia + Napari

Author: [Yasmin Kassim](https://github.com/Yasmin-Kassim)

Join Yasmin Kassim for an immersive session that bridges cutting-edge deep learning with biological discovery. She will unveil VASCilia—a powerful Napari plugin designed for 3D analysis of cochlear hair cell stereocilia bundles—highlighting the challenges of real-world biological datasets and the five deep learning models powering the platform, including Z-Focus Tracker,  PCPAlignNet, 3D instance segmentation, region prediction, and tracking. In the second half, Yasmin will lead a hands-on coding workshop, guiding participants through building their own interactive Napari plugin—complete with data loading, segmentation (traditional and ML-based), instance filtering, measurement export, and UI design. Ideal for anyone passionate about scientific computing, imaging, and elegant toolmaking.

## 🔍 Tutorial Descriptions

This tutorial will provide a practical understanding of:
- What Napari is
- How to install and use it
- How to design and implement your own interactive plugin

Participants will learn how to:

- Set up a Napari plugin interface
- Create buttons to load and segment data (using traditional methods and machine learning)
- Perform instance segmentation
- Delete un-desired objects
- Calculate and export measurements
- Build a basic UI and exit workflow

## 🧩 Pre-Workshop Setup Instructions

1. Install Anaconda

Follow the instructions to install Anaconda: [Download Anaconda Distribution | Anaconda](https://www.anaconda.com/download)


2. Create the kgml_workshop anaconda Environment:

Open your Anacond Terminal Prompt and run the following:
```
conda create -n kgml_workshop python=3.9 -y

conda activate kgml_workshop

pip install numpy scipy pandas matplotlib scikit-image imageio tifffile magicgui napari[all] pyqt5
```


3. Install PyCharm Community Edition

Download and install from: [Download PyCharm: The Python IDE for data science and web development by JetBrains](https://www.jetbrains.com/pycharm/download/?section=windows)


4. Pull this GitHub repo to your computer

---

## 💡 Citation & Attribution

If you use or build upon these tutorials, please cite the KGML workshop and acknowledge the authors. For inquiries or collaborations, contact [Yasmin Kassim](https://github.com/Yasmin-Kassim).

---

## 🌐 Workshop Info

This repository is part of the **Knowledge-Guided Machine Learning Workshop**. For more details, visit the [official workshop website](https://midas.umich.edu/events/kgml-workshop-leading-the-new-paradigm-of-ai-for-science/).

