# kdt-ai-aws
Forked from "https://github.com/sackoh/kdt-ai-aws"

### Activate conda virtual environment
```
conda activate pytorch_p36
```

### Install required libraries
```
pip install -r requirements.txt
```


## Train Model
```
python train_ml.py
```

## Unittest model handler
```
python -m unittest -v test_model_handler.py
```

## Test API on remote
#### In a local cli
```
curl -d '{"text":["영화 오랜만에 봤는데 괜찮은 영화였어", "정말 지루했어"]}' \
-H "Cotent-Type : application/json" \
-X POST \
http://host:port/predict
```

#### Using Python Script
```
import requests
url  = "http://host:port/predict"
data = {"text":["영화 오랜만에 봤는데 괜찮은 영화였어", "정말 지루했어"]}
response = requests.post(url, json=data)
print(response)
```
