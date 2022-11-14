# Data Encryption/Decryption (Pyspark)
Data encryption translates data into another form, or code so that only people with access to a secret key (formally called a decryption key) or password can read it. Currently, encryption is one of the most popular and effective data security methods used by organizations. Two main types of data encryption exist - asymmetric encryption, also known as public-key encryption, and symmetric encryption. We encrypt and decrypt data almost every day when browsing websites, accessing digitally signed documents, making digital payments, etc.

Full Description: https://medium.com/codex/encrypting-data-with-spark-big-data-with-pluggable-code-bd70175c98e2

## Configuration Steps

### Step 1
Include encryption_lib.py library in your driver code and adjust encryption_decryption_driver.py based on requirements.

### Step 2
spark-submit encryption_decryption_driver.py --py-files encryption_library/encryption_lib.py

## Output

### Input:
|id |name  |message                  |
|---|------|-------------------------|
|1  |John  |Do you even lift?        |
|2  |Adam  |Do you like Wendy's?     |
|3  |Thomas|The great state of Texas!|

### Encrypt Column 'Message'
|id |name  |message                  |encrypted_message                                               |
|---|------|-------------------------|----------------------------------------------------------------|
|1  |John  |Do you even lift?        |UleFvxOQpJ+00oIM8zPnNlhh0NkMOST+42Ysgne+1qldFFJqSELrd8ezEFF84Xfz|
|2  |Adam  |Do you like Wendy's?     |hI8fd2ea38nq0rZNY86GtcV4CFwQ4UIDu4ZJvZ+GtxC9RpxutqjRMKGQgcaY5hhN|
|3  |Thomas|The great state of Texas!|lf8zkvH5kSQeTO1qfSpzMgBrJntknEPaa6gRZKwLI+H6q/Xa5H7iWmSCYNTynT+I|

### Decrypt Column 'Message'

|id |name  |message                  |encrypted_message                                               |decrypted_message        |
|---|------|-------------------------|----------------------------------------------------------------|-------------------------|
|1  |John  |Do you even lift?        |Ok1SHB9SQcdc6X3oPKHNNGnxT+3jPKAM+1SZF9fTDogK6PvzBLZGGKl6vIR7TXUN|Do you even lift?        |
|2  |Adam  |Do you like Wendy's?     |5yIFzmXIttUPxtU+aYdYIAeg+/P4nPtgbtChEd036hruKb+t/wLi1PoowxSORKhe|Do you like Wendy's?     |
|3  |Thomas|The great state of Texas!|Vp1KiNqV+RgLHS8Ouv+0TgQ5mtcZV2L4qKwaPVTsjgzpwSFNW8Ptt5x/4FYriR9Z|The great state of Texas!|

### Concat Columns for Encryption
|id |name  |message                  |concat_col                          |
|---|------|-------------------------|------------------------------------|
|1  |John  |Do you even lift?        |John:%%%:Do you even lift?          |
|2  |Adam  |Do you like Wendy's?     |Adam:%%%:Do you like Wendy's?       |
|3  |Thomas|The great state of Texas!|Thomas:%%%:The great state of Texas!|

### Encrypt Concatenated Column
|id |name  |message                  |concat_col                          |encrypted_concat_col                                                                    |
|---|------|-------------------------|------------------------------------|----------------------------------------------------------------------------------------|
|1  |John  |Do you even lift?        |John:%%%:Do you even lift?          |8+LMVv2rQl+OagJ3cnvUy/2Rvp8l3RElsnx3sNM17k/Hgvq9AkpQYVn4ntTx4CWg                        |
|2  |Adam  |Do you like Wendy's?     |Adam:%%%:Do you like Wendy's?       |fRarKUkAj3csq/IKWRkZVmuTLLv7MlPOjFW3iNgvyNZBu9/NXNZVUG6Ebu/48u+A                        |
|3  |Thomas|The great state of Texas!|Thomas:%%%:The great state of Texas!|IEu4+WaIte5Sfr8cb9n9dnmo4by3BytSpFfSQoGWB7Oih6iaU2SWHn8hyTU6iauWmUzGVQ0BdkiXN98TOHZCHQ==|

### Decrypt Concatenated Column
|id |name  |message                  |concat_col                          |encrypted_concat_col                                                                    |decrypted_concat_col                |
|---|------|-------------------------|------------------------------------|----------------------------------------------------------------------------------------|------------------------------------|
|1  |John  |Do you even lift?        |John:%%%:Do you even lift?          |XASDVyDRRyodEVcFUlDP0R77g8rJJmodd0Lydp8YhWS9nuE/mX9ETyDVthgz2/gj                        |John:%%%:Do you even lift?          |
|2  |Adam  |Do you like Wendy's?     |Adam:%%%:Do you like Wendy's?       |JoetJAsu+kyJ+/YTuffJ36HK3i/Stdv/VYfotPgsVrgcHAS5J/5x7m1yY4lr7+EV                        |Adam:%%%:Do you like Wendy's?       |
|3  |Thomas|The great state of Texas!|Thomas:%%%:The great state of Texas!|EdevjnuK/UC/WSxDvKtvczg3wHUJU4THRdSrnM+P+Psq5WGGBh2fQvmdW84N4DUS+fttI04DbqvC8T8FnpU6KA==|Thomas:%%%:The great state of Texas!|
