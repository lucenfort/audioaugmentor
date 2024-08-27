audioaugmentor
==============

Pacote de aumento de dados para processamento de áudio.

Usage
-----

```python
import librosa
from audioaugmentor.augmentation import add_white_noise, pitch_shift

# Carregar um arquivo de áudio
y, sr = librosa.load('caminho/para/audio.wav')

# Aumentar os dados
y_noisy = add_white_noise(y)
y_shifted = pitch_shift(y, sr, n_steps=2)
```

Installation
------------

Você pode instalar o pacote utilizando pip:

```bash
pip install audioaugmentor
```

Requirements
------------

- `numpy>=1.18.0`
- `librosa>=0.8.0`
- `scipy>=1.4.0`

Compatibility
-------------

Compatível com Python 3.6 e versões superiores.
