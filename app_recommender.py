import streamlit as st
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os
import gdown

# Crear carpeta si no existe
os.makedirs("recommender_artifacts", exist_ok=True)

# Descargar archivos grandes desde Google Drive (reemplaza con tus IDs reales)
gdown.download("https://drive.google.com/uc?id=1-1aiZmE-_N40IS4vEHfXX5fSdZhXuCBb", "recommender_artifacts/df_rec.parquet", quiet=False)
gdown.download("https://drive.google.com/uc?id=1-23W8XpXbyjQo99BEjGpnpWFqaYqwKC5", "recommender_artifacts/embeddings.npy", quiet=False)
gdown.download("https://drive.google.com/uc?id=1-A3LtK-PkW7FC624c_NwEytRGRvOgq_n", "recommender_artifacts/faiss.index", quiet=False)

# Funciones y app (igual que antes)
# Puedes pegar aquí el resto de tu código, desde load_artifacts() hasta el final
st.title("Movie Recommender System")
st.markdown("Recomienda películas a partir de tus favoritas o de una descripción de tu estado de ánimo.")
