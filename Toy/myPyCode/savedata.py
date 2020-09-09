    
def read_f(file):
    DATASET_DIR = os.getcwd()
    where_f = os.path.join(DATASET_DIR, file)
    read_f = pd.read_csv(where_f)
    return read_f
