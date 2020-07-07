# IEA-10.0-198-RWT
This repository contains the model data of the offshore reference wind turbine developed within IEA Wind Task 37. 

The documentation of the turbine and the design process is accessible here: https://www.nrel.gov/docs/fy19osti/73492.pdf

The data include the OpenFAST and HAWC2 aeroelastic files, a .yaml file with the corresponding json schema and open-source controllers.

The documentation of the .yaml file is available at https://windio.readthedocs.io/en/latest/

The OpenFAST model uses the ROSCO controller https://github.com/NREL/ROSCO 

If you use the wind turbine, please cite it like this:

	@techreport{RWT,
	Author = {Pietro Bortolotti and Helena Canet Tarres and Katherine Dykes and Karl Merz and Latha Sethuraman and David Verelst and Frederik Zahle},
	Howpublished = {NREL/TP-73492},
	Institution = {International Energy Agency},
	Title = {IEA Wind Task 37 on Systems Engineering in Wind Energy -- WP2.1 Reference Wind Turbines},
    Url ={https://www.nrel.gov/docs/fy19osti/73492.pdf},
	Year = {2019}}

For questions, please ask to Pietro Bortolotti (pietro.bortolotti@nrel.gov)