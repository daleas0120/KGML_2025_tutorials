# Topology-Aware Graph Neural Networks by Physics

Author: Haoyang Jiang

## 🌐 Workshop Info

This repository is part of the **Knowledge-Guided Machine Learning Workshop**. For more details, visit the [official workshop website](https://midas.umich.edu/events/kgml-workshop-leading-the-new-paradigm-of-ai-for-science/).

## 1. Data Setup

First, you must get the required data. Click the link below and save the contents to your own Google Drive. In most cases, the files will be added to your drive automatically after you open the link. This step is necessary for the notebooks to run correctly.

* **Data Link:** [Google Drive Folder](https://drive.google.com/drive/folders/1Zjv3Vf9bO-WcQdaF7Lz-6-5Qk_YRHOk4)

---

## 2. Colab Notebooks

### Basic Graph Learning

* [GCN for Cora Dataset](https://colab.research.google.com/drive/1sS3BuJpQBpsKbLpebhLMeC02jfQUgF5X)
* [GCN for ENZYMES](https://colab.research.google.com/drive/1XT4MDvtXlX57Ei7xeUCavjFIRLtrtOlY)

### Graph Learning for River Net

* [Graph learning for the river net](https://colab.research.google.com/drive/1z-JNEkO4MSgF8vaWvw3THqQv61rTzGPf)

### Spatial-Temporal Graph Learning

* [Spatial-temporal graph learning for the traffic data](https://colab.research.google.com/drive/1950jb6MYTmMJt87_tEmv6Sb3X42_id_K)



## 3. Installation for my works

> **Important Note**: Due to the long installation time for dependencies on Google Colab, we strongly recommend setting up and running this project in a **local environment** for a better experience.

### Dependencies

This project primarily depends on `PyTorch` and `PyTorch Geometric` (PyG). Please follow the steps below to install the required libraries.

#### 1. Install PyTorch Geometric (PyG)

The following commands are for an environment with `PyTorch 2.5.1` and `CUDA 12.4`. If your setup is different, please consult the [official PyG installation documentation](https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html) to find the appropriate commands for your system.

```bash
# For PyTorch 2.5.1 and CUDA 12.4
pip install -q torch-scatter -f [https://data.pyg.org/whl/torch-2.5.1+cu124.html](https://data.pyg.org/whl/torch-2.5.1+cu124.html)
pip install -q torch-sparse -f [https://data.pyg.org/whl/torch-2.5.1+cu124.html](https://data.pyg.org/whl/torch-2.5.1+cu124.html)
pip install -q torch-cluster -f [https://data.pyg.org/whl/torch-2.5.1+cu124.html](https://data.pyg.org/whl/torch-2.5.1+cu124.html)
pip install -q git+[https://github.com/pyg-team/pytorch_geometric.git](https://github.com/pyg-team/pytorch_geometric.git)
