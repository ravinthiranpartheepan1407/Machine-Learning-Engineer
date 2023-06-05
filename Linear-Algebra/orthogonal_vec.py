import numpy as np
import matplotlib.pyplot as plt

def orthogonal_vec():
    vec_1 = np.array([16,-2,4])
    vec_2 = np.array([0.5,2,-1])
    print(np.dot(vec_1, vec_2)) # Orthogonal because it's 0
    angle = np.arccos(np.dot(vec_1, vec_2) / (np.linalg.norm(vec_2) * np.linalg.norm(vec_2)))
    print(f'The angle is: {angle}')
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot([0, vec_1[0]], [0, vec_1[1]], [0, vec_1[2]])
    ax.plot([0, vec_2[0]], [0, vec_2[1]], [0, vec_2[2]])
    plt.axis((-6,6,-6,6))
    plt.show()

orthogonal_vec()