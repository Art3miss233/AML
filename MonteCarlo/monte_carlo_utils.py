import seaborn as sns
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

def show_rewards(rewards):
    
    fig, axs = plt.subplots(1, 2, layout="constrained", figsize=(15, 5), sharey=True)

    fig.suptitle("Average reward wrt to states")
    
    cmap =sns.color_palette("vlag", as_cmap=True)
    
    yticklabels=range(1, 11)
    xticklabels=range(12, 22)
    
    for ax, hold in zip(axs, [1,0]):
        states = {(i, j): reward for (i, j, ace), reward in rewards.items() if ace==hold}
        
        Z = np.array([[states[x,y] if states[x,y] is not None else np.nan  for x in xticklabels ] for y in yticklabels ])

        sns.heatmap(Z, cmap=cmap, annot=True,vmin=-1.0, vmax=1.0, ax=ax, xticklabels=xticklabels, yticklabels=yticklabels, mask=np.isnan(Z))
        ax.set_xlabel('Player sum')
        ax.set_ylabel('Dealer showing')
        
        ax.set_title("usable" if bool(hold) else "not usable")
    plt.show()
    

def show_strategy(policy):

    actions = ["sticks", "hits"]
    
    action_conversion= { a:i for i, a in enumerate(range(2))}

    fig, axs = plt.subplots(1, 2, layout="constrained", figsize=(15, 5), sharey=True)

    fig.suptitle("Optimal policy wrt to states")
    
    colors = ["green", "purple"]
    
    cmap = LinearSegmentedColormap.from_list('Custom', colors, len(colors))
    
    yticklabels=range(1, 11)
    xticklabels=range(12, 22)

    #xticklabels=range(1, 11)
    #yticklabels=range(12, 22)
    
    
    for ax, hold in zip(axs, [1, 0]):
        policy_hold = {(i, j): action for (i, j, ace), action in policy.items() if ace==hold}
        
        Z = np.array([[policy_hold[x,y] if policy_hold[x,y] is not None else np.nan for x in xticklabels ] for y in yticklabels ])

        sns.heatmap(Z, cmap=cmap, annot=False, ax=ax, xticklabels=xticklabels, yticklabels=yticklabels, mask=np.isnan(Z) )
        
        ax.collections[0].colorbar.set_ticklabels(actions)
        ax.collections[0].colorbar.set_ticks(list(range(len(actions))))
        ax.set_xlabel('Player sum')
        ax.set_ylabel('Dealer showing')
        ax.set_title("usable" if bool(hold) else "not usable")
    plt.show()