import oci
import sys
import getopt
import os


def usage():
    print("Usage: OCIBucketObjectOPS.py [-h] [-c configFile] -b [bucket_name] -o [object_name] -g -p")
    print("       -h : help")
    print("       -c : Specify config file, the default config file is ~/.oci/config")
    print("       -b : Specify Bucket name")
    print("       -o : Specify Object name")
    print("       -g : Get Object ")
    print("       -p : Put Object ")

def download_file(object_name, stream):
    file_name=os.path.basename(object_name)
    file_name_path= "./" + file_name
    f=open(file_name_path,"wb")
    f.write(stream.data)
    f.close()
    return file_name_path

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:b:o:gp", ["help", "configfile=", "bucket_name=", "object_name=", "get", "put"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    configfile = None
    bucket_name = None
    object_name = None
    getFlag = 0
    putFlag = 0
    envfile = None
    debugFlag = 0
    for o, a in opts:
        if o in ("-c", "--configfile"):
            configfile = a.strip()
        elif o in ("-b", "--bucket_name"):
            bucket_name = a.strip()
        elif o in ("-o", "--object_name"):
            object_name = a.strip()
        elif o in ("-g", "--get"):
            getFlag = 1
        elif o in ("-p", "--put"):
            putFlag = 1
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"

    try:
        if configfile is not None:
            config = oci.config.from_file(file_location=configfile)
        else:
            config = oci.config.from_file()

        if bucket_name == None:
            print("Specify Bucket name")
            usage()
            sys.exit(2)

        if object_name == None:
            print("Specify Object name")
            usage()
            sys.exit(2)

        if getFlag == 1 and putFlag == 1:
            print("Specify only one option, either --g or --p name")
            usage()
            sys.exit(2)

        if getFlag == 0 and putFlag == 0:
            print("Specify only one option, either --g or --p name")
            usage()
            sys.exit(2)

        # Initialize service client with default config file
        object_storage_client = oci.object_storage.ObjectStorageClient(config)
        mnamespace = object_storage_client.get_namespace().data

        # Send the request to service, some parameters are not required, see API
        # doc for more info
        if getFlag == 1:
            print(mnamespace)
            get_object_response = object_storage_client.get_object(
                namespace_name=mnamespace,
                bucket_name=bucket_name,
                object_name=object_name)

            # Get the data from response
            stream = get_object_response.data.raw
            download_file(object_name, stream)
            print("Downloaded File->"+object_name)

        if putFlag == 1:
            with open(object_name, 'rb') as f:
                obj = object_storage_client.put_object(mnamespace, bucket_name, object_name, f)
            print("Uploaded File->"+object_name)


    except Exception as e:
          print("OCIBucketobjectOPS.py Failed->")
          print(e)

if __name__ == "__main__":
    main()



