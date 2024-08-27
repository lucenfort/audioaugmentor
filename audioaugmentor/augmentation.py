import numpy as np
import librosa
from scipy.signal import butter, sosfilt

def normalize_audio(y: np.ndarray) -> np.ndarray:
    """Normaliza o sinal de áudio para garantir que sua amplitude máxima seja 1."""
    return y / np.max(np.abs(y))

def add_white_noise(y: np.ndarray, noise_factor: float = 0.005) -> np.ndarray:
    """Adiciona ruído branco ao sinal de áudio."""
    noise = np.random.randn(len(y))
    augmented_audio = y + noise_factor * noise
    return normalize_audio(augmented_audio)

def pitch_shift(y: np.ndarray, sr: int, n_steps: int) -> np.ndarray:
    """Altera o pitch do sinal de áudio."""
    shifted_audio = librosa.effects.pitch_shift(y, sr=sr, n_steps=n_steps)
    return normalize_audio(shifted_audio)

def time_stretch(y: np.ndarray, rate: float = 1.0) -> np.ndarray:
    """Altera a velocidade do sinal de áudio sem alterar o pitch."""
    stretched_audio = librosa.effects.time_stretch(y, rate=rate)
    return normalize_audio(stretched_audio)

def change_volume(y: np.ndarray, factor: float = 1.0) -> np.ndarray:
    """Altera o volume do sinal de áudio."""
    return normalize_audio(y * factor)

def invert_audio(y: np.ndarray) -> np.ndarray:
    """Inverte o sinal de áudio (espelhamento no tempo)."""
    return np.flipud(y)

def apply_echo(y: np.ndarray, sr: int, delay: float = 0.2, attenuation: float = 0.6) -> np.ndarray:
    """Aplica um efeito de eco ao sinal de áudio."""
    delay_samples = int(delay * sr)
    echo = np.zeros_like(y)
    echo[delay_samples:] = y[:-delay_samples] * attenuation
    augmented_audio = y + echo
    return normalize_audio(augmented_audio)

def time_shift(y: np.ndarray, shift_max: float = 0.2) -> np.ndarray:
    """Desloca o sinal de áudio no tempo."""
    shift = np.random.randint(int(shift_max * len(y)))
    shifted_audio = np.roll(y, shift)
    return normalize_audio(shifted_audio)

def low_pass_filter(y: np.ndarray, sr: int, cutoff: int = 4000) -> np.ndarray:
    """Aplica um filtro passa-baixa ao sinal de áudio."""
    sos = butter(10, cutoff, btype='low', fs=sr, output='sos')
    filtered_audio = sosfilt(sos, y)
    return normalize_audio(filtered_audio)

def combined_augmentation(y: np.ndarray, sr: int, noise_factor: float = 0.005, pitch_steps: int = 2, echo_delay: float = 0.2) -> np.ndarray:
    """Aplica uma combinação de técnicas de aumento de dados ao sinal de áudio."""
    y = add_white_noise(y, noise_factor=noise_factor)
    y = pitch_shift(y, sr=sr, n_steps=pitch_steps)
    y = apply_echo(y, sr=sr, delay=echo_delay)
    return normalize_audio(y)
