
# scripts/train.py
import torch
import torch.optim as optim
from models.transformer import Transformer
from scripts.data_preprocessing import create_dataloader
from torch.utils.data import DataLoader
import time

def train(model, train_loader, optimizer, loss_fn, device):
    model.train()
    total_loss = 0

    for batch in train_loader:
        batch = batch.to(device)
        optimizer.zero_grad()

        # Forward pass
        output = model(batch, batch)  # You would have the model work on batch data

        loss = loss_fn(output.view(-1, output.size(-1)), batch.view(-1))
        total_loss += loss.item()

        # Backpropagate
        loss.backward()
        optimizer.step()

    return total_loss / len(train_loader)

def main():
    # Set up device (CUDA or CPU)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Initialize tokenizer (assumed from a library like Hugging Face Tokenizer)
    tokenizer = ...  # Replace with tokenizer initialization
    train_loader = create_dataloader("data/train_data.txt", tokenizer)

    # Model setup
    vocab_size = 10000  # Use the size of your vocabulary
    model = Transformer(vocab_size).to(device)

    # Optimizer and Loss function
    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    loss_fn = torch.nn.CrossEntropyLoss()

    # Training loop
    for epoch in range(10):  # Adjust number of epochs
        start_time = time.time()
        loss = train(model, train_loader, optimizer, loss_fn, device)
        print(f"Epoch [{epoch+1}], Loss: {loss:.4f}, Time: {time.time() - start_time:.2f}s")

        # Save model checkpoint after every epoch
        torch.save(model.state_dict(), f"checkpoints/model_epoch_{epoch+1}.pt")

if __name__ == "__main__":
    main()
