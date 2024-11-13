# scripts/data_preprocessing.py
from torch.utils.data import Dataset
import torch

class ConversationDataset(Dataset):
    def __init__(self, data_file, tokenizer, max_length=512):
        self.data_file = data_file
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.data = self.load_data()

    def load_data(self):
        # Load your dialogue data here (you can also preprocess it)
        with open(self.data_file, 'r') as f:
            data = f.readlines()
        return data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        conversation = self.data[idx]
        tokens = self.tokenizer.encode(conversation, max_length=self.max_length, truncation=True, padding='max_length')
        return torch.tensor(tokens)

def create_dataloader(data_file, tokenizer, batch_size=32):
    dataset = ConversationDataset(data_file, tokenizer)
    return torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)
