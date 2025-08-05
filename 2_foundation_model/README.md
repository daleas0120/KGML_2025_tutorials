# Apply Scientific Foundation Model for Materials Science

Author: [Changwen Xu](https://changwenxu98.github.io/)

Welcome to the official code repository for the **Knowledge-Guided Machine Learning (KGML) Workshop**. This repository includes three tutorial notebooks that demonstrate how to incorporate domain knowledge into machine learning workflows for materials science and scientific reasoning.

## 📁 Repository Structure

- `CLOUD.ipynb`: Pretraining and fine-tuning a transformer-based foundation model for crystal property prediction.
- `DREAMS_bulk_modulus_demo.ipynb`: A LLM-agentic workflow for predicting bulk modulus from crystal structures.
- `multiagent_authoritarian_anthropic.ipynb`: A multi-agent system that simulates scientific discourse and decision-making using language models guided by principles of knowledge hierarchy.

---

## 🔍 Tutorial Descriptions

### 1. `CLOUD.ipynb`: Crystal Language Foundation Model (CLOUD)
This notebook presents the **CLOUD** model — a BERT-style transformer pretrained on symmetry-consistent representations of crystal structures. It demonstrates:

- How to tokenize crystal structures using a symmetry-aware string representation.
- Pretraining with a masked language modeling (MLM) objective.
- Fine-tuning on a downstream regression task (e.g., dielectric constant).
- Integrate Debye model for physics-consistent ML framework

> 📌 **Key Concepts**: Crystal representation learning, pretraining, transfer learning, transformer models, differentiable physics.

---

### 2. `DREAMS_bulk_modulus_demo.ipynb`: Differentiable Elasticity Modeling
This notebook introduces **DREAMS** — an agentic framework where the LLM agents automate the DFT calculation to compute the bulk modulus.

- Builds atomic structures with varying Cu/Au concentrations.
- Automatically generates DFT-like input settings.
- Computes bulk modulus using the equation of state (EOS) fit.

> 📌 **Key Concepts**: LLM agents, DFT calculation, autonomous science.

---

### 3. `multiagent_authoritarian_anthropic.ipynb`: Scientific Multi-Agent Reasoning
This notebook presents a prototype of a **multi-agent dialogue system** simulating scientific deliberation and collective decision-making. The notebook is adapted from examples from [LangChain](https://github.com/langchain-ai/langchain).

- Agents play different roles in a scientific conversation (e.g., Director, Analyst).
- Uses Anthropic Claude models via LangChain.
- Demonstrates how structured interaction protocols and hierarchy can guide model behavior.

> 📌 **Key Concepts**: Multi-agent systems, scientific reasoning, role-based prompting, alignment.

---

## 🧩 Requirements

- Python 3.9+
- PyTorch, HuggingFace Transformers, LangChain, OpenAI/Anthropic SDKs, and scientific computing libraries (NumPy, pandas, etc.)
- See each notebook's cells for specific package installation if needed.

---

## 💡 Citation & Attribution

If you use or build upon these tutorials, please cite the KGML workshop and acknowledge the authors. For inquiries or collaborations, contact [Changwen Xu](mailto:changwex@umich.edu).

---

## 🌐 Workshop Info

This repository is part of the **Knowledge-Guided Machine Learning Workshop**. For more details, visit the [official workshop website](https://midas.umich.edu/events/kgml-workshop-leading-the-new-paradigm-of-ai-for-science/).

