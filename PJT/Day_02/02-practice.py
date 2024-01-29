import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = "C:/Users/SSAFY/Desktop/TLI/TLI/PJT/Day_02/archive/google-stock-dataset-Daily.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=range(1, 7))

# DataFrame 출력
df.head()