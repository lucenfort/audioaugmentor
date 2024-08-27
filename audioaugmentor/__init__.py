"""audioaugmentor - Pacote de aumento de dados para processamento de áudio."""

from .augmentation import (
    normalize_audio,
    add_white_noise,
    pitch_shift,
    time_stretch,
    change_volume,
    invert_audio,
    apply_echo,
    time_shift,
    low_pass_filter,
    combined_augmentation,
)

__version__ = '0.1.0'

__author__ = 'Luciano Arruda <lucianoarruda@aluno.uema.br>'

__all__ = [
    "normalize_audio",
    "add_white_noise",
    "pitch_shift",
    "time_stretch",
    "change_volume",
    "invert_audio",
    "apply_echo",
    "time_shift",
    "low_pass_filter",
    "combined_augmentation",
]