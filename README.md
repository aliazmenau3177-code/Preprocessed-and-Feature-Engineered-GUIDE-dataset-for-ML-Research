# Title: Preprocessed-and-Feature-Engineered-GUIDE-dataset-for-ML-Research-on-SOC
# Description
The dataset presented wtihin this repostitory is a pre-processed and feature engineered Data sub set of Microsoft GUIDE which is requried by researchers to carry out ML alogrithm trainings and testings. 
In 2025 Microsft released the first publicly available Dataset of SOC. The intention was to fill the gap of existing research on SOC, where a verified real world dataset for SOC is not available to researchers. This leads to all SOC research being carried out on Datasets of other technologies such as IDS/ IPS e.t.c. With GUIDE, microsoft has filled this gap. 
However, microsoft's GUIDE like any other SOC data set cannot be directly used within Machine learning and Data mining algorithms since it contains many features and fields which are either non numeric in nature or do not make sense to the overall ML prediction process. The dataset has to be conditioned through pre-processing and featuer engineering in order to bring it into a shape which can be utilized by machine learning algorithms. 
# Dataset Information 
The original dataset of Microsoft GUIDE consisted of raw telemetry data related to SOC, consisting of 46 features/ columns, which can be divided into 5 main cateogries of information as follows: -
1. Identifiers
2. Alert Meta Data
3. MITRE ATT&CK annotations
4. Host/ network context
5. Enrichment Labels

The original dataset consists of 7,95,426 rows of records. 
Four sequential processes have been executed on the given dataset to achieve following: -
1. Removal of attributes that do not affect alert correctness or contribute to inferring the type of an offence (i.e. TP/FP)
2. Removal of leakage attirbutes - i.e attributes which may cause a bias within the learning process of the applied ML algorithm
3. Removal of redundancy and noise through feature engineering
4. Normalization and binarization of values
5. Label trasnformation
6. Encoding of important features for utilization by ML algorithms

The resulting code contains the same number of records/ rows as the original one but after the execution of feature engineering and encoding processes the new dataset contains 790 columns

The steps carried out are explained under the heading of methodology

# Code Information 
The excerpt of my original python script, utilized for carrying out the above mentioned pre processing and feature engineering is provided alogwith this readme file as the second file named "SOC_

# Method of Access
The subject Data sub set is in CSV format with a size of 3.48 GB and having 796 columns. 
Since such a large dataset cannot be uploaded directly therefore it has been placed on google drive and a link has been placed within this repository. 
The access is open for this database with a view to facilitate researches across the globe in making their efforts for achieving a better, more optimized and automated SOC. 
# Dataset Link
The pre-processed dataset can be accessed and downloaded through this link: https://drive.google.com/file/d/1lOPmmG2cnZX3ORvevhEH1Ypo5jxCnIrJ/view?usp=drive_link
The downloaded version of dataset has large number of fields and therefore cannot be handled by normal worksheet softwares such as excel.
However it can be viewed and processed further by using softwares such as Row Zero or Tableau
Moreover the zipped version of the dataset is also available on the link https://drive.google.com/file/d/1rKx3uOlaeg_nVVVAm1Xm6Q7gaRBSOrr6/view?usp=drive_link 





Title – Name of the project or dataset.
Description – An overview of the code/dataset.
Dataset Information.
Code Information.
Usage Instructions – How to use or load the dataset and code.
Requirements – Any dependencies (e.g., Python libraries).
Methodology (if applicable) – Steps taken for data processing or modeling.
Citations (if applicable) – If this dataset was used in research,provide references.
License & Contribution Guidelines (if applicable).
