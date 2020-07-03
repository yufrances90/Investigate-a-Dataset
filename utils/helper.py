import matplotlib.pyplot as plt
import matplotlib as mpl

NUM_COLORS = 5

cm = plt.get_cmap('rainbow')
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=[cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)])

def generate_data_list(data_arr, label_arr):
    
    data_list = []

    for (entry, label) in zip(data_arr, label_arr):
    
        data_list.append({
            'x': entry.index,
            'y': entry,
            'label': label
        })
        
    return data_list

def draw_popularity_graph(data_arr, label_arr):
    
    assert len(data_arr) == NUM_COLORS
    assert len(label_arr) == NUM_COLORS
    
    data_list = generate_data_list(data_arr, label_arr)
    
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111)
    
    for data in data_list:
        ax.plot(data['x'], data['y'], label=data['label'])
        
    ax.set_title("Popularity by Release Year")
    ax.set_xlabel("Release Year")
    ax.set_ylabel("Popularity")

    plt.legend()
    plt.show()
    
def generate_popularity_data_by_genre(genre_key, df):
    
    popularity_df = df[[genre_key, 'release_year', 'popularity']]
    
    popularity_df = popularity_df[popularity_df[genre_key] == 1]

    popularity_df = popularity_df[['release_year', 'popularity']]

    popularity_df = popularity_df.set_index(['release_year'])

    return popularity_df.sum(level=[0]).sort_index()
    
    

 