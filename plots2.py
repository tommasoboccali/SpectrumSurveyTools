import matplotlib.pyplot as plt
import numpy as np
import textwrap
if (True):
    x = ["Yes","No"]   
    y = [2,9]
    y_norm = [value/sum(y) for value in y]
    wrapped_x = [ "\n".join(textwrap.wrap(label, width=25)) for label in x ]

    print("BARH")
    print (wrapped_x)
    print (y)
    print (y_norm)
    fig, ax = plt.subplots(figsize=(10, 4))
    bars = ax.barh(wrapped_x, y, color='skyblue')
    total = sum(y)
    tit = "Is your centre (also) operating on sensitive data?".replace('+', ',')

# Add annotations for the relative fraction
    for bar, fraction in zip(bars, y_norm):
        width = bar.get_width()
    #    ax.text(bar.get_width() +  total * 0.02,
    #        bar.get_y() + bar.get_height() / 2, 
    #        f"{fraction:.1%}", 
    #        va='center', ha='left', fontsize=12, color='black')
        ax.text(width * 0.5,
            bar.get_y() + bar.get_height()/2,
            f"{fraction:.1%}",
            va='center', ha='center', fontsize=14, color='black', fontweight='bold')
    ax.tick_params(axis='y', labelsize=14)

    ax.set_xlabel('Entries')
    w_title = "\n".join(textwrap.wrap(tit, width=60))
    #ax.set_title(w_title)
    ax.set_title(w_title, fontsize=14, fontweight='bold')
    ax.set_xlim(0, max(y) * 1.1)

    plt.tight_layout()
    plt.show()
