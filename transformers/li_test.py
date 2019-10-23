# coding: utf-8
# @Time    : 2019/9/29 17:35
# @Author  : 李志伟
# @Email   : lizhiweiena@163.com


import torch

from transformers.tokenization_bert import BertTokenizer
from transformers.modeling_bert import BertModel

import sys
import PIL

def main():
    # tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    # print("【tokenizer】 : ", tokenizer)
    # model = BertModel.from_pretrained('bert-base-uncased')
    # print("【model】 : ", model)
    # input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute")).unsqueeze(0)  # Batch size 1
    # print("【input_ids】 : ", input_ids)
    # outputs = model(input_ids)
    # print("【outputs】 : ", outputs)
    # last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple
    # print("【last_hidden_states】 : ", last_hidden_states)
    #
    # embedding = model.embeddings.word_embeddings
    # print("【embedding】 : ", embedding)

    # print("=" * 100)

    print(sys.path)
    print("=" * 100)
    print(PIL.__file__)

if __name__ == "__main__":
    main()









