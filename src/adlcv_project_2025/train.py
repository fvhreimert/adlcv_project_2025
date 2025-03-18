from adlcv_project_2025.model import Model
from adlcv_project_2025.data import MyDataset

def train():
    dataset = MyDataset("data/raw")
    model = Model()
    # add rest of your training code here

if __name__ == "__main__":
    train()
