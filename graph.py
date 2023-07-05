import numpy as np
from matplotlib import pyplot
from math import fabs

def main():
	simpleGraph("e-", "Water", 8)            # For one graph.
	compareGraph("e-", 8) # For comparing materials.
	#compareAllGraphs()                       # For generating all graphs.
	return


def compareMaterials(par, mat, eng, path="energyActor", axis=False, ticks=False):
	for particle in par:
		for energy in eng:
			for material in mat:
				x, y = generateGraph(f"{path}_{particle}_{material}_{energy}-Edep.txt")
				if (x != 0):
					pyplot.plot(x,y, label=material)
					pyplot.legend()

					pyplot.title(f"Energy Deposition vs Depth ({energy} MeV {particle} beam)")
					pyplot.xlabel("Depth (mm)")
					pyplot.ylabel("Energy Deposition (a.u.)")
				else:
					pass

			pyplot.show()
	return


def simpleGraph(particle, material, energy, path="energyActor"):
	compareMaterials( (particle,), (material,), (energy,), path=path )
	return


def compareGraph(particle, energy, path="energyActor"):
	compareMaterials( ("e-",), ("Water", "ScintY", "ScintX", "PMMA"), (energy,), path=path )


def compareAllGraphs():
	compareMaterials( ("e-", "gamma", "proton"), ("Water", "ScintY", "ScintX", "PMMA"), range(3,20+1), path="energyActor")
	return


def generateGraph(filename):
	try:
		infile = open(filename)
		for i in range(4):
			next(infile)
		line = next(infile)
		line = line.strip()
		lineArray = line.split(' ')
		numBins = int(lineArray[-1])

		x = list(range(numBins))
		y = []

		next(infile)
		for line in infile:
			line = line.strip()
			y.append(float(line))

		infile.close()

	except FileNotFoundError:
		x = 0
		y = 0

	return x,y


def integrateGraph(x, y, cut=0):
	myIntegral = 0
	deltaX = sum(x) / len(x)

	for val in y:
		myIntegral += val if val > cut else 0
	myIntegral = myIntegral * deltaX

	return myIntegral


if __name__ == "__main__":
	main()
