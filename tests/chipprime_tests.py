from nose.tools import *
import chipprime.gene_parser

def setup():
    print "SETUP"
    
def teardown():
    print "TEARDOWN"
    
def test_retreive_annotations():
    id_list = ["60", "7422"]
    #Test genes: Human beta actin (GeneID 60) and human VEGFA (GeneID 7422)
    
    annot = chipprime.gene_parser.retrieve_annotations(id_list)
    
    assert_equal(annot[0]['Name'],"ACTB")
    
def test_parse_annotation():
    id_list = ["60"]
    actin = chipprime.gene_parser.Gene()
    
    annot = chipprime.gene_parser.retrieve_annotations(id_list)
    actin.parse_annotation(annot[0])
    
    assert_equal(actin.gene_id, "60")
    assert_equal(actin.chromosome, '7')
    