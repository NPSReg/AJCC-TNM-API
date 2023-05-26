# AJCC-TNM-API
TNM is a three-pronged tumor staging definition set: Tumor staging, nodal staging and metastasis staging.
There exists two main accepted terminologies / definition sets for TNM across different tumor groups: UICC (european) and AJCC (american).
Originally the Norwegian project wanted to continue using UICC, however the terminology access was via PDF / physical book.
The AJCC terminology is accessable via an API, and and is therefore considered for the structured EHR / registry project.
* Note that the difference between the terminologies are minute, see https://pubmed.ncbi.nlm.nih.gov/30711335/

This code does the following:
* Access the AJCC API using a developer key (not included in this repository, uses a .env key)
* Sends separate requests for T, N and M definitions for p (pathological), c ( clinical) each with /without the y (neoadjuvant) modifier
* Receives an XML response for each of these 12 requests, adds some metadata, wrangles using pandas
* Stores the pandas dataframe as human / machine readable CSV file

Since this code is based on a developer API license, the scope is only prostate cancer, with more to follow with access to a general API license.

Lagt til en linje her, det er bra.