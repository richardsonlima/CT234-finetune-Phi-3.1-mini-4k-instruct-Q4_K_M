
# Fine-Tuning the Phi-3.1-mini-4k-instruct-Q_K_M Model with MLX-LM

This guide will walk you through fine-tuning the **Phi-3.1-mini-4k-instruct-Q_K_M** model using the **MLX-LM** library. The fine-tuning process will use educational content from [this academic website](https://www.comp.ita.br/~alonso/ensino.html) and its related materials on **data structures, algorithms, complexity**, and more. By the end of this tutorial, you’ll be able to customize the Phi-3.1-mini-4k-instruct-Q_K_M model for educational purposes.

## Step 1: Preparing the Training Data

The educational content from the website covers a wide range of topics including:

- **Data Structures**: Linked lists, trees, stacks, queues, deques
- **Algorithms**: Sorting, searching, recursive algorithms, dynamic programming
- **Complexity**: Time and space complexity analysis
- **Graphs**: Traversal, shortest path algorithms
- **Programming Paradigms**: Object-oriented programming in C++

You can download the materials or structure the content yourself. To facilitate fine-tuning, convert the content into JSON format or download preprocessed data, such as [this dataset](https://huggingface.co/datasets/mzbac/function-calling-llama-3-format-v1.1/tree/main), and store it in a `data` directory.

## Step 2: Installing the MLX-LM Package

To install the **MLX-LM** library, which is required for fine-tuning, run the following command:

```bash
pip install mlx-lm
```

This will provide you with the tools needed to fine-tune the model easily and effectively.

## Step 3: Creating the LoRA Config

The **LoRA (Low-Rank Adaptation)** configuration for fine-tuning the **Phi-3.1-mini-4k-instruct-Q_K_M** model should look like this:

```yaml
# Path to the local model directory or Hugging Face repo.
model: "microsoft/Phi-3-mini-4k-instruct"

# Enable training.
train: true

# Directory containing {train, valid, test}.jsonl files
data: "data"

# PRNG seed.
seed: 0

# Layers to fine-tune.
lora_layers: 32

# Batch size.
batch_size: 1

# Training iterations.
iters: 6000

# Validation batches.
val_batches: 25

# Adam learning rate.
learning_rate: 1e-6

# Report loss after every 10 steps.
steps_per_report: 10

# Validate every 200 steps.
steps_per_eval: 200

# Save trained adapter weights.
adapter_path: "adapters"

# Save model every 1000 steps.
save_every: 1000

# Gradient checkpointing for memory optimization.
grad_checkpoint: true

# LoRA parameters.
lora_parameters:
  keys: ['mlp.gate_proj', 'mlp.down_proj', 'self_attn.q_proj', 'mlp.up_proj', 'self_attn.o_proj','self_attn.v_proj', 'self_attn.k_proj']
  rank: 128
  alpha: 256
  scale: 10.0
  dropout: 0.05
```

## Step 4: Running the Fine-Tuning Process

Once the configuration is ready, fine-tune the **Phi-3.1-mini-4k-instruct-Q_K_M** model by running the following command:

```bash
mlx_lm.lora --config lora_config.yaml
```

MLX-LM will handle the fine-tuning process, adapting the model to the educational content.

## Step 5 (Optional): Fusing the Trained Adapters

To fuse the trained adapters with the original model for distribution or further use, run the following command:

```bash
mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct
```

## Conclusion

By following this guide, you will successfully fine-tune the **Phi-3.1-mini-4k-instruct-Q_K_M** model using **MLX-LM**. The fine-tuning process will equip the model to handle advanced topics related to **data structures**, **algorithms**, and **complexity analysis**—important subjects for educational and research applications. 

For more information or to access the source materials, visit [this website](https://www.comp.ita.br/~alonso/ensino.html).

---

Happy fine-tuning!
