# DATA ANALYSIS IN CLINICAL WORKFLOWS

Data analysis is a process in which information is first collected; it is then validated, processed, stored, and finally analyzed. ** Inconsistencies can arise at any stage, so it is important to verify that the data is complete and consistent ** and, if an error occurs, trace it back to the point in the workflow where it originated so that it can be corrected. 

1. Data Collection 
In clinical information systems such as HIS, RIS, or PACS, errors such as the following may occur:
* Incorrectly selected patient
* Incomplete data

2. Initial Validation
When entering patients into studies, the MWL worklist is checked to ensure the data does not contain the following errors:
* Missing data: Is the data complete?
* No duplicates: Do the identifiers match? 
* Correct formats: Does the information correspond to the recorded field? 

3. Processing / Transformation
At this stage, the following occurs in the systems:
* Data transmission (DICOM)
* Study-patient association
The following errors may occur:
* Incorrect association
* Loss of information

4. Storage (PACS / database)
Verify that:
* Has the complete data arrived? - No incomplete studies
* Are they properly indexed? - No corrupted data


5. Analysis / visualization
The following are detected here:
* Missing images
* Mismatched data
* Viewer issues


6. Error detection and correction
Identify at which stage the error occurred and correct it at the source, if possible.