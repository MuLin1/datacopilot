from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments, Seq2SeqTrainingArguments, Seq2SeqTrainer
from datasets import Dataset

# 加载预训练模型和分词器
model_name = 't5-small'
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# 创建数据集
train_data = {
    'input_text': ['帮我挑几只定投的指数基金'],
    'target_text': ["SELECT 基金名称 FROM FundTable WHERE 3 = '指数型'"]
}

train_dataset = Dataset.from_dict(train_data)

def preprocess_function(examples):
    inputs = examples['input_text']
    targets = examples['target_text']
    model_inputs = tokenizer(inputs, max_length=128, truncation=True)
    labels = tokenizer(targets, max_length=128, truncation=True)

    model_inputs['labels'] = labels['input_ids']
    return model_inputs

tokenized_train_dataset = train_dataset.map(preprocess_function, batched=True)

# 定义训练参数
training_args = Seq2SeqTrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    learning_rate=5e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=3,
    predict_with_generate=True
)

# 创建Trainer
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset
)

# 开始训练
trainer.train()
