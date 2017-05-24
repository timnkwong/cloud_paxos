# cs171_cloud_paxos

DICTIONARY HIERARCHY FORMATTING:

MAIN_PRM_LOG[index] = ...                   //index will be int key mapping to dictionary  
      {'name': filename, 'words': {...}}    //name key will map to filename of the indexed dictionary, words key maps to logged dictionary
            'words': {'wordA': #, 'wordB': #, etc. }    /*  inside the words dictionary, each word key will map to the int number of times                                                             they occur */
