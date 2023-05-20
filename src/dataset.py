from torch.utils.data import Dataset
import pandas as pd
import torchaudio
import torch
import os
import glob

class UrbanSoundDataset(Dataset):
    """__Co to robi bazowo:

    
    """    
    def __init__(self, folder_path, transformation, target_sample_rate, num_samples):
        self.file_list = glob.glob(folder_path + "/*.wav")
        self.transformation = transformation
        self.target_sample_rate = target_sample_rate
      
        
    def __len__(self):
        return len(self.anotations)
    
    def __getitem__(self, index):
        audio_sample_path = self.file_list[index]
        label = self._get_audio_sample_label(index)
        signal, sameple_rate = torchaudio.load(audio_sample_path)
        signal = self._resample_if_necessary(signal, sameple_rate)
        signal = self._mix_down_if_necessary(signal)
        signal = self._cut_if_necessary(signal)
        signal = self._right_pad_if_necessary(signal)
        signal = self.transformation(signal)
        return signal, label
    
    def _cut_if_necessary(self, signal):
        if signal.shape[1] > self.num_samples:
            signal = signal[:, :self.num_samples]
        return signal
    
    def _right_pad_if_necessary(self, signal):
        length_signal = signal.shape[1]
        if length_signal < self.num_samples:
            num_missing_samples = self.num_samples - length_signal
            last_dim_padding = (0, num_missing_samples)
            signal = torch.nn.functional.pad(signal, last_dim_padding)
        return signal
                
    def _resample_if_necessary(self, signal, sample_rate):
        if sample_rate != self.target_sample_rate:
            resampler = torchaudio.transforms.Resample(sample_rate, self.target_sample_rate)
            signal = resampler(signal)
        return signal
    
    def _mix_down_if_necessary(self, signal):
        if signal.shape[0] > 1:
            signal = torch.mean(signal, dim=0, keepdim=True)
        return signal
    
    def _get_audio_sample_label(self, index):
        file_path = self.file_list[index]
        label = int(file_path[-15:13])
        return label
    
    
    
    
if __name__ == "__main__":
    ANNOTATIONS_FILE = "./data/UrbanSound8K/metadata/UrbanSound8K.csv"
    AUDIO_DIR = "./data/UrbanSound8K/audio"
    SAMPLE_RATE = 22050
    NUM_SAMPLES = 22050
    mel_spectrogram = torchaudio.transforms.MelSpectrogram(
        sample_rate = SAMPLE_RATE,
        n_fft = 1024,
        hop_length = 512,
        n_mels=64
    )
                
    dataset = UrbanSoundDataset(ANNOTATIONS_FILE, AUDIO_DIR, mel_spectrogram, SAMPLE_RATE, NUM_SAMPLES)
    print(f"There are {len(dataset)} samples in the dataset")
    
    signal, label = dataset[0]
    print(signal)
    a=1