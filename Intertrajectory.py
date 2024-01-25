import numpy as np
# Trajectory classes 
class Trajectory:
    def __init__(self, points):
        self.points = np.array(points)
        
    def sample_point(self, t):
        # Linear interpolation to sample a point
        if t <= 0:
            return self.points[0]
        elif t >= 1:
            return self.points[-1]
        else:
            idx = int(t * (len(self.points) - 1))
            t = (t * (len(self.points) - 1)) % 1
            return (1 - t) * self.points[idx] + t * self.points[idx + 1]
        
# Calculate inter trajectory point        
def calculate_inter_point(traj1, traj2, alpha):
    point1 = traj1.sample_point(alpha)
    point2 = traj2.sample_point(alpha)
    
    return (1 - alpha) * point1 + alpha * point2

# Example    
if __name__ == "__main__":
    traj1_points = [(0, 0), (1, 0), (2, 1)] 
    traj2_points = [(0, 1), (1, 2), (2, 4)]
    
    traj1 = Trajectory(traj1_points)
    traj2 = Trajectory(traj2_points)
    
    inter_point = calculate_inter_point(traj1, traj2, 0.5)
    print(inter_point) # (0.5, 0.5)
    