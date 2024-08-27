
import unittest
import numpy as np
from audioaugmentor.augmentation import (
    add_white_noise,
    pitch_shift,
    time_stretch,
    change_volume,
    invert_audio,
    apply_echo,
    time_shift,
    low_pass_filter,
    combined_augmentation
)

class TestAudioAugmentor(unittest.TestCase):

    def setUp(self):
        self.sr = 22050  # Taxa de amostragem padrão para testes
        self.y = np.sin(2 * np.pi * 220 * np.linspace(0, 5, self.sr * 5))  # Sinal de áudio de teste (senoide)

    def test_add_white_noise(self):
        augmented = add_white_noise(self.y)
        self.assertEqual(len(augmented), len(self.y))

    def test_pitch_shift(self):
        shifted = pitch_shift(self.y, self.sr, n_steps=2)
        self.assertEqual(len(shifted), len(self.y))

    def test_time_stretch(self):
        stretched = time_stretch(self.y, rate=1.5)
        self.assertTrue(len(stretched) > len(self.y))

    def test_change_volume(self):
        louder = change_volume(self.y, factor=2.0)
        self.assertEqual(len(louder), len(self.y))

    def test_invert_audio(self):
        inverted = invert_audio(self.y)
        self.assertEqual(len(inverted), len(self.y))

    def test_apply_echo(self):
        echoed = apply_echo(self.y, self.sr, delay=0.5)
        self.assertEqual(len(echoed), len(self.y))

    def test_time_shift(self):
        shifted = time_shift(self.y)
        self.assertEqual(len(shifted), len(self.y))

    def test_low_pass_filter(self):
        filtered = low_pass_filter(self.y, self.sr, cutoff=1000)
        self.assertEqual(len(filtered), len(self.y))

    def test_combined_augmentation(self):
        augmented = combined_augmentation(self.y, self.sr)
        self.assertEqual(len(augmented), len(self.y))

if __name__ == "__main__":
    unittest.main()