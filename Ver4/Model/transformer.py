# models/transformer.py
import torch
import torch.nn as nn
import math

class Transformer(nn.Module):
    def __init__(self, vocab_size, d_model=512, nhead=8, num_layers=6, max_len=512):
        super(Transformer, self).__init__()
        
        self.d_model = d_model
        self.max_len = max_len
        
        # Embedding Layer
        self.embedding = nn.Embedding(vocab_size, d_model)
        
        # Positional Encoding
        self.positional_encoding = nn.Parameter(torch.zeros(1, max_len, d_model), requires_grad=False)
        self._init_positional_encoding()

        # Transformer Decoder Layer
        self.transformer_decoder = nn.TransformerDecoder(
            nn.TransformerDecoderLayer(d_model=d_model, nhead=nhead), 
            num_layers=num_layers
        )

        # Output Layer
        self.fc_out = nn.Linear(d_model, vocab_size)

    def _init_positional_encoding(self):
        # Generate the sinusoidal positional encoding
        position = torch.arange(0, self.max_len).unsqueeze(1).float()
        div_term = torch.exp(torch.arange(0, self.d_model, 2).float() * -(math.log(10000.0) / self.d_model))
        self.positional_encoding[0, :, 0::2] = torch.sin(position * div_term)
        self.positional_encoding[0, :, 1::2] = torch.cos(position * div_term)

    def forward(self, tgt, memory):
        # Apply positional encoding
        tgt = self.embedding(tgt) + self.positional_encoding[:, :tgt.size(1), :]

        # Pass through transformer decoder
        output = self.transformer_decoder(tgt, memory)

        # Pass through final linear layer
        output = self.fc_out(output)
        return output
