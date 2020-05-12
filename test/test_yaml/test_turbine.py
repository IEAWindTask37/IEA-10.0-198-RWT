import unittest
import os
from jsonschema import validate
import yaml

path2schema = os.path.dirname( os.path.dirname( os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ) ) ) + os.sep + 'windIO' + os.sep + 'windIO' + os.sep + 'turbine' + os.sep + "IEAontology_schema.yaml"

class TestRegression(unittest.TestCase):
    
    def test_IEA_3_4_130_RWT(self):
        
        path2yaml = os.path.dirname( os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ) ) + os.sep + 'yaml' + os.sep + "IEA-10-198-RWT.yaml"
        # Read the input yaml
        with open(path2yaml, 'r') as myfile:
            inputs = myfile.read()

        # Read the schema
        with open(path2schema, 'r') as myfile:
            schema = myfile.read()

        # Run the validate class from the jsonschema library
        validate(yaml.load(inputs, Loader=yaml.FullLoader), yaml.load(schema, Loader=yaml.FullLoader))

        # Move it to a dictionary called wt_data
        wt_data = yaml.load(inputs, Loader=yaml.FullLoader)

        return None 

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRegression))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
    
    
