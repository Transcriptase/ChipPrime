import sys
from Bio import Entrez


user_email = "russell.d.williams@gmail.com"

Entrez.email = user_email
#NCBI requires email to know who you are
#might need to replace with a user input if anyone else uses this

class Gene(object):
    def parse_annotation(self, annotation):
        #We could extract a lot more info from the annotation
        #Will start with just what we need to pull promoter sequence
        self.symbol = annotation['NomenclatureSymbol']
        self.gene_id = annotation['Id']
        self.chromosome = annotation['GenomicInfo'][0]['ChrLoc']
        self.start = annotation['GenomicInfo'][0]['ChrStart']
        self.stop = annotation['GenomicInfo'][0]['ChrStop']
        self.chr_acc = annotation['GenomicInfo'][0]['ChrAccVer']

def retrieve_annotations(id_list):
    """Annotates Entrez Gene IDs using Bio.Entrez
    
    Takes a list of Gene IDs (stored as strings), looks them up using
    Entrez Gene, and returns a list of dictionaries of their annotations.
    
    Basic code structre from the BioPython cookbook."""
    
    request = Entrez.epost("gene", id = ",".join(id_list))
    #sets up a session and uploads the list of genes
    
    try:
        result = Entrez.read(request)
    except RunTimeError as e:
        #FIXME: More graceful error handling, maybe just generate
        #N/A data with a warning
        print "An error occured while retreiving annotations."
        print "The error was returned as %s" % e
        sys.exit(-1)
    #retrieves the session data
        
    webenv = result['WebEnv']
    query_key = result['QueryKey']
    #moves the session data to accessible variables
    
    data = Entrez.esummary(db = "gene", webenv = webenv, query_key = query_key)
    #downloads the summary data in XML format
    
    annotations = Entrez.read(data)
    #parses the XML into a Python dictionaries
    
    print "Retreived %d annotations for %d genes" % (len(annotations), len(id_list))
    
    return annotations