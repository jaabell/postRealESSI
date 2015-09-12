import domain_components
import h5py
import scipy as sp
class RealESSIModel:
    """
RealESSIModel

    Class that takes an input gmsh file (.msh) and provides functionality to parse and transform
    the .msh to other formats. 
    """

    def __init__(self, filename):
        self.filename = filename
        self.f = h5py.File(filename)
        self.time = self.f["time"][:]
        self.Nnodes = self.f["Number_of_Nodes"][0]
        self.Nelems = self.f["Number_of_Elements"][0]
        self.ModelName = self.f["Model_Name"][0]
        self.StageName = self.f["Stage_Name"][0]
        self.PreviousStage = self.f["Previous_Stage"][0]
        self.Nelems = self.f["Number_of_Elements"][0]
        self.Nelems = self.f["Number_of_Elements"][0]

    def getNode(self, tag):
        return domain_components.Node( tag, self.f)

    def getElement(self, tag):
        return domain_components.Element( tag, self.f)

    def getTime(self):
        return self.time

    def __str__(self):
        pass

