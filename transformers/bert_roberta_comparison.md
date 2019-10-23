## PyTorch-bert 和 PyTorch-roberta 在文本分类上的比较

1. **参数设置**：

   - max_seq_length = 128

   - train_batch_size = 16

   - eval_batch_size = 16

   - learning_rate = 5e-5

   - num_train_epochs = 1.0

   - save_checkpoint_steps = 100

     

2. **实验效果：**

   - ### PyTorch-bert 的训练和预测结果

   - **首次训练和预测结果：**

     - PyTorch-bert 训练

     ```python
     Running training
     
     INFO  Num examples = 2000
     INFO  Num Epochs = 1
     INFO  Instantaneous batch size per GPU = 16
     INFO  Total train batch size (w. parallel, distributed & accumulation) = 16
     INFO  Gradient Accumulation steps = 1
     INFO  Total optimization steps = 125
     ************************ Training time 24.254299 秒
     ```

     - PyTorch-bert 预测

     ```python
     Running evaluation 
     
     INFO  Num examples = 2000
     INFO  Batch size = 16
     INFO  ***** Eval results  *****
     INFO  acc = 0.7988994497248624
     INFO  acc_and_f1 = 0.8005324020277855
     INFO  f1 = 0.8021653543307087
     ************************ Evaluation time 16.960302 秒
     ```

   - **从cache中直接加载数据的训练和预测结果**：

     - PyTorch-bert 训练

     ```python
     Running training
     
     INFO  Num examples = 2000
     INFO  Num Epochs = 1
     INFO  Instantaneous batch size per GPU = 16
     INFO  Total train batch size (w. parallel, distributed & accumulation) = 16
     INFO  Gradient Accumulation steps = 1
     Total optimization steps = 125
     
     ************************ Training time 26.924685 秒
     ```

     - PyTorch-bert 预测

     ```python
      Running evaluation 
      
      INFO  Num examples = 2000
      INFO  Batch size = 16
      INFO  ***** Eval results  *****
      INFO  acc = 0.7988994497248624
      INFO  acc_and_f1 = 0.8005324020277855
      INFO  f1 = 0.8021653543307087
     ************************ Evaluation time 6.711065 秒
     ```

     

   - ### PyTorch-roberta 的训练和预测结果

   - **首次训练和预测结果：**

     - PyTorch-roberta 训练

     ```python
      Running training
     
      INFO  Num examples = 2000
      INFO  Num Epochs = 1
      INFO  Instantaneous batch size per GPU = 16
      INFO  Total train batch size (w. parallel, distributed & accumulation) = 16
      INFO  Gradient Accumulation steps = 1
      INFO  Total optimization steps = 125
     
     ************************ Training time 24.792296 秒
     ```

     

     - PyTorch-roberta 预测

     ```python
      Running evaluation 
     
      INFO  Num examples = 2000
      INFO  Batch size = 16
      INFO  ***** Eval results  *****
      INFO  acc = 0.7903951975987994
      INFO  acc_and_f1 = 0.7968869465234729
      INFO  f1 = 0.8033786954481464
     ************************ Evaluation time 10.762685 秒
     ```

     

   - **从cache中直接加载数据的训练和预测结果**：

     - PyTorch-roberta 训练

     ```python
      Running training
     
      INFO  Num examples = 1999
      INFO  Num Epochs = 1
      INFO  Instantaneous batch size per GPU = 16
      INFO  Total train batch size (w. parallel, distributed & accumulation) = 16
      INFO  Gradient Accumulation steps = 1
      INFO  Total optimization steps = 125
     
     ************************ Training time 27.662308 秒
     ```

     - PyTorch-roberta 预测

     ```python
      Running evaluation 
     
      INFO  Num examples = 2000
      INFO  Batch size = 16
      INFO  ***** Eval results  *****
      INFO  acc = 0.7903951975987994
      INFO  acc_and_f1 = 0.7968869465234729
      INFO  f1 = 0.8033786954481464
     ************************ Evaluation time 6.790019 秒
     ```

     

   

3. **实验结果：**

   |       任务分类       | sample | 总时长  |
   | :------------------: | :----: | :-----: |
   |   PyTorch-bert训练   |  2000  | 26.92 s |
   |   PyTorch-bert预测   |  2000  | 6.71 s  |
   | PyTorch-roberta 训练 |  2000  | 27.66 s |
   | PyTorch-roberta 预测 |  2000  | 6.79 s  |