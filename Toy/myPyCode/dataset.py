    
def f_read(a):
    DATASET_DIR = os.getcwd()
    where_f = os.path.join(DATASET_DIR, a)
    read_f = pd.read_csv(where_f)
    return read_f
