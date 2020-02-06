# Medical Device Indication Annotation

This repository features documentation, data, and code for participating in the shared annotation task of generating a structured database linking medical devices to their indications.

## Permarket Approval Corpus

Our corpus of premarket approval statements mentioning class III device indications can be found at on our [PubAnnotation project page.](http://pubannotation.org/projects/blah6_medical_device)

The ipython notebook pma_corpus_builder.ipynb contains code for downloading data from OpenFDA, parsing it, and uploading to PubAnnotation.

## Named Entity Recognition (NER)

The Blah6 MER folder contains code and data for NER contributed by Diana Sousa.  The NER code leverages the [MER repository](https://github.com/lasigeBioTM/MER) maintained by the [Biomedical Text Mining Team](http://dest.rd.ciencias.ulisboa.pt/) at Univeristy of Lisbon.  A demonstration web app powered by MER (which is blazing fast) is available at http://labs.rd.ciencias.ulisboa.pt/mer/.

##### MER References
* MER: a Shell Script and Annotation Server for Minimal Named Entity Recognition and Linking, F. Couto and A. Lamurias, Journal of Cheminformatics, 10:58, 2018 [https://doi.org/10.1186/s13321-018-0312-9]
 *MER: a Minimal Named-Entity Recognition Tagger and Annotation Server, F. Couto, L. Campos, and A. Lamurias, in BioCreative V.5 Challenge Evaluation, 2017 [https://www.researchgate.net/publication/316545534_MER_a_Minimal_Named-Entity_Recognition_Tagger_and_Annotation_Server]
