import os
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset

# Dataset class
class GalaxyDataset(Dataset):
    def __init__(self, csv_file, img_dir, transform=None):
        """
        Args:
            csv_file (str): Path to the csv file with annotations.
            img_dir (str): Directory with all the images.
            transform (callable, optinal): Optional transform to be applied on a sample.    
        """
        self.annotations = pd.read_csv(csv_file, header=0)
        self.img_dir = img_dir
        self.transform = transform
    
    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        # Load image path and label
        img_path = os.path.join(self.img_dir, self.annotations.loc[idx, 'image_name'])
        label = int(self.annotations.loc[idx, 'label'])

        # Load image
        image = Image.open(img_path).convert('RGB')

        # Transform image
        if self.transform:
            image = self.transform(image)

        return image, label