from tools import *
from bintrees import AVLTree

class Distance:
	def __init__(self, dist, index):
		self.dist = dist
		self.index = index

	def __lt__(self, other):
		if self.dist < other.dist:
			return True

		if self.dist == other.dist and self.index < other.index:
			return True

		return False

	def __le__(self, other):
		if self.dist < other.dist:
			return True

		if self.dist == other.dist and self.index <= other.index:
			return True

		return False

	def __eq__(self, other):
		if self.dist == other.dist and self.index == other.index:
			return True

		return False

	def __ne__(self, other):
		if self.dist != other.dist or self.index != other.index:
			return True

		return False

	def __gt__(self, other):
		if self.dist > other.dist:
			return True

		if self.dist == other.dist and self.index > other.index:
			return True

		return False

	def __ge__(self, other):
		if self.dist > other.dist:
			return True

		if self.dist == other.dist and self.index >= other.index:
			return True

		return False 

	def __str__(self):
		return str(self.index) + ': ' + str(self.dist)


class classifier:
	# multiset for storing sorted distances: insert/delete operation - O(log N)
	# vector<multiset<Distance, Cmp> > P;
	# 2d vector for storing distances matrix
	# vector<unordered_map<int, Distance> > C;
	# vector for storing flags for marking currently active clusters
	# vector<int> II;
	# 2d vector for storing lists of titles in clusters
	# vector<vector<int> > A;

	# The way of separating clusters, either by
	# specifying the number of clusters K, or by
	# specifying a threshold T
	# int cutoffType;

	# number of classes to cluster
	# int numCluster;

	# seperating threshold
	# double threshold;

	# distance function
	# double distanceType;

	# number of rows of features
	# int N;

	# bitset representation of features
	# vector<bitset<FEATURE_SIZE> > features;

	# all-pair distance of features, either compute on-the-fly,
	# or read from file
	# vector<vector<float> > Dist;
	# vector<unordered_map<int, float> > Dist;

	def __init__(self, bfs, dist):
		self.features = bfs
		self.Dist = dist
		self.N = len(self.Dist)

	def __init__(self, dist):
		self.Dist = dist
		self.N = len(self.Dist)


	def setCluster(self, k):
		self.cutoffType = BY_NUMBER
		self.numCluster = k
		self.threshold = 10 * MIN_DIST

	def setThreshold(self, t):
		self.cutoffType = BY_THRESHOLD
		self.threshold = t
		self.numCluster = 1

	def initContainer(self):
		self.C = [None] * self.N
		self.P = [None] * self.N
		self.II = [0] * self.N
		self.A = [None] * self.N

		self.populate_distance()

	def populate_distance(self):
		added = 0
		for i in range(self.N):
			E_temp = self.Dist[i]
			V_temp = {}
			Q_temp = AVLTree()


			for key in E_temp:
				j = key
				D_temp = distance(E_temp[key], key)
				V_temp[key] = D_temp

				if key != i:
					Q_temp[D_temp] = D_temp

				added += 1

			self.C[i] = V_temp
			self.II[i] = 1
			self.P[i] = Q_temp

			A_i = []
			A_i.append(i)
			self.A[i] = A_i

	def clustering(self, linkage_criteria):
		print '    Initialization ...\n'
		self.initContainer()
		print '    Merging clusters ...\n'

		for n in range(self.N - self.numCluster):
			min_dist = MIN_DIST
			min_index = 0

			for k in range(self.N-1):
				if self.II[k] == 1 and len(self.P[k]) > 0:
					dist = self.P[k].min_key().dist
					if dist < min_dist:
						min_dist = dist
						min_index = self.P[k].min_key().index

			if min_dist > self.threshold:
				break

			k1 = min_index
			k2 = self.P[k1].min_key().index

			N_k1 = len(self.A[k1])
			N_k2 = len(self.A[k2])

			self.P[k1].clear()

			for l in range(len(self.A[k2])):
				self.A[k1].append(self.A[k2][l])

			self.II[k2] = 0

			for m in range(self.N):
				if len(self.C[m]) > 0:
					if self.II[m] != 0 and m != k1 and k1 in self.C[m] and k2 in self.C[m]:
						pass



if __name__=='__main__':
	t = AVLTree()
	d1 = Distance(1.12, 1)
	d2 = Distance(0.9, 2)
	d3 = Distance(0.9, 3)

	t[d1] = d1
	t[d2] = d2
	t[d3] = d3

	del t[d3]
	print len(t)


