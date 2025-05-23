
# LLM Fine-Tuning with Weights & Biases (W&B)

This project demonstrates how to fine-tune a GPT-2 language model using Hugging Face Transformers and track training runs using Weights & Biases (W&B).

## 🧰 Features

- Fine-tune GPT-2 on a subset of the WikiText-2 dataset.
- Track loss, metrics, and model hyperparameters in real time with W&B.
- Simple, lightweight demo suitable for experimentation or learning.
- Works as both a script (`train.py`) or in a Jupyter notebook (optional).

## 📦 Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/llm-wandb-demo.git
cd llm-wandb-demo
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Authenticate Weights & Biases

```bash
wandb login
```

Paste your W&B API key when prompted (from https://wandb.ai/authorize).

## 🚀 Run Training

Run the script to start training:

```bash
python train.py
```

Training will start on a small dataset and log results to your W&B project dashboard.

## 📊 Results

After running, you can view your experiment at:

```
https://wandb.ai/YOUR_USERNAME/llm-wandb-demo
```

## 📁 Project Structure

```
llm-wandb-demo/
├── train.py              # Main training script
├── requirements.txt      # Python dependencies
├── README.md             # Project description and instructions
└── .gitignore            # Ignored files for Git
```

## 📝 Notes

- The dataset is a small sample (`train[:1000]`) to keep training fast and lightweight.
- GPT-2 tokenizer doesn't have a pad token by default; this is set manually.
- W&B automatically logs training metrics, system info, and hyperparameters.

## 💡 License

This project is open source and free to use under the [MIT License](LICENSE).
