# scripts/evaluate.py
import torch
from models.transformer import Transformer
from scripts.data_preprocessing import create_dataloader

def evaluate(model, val_loader, loss_fn, device):
    model.eval()
    total_loss = 0

    with torch.no_grad():
        for batch in val_loader:
            batch = batch.to(device)
            output = model(batch, batch)  # Pass batch through model
            loss = loss_fn(output.view(-1, output.size(-1)), batch.view(-1))
            total_loss += loss.item()

    return total_loss / len(val_loader)

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = ...  # Initialize tokenizer
    val_loader = create_dataloader("data/val_data.txt", tokenizer)

    vocab_size = 10000  # Adjust according to your data
    model = Transformer(vocab_size).to(device)

    # Load pre-trained model if available
    model.load_state_dict(torch.load("checkpoints/model_epoch_10.pt"))
    model.eval()

    loss_fn = torch.nn.CrossEntropyLoss()

    val_loss = evaluate(model, val_loader, loss_fn, device)
    print(f"Validation Loss: {val_loss:.4f}")

if __name__ == "__main__":
    main()
