**OCIBucketObjectOPS**

**Description**
This Python script is for Oracle Cloud Infrastructure (OCI) Object Storage to perform basic operations on buckets and objects. It uses the OCI SDK for Python to connect to the OCI Object Storage service.

**Prerequisites**
- Python installed (version 3.6 or above)
- OCI SDK for Python installed ('oci' package)
- OCI configuration file ('~/.oci/config') or specify a custom configuration file using the '-c' option

**Usage**

OCIBucketObjectOPS.py [-h] [-c configFile] -b [bucket_name] -o [object_name] -g -p
    -h : help
    -c : Specify config file, the default config file is ~/.oci/config
    -b : Specify Bucket name
    -o : Specify Object name
    -g : Get Object
    -p : Put Object 

**Options**
- `-h, --help`: Display help information.
- `-c, --configfile`: Specify the OCI configuration file (default is `~/.oci/config`).
- `-b, --bucket_name`: Specify the OCI Object Storage bucket name.
- `-o, --object_name`: Specify the object's name within the bucket.
- `-g, --get`: Download the specified object from the bucket.
- `-p, --put`: Upload the specified file as an object to the bucket.

**Download an Object**

python OCIBucketObjectOPS.py -c ~/.oci/config -b my_bucket -o my_object -g
This command downloads the specified object (`my_object`) from the bucket (`my_bucket`).

**Upload an Object**
python OCIBucketObjectOPS.py -c ~/.oci/config -b my_bucket -o local_file.txt -p
This command uploads the local file `local_file.txt` as an object to the bucket (`my_bucket`).

**Notes**
- The default configuration file is `~/.oci/config`, but you can specify a custom file using the `-c` option.
