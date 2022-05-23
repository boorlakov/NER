# NER

Solution for Dasha.AI test task

## Usage

To install dependencies simply run following command

```bash
python setup.py
```

### Inference example

```py
tokenizer = AutoTokenizer.from_pretrained('./ner/models/distilbert/five_epochs/')

paragraph = "Vladimir Burlakov want to see a flight from la to ny"
tokens = tokenizer(paragraph)
torch.tensor(tokens['input_ids']).unsqueeze(0).size()

model = AutoModelForTokenClassification.from_pretrained('./ner/models/distilbert/five_epochs/')

predictions = model.forward(input_ids=torch.tensor(tokens['input_ids']).unsqueeze(0), attention_mask=torch.tensor(tokens['attention_mask']).unsqueeze(0))
predictions = torch.argmax(predictions.logits.squeeze(), axis=1)
predictions = [entity_classes[i] for i in predictions]

words = tokenizer.batch_decode(tokens['input_ids'])

print(pd.DataFrame({'ner': predictions, 'words': words}))
```

`entity_classes` могут быть найдены в `uncased_distilbert_base_training.ipynb`
