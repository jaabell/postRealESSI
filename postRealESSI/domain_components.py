import scipy as sp

class Node:
	def __init__(self, tag, essi_file_id):
		print "Getting ", tag
		self.tag = tag
		ii = essi_file_id["/Model/Nodes/Index_to_Coordinates"][tag]
		print "Found at ", ii
		coords = essi_file_id["/Model/Nodes/Coordinates"][ii:(ii+3)]
		print "Coords ", coords
		pos = essi_file_id["/Model/Nodes/Index_to_Generalized_Displacements"][tag]
		print "pos ", pos
		self.ndofs = essi_file_id["/Model/Nodes/Number_of_DOFs"][tag]
		self.x = coords[0]
		self.y = coords[1]
		self.z = coords[2]
		self.u = essi_file_id["/Model/Nodes/Generalized_Displacements"][pos:(pos+self.ndofs),:]

	def __str__(self):
		return "Node {tag} at ({x} m, {y}, {z} m) with {ndofs} dofs.".format(tag = self.tag,x = self.x, y= self.y,z = self.z,ndofs = self.ndofs)

	def get_generalized_displacements(self):
		return self.u

class Element:
	def __init__(self, tag, essi_file_id):
		print "Getting ", tag
		self.tag = tag

		pos = essi_file_id["/Model/Elements/Index_to_Outputs"][tag]

		if pos >= 0:
			self.Noutputs = essi_file_id["/Model/Elements/Number_of_Output_Fields"][tag]
			self.output = essi_file_id["/Model/Elements/Outputs"][pos:(pos+self.Noutputs),:]

	# def __str__(self):
		# return "Node {tag} at ({x} m, {y}, {z} m) with {ndofs} dofs.".format(tag = self.tag,x = self.x, y= self.y,z = self.z,ndofs = self.ndofs)

	def get_output(self):
		return self.output