# postRealESSI
A simple python post-processor for RealESSI HDF5 output

## Intro

postRealESSI is meant to handle simple post-processing tasks for RealESSI output. postRealESSI is good for:

* Plotting single (or a few) nodal displacement histories or elemental output histories.
* Finding out global model parameters (number of nodes, elements, time steps, etc.)

Things postRealESSI is not really meant to do (you can do it if you want to wait a lot or have a simple model):

* Showing a mesh deformed shape (use visitESSI for that)
* Determining maximums or minimums of nodal or elemental data (you're better off directly doing it using the HDF5 api)

I intend to provide a simple, object oriented interface to the output format to aid in simple tasks.

## Installing

Clone the repo:

   git clone git@github.com:jaabell/postRealESSI.git

Install the module

   cd postRealESSI
   python setup.py build
   sudo setup.py install
   
## Using postRealESSI

The following example shows how to use postRealESSI to plot the time response of a node.

  # Import the module
  import postRealESSI
  
  # Open a model output file
  essi_model = postRealESSI.open_essi_output_file("mymodel_stage.h5.feioutput")
  
  # Get time vector
  t = essi_model.getTime()
  
  # Get nodal displacements for node with tag 1
  node1 = essi_model.getNode(1)
  displacements = node1.get_generalized_displacements()
  
  # Plot using matplotlib
  import matplolib.pyplt as plt
  plt.figure()
  plt.plot(t,displacements[0,:], label="ux")
  plt.plot(t,displacements[1,:], label="uy")
  plt.plot(t,displacements[2,:], label="uz")
  plt.xlabel("Time [s]")
  plt.ylabel("Displacements [m]")
  plt.legend()
  
