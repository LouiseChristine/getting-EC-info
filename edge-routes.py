import os

edge_ids=["edge-769","edge-875","edge-138","edge-538","edge-613","edge-921","edge-894","edge-688","edge-727","edge-947","edge-854","edge-890","edge-918","edge-917","edge-860","edge-929","edge-925","edge-576","edge-650","edge-824"]

#edge_ids = ['edge-85-2']

updated = open('nsx-edge-routing.csv','w+')

for i in range(len(edge_ids)):
    edge_filename = "ROUTING"+edge_ids[i]+".json"
    rf1= open(edge_filename, 'r+')
    rf2= open("updated"+edge_filename, 'w+')
    config=rf1.read()
    config=config.replace('><','>\n<')
    rf2.write(config)
    rf2.close()
    rf2= open("updated"+edge_filename, 'r')
    edge_fw_lines = rf2.readlines()
    print("whoooo "+edge_ids[i])
    for index, line in enumerate(edge_fw_lines,start=1):
        detail=[]
        if "<vnic>" in line:
            detail_1 = "\n"+edge_ids[i]+","+line[:-1]+","
            detail.append(detail_1)
            #updated.write(detail)
        elif "<gatewayAddress>" in line:
            detail_2 = line[:-1]+","
            detail.append(detail_2)
            #updated.write(detail)
        elif "<network>" in line:
            detail_3 = line[:-1]+","
            detail.append(detail_3)
            #updated.write(detail)
##        elif "<isConnected>" in line:
##            detail_4 = line[:-1]+","
##            #print(len(detail))
##            if len(detail)<2:
##                #print(len(detail))
##                detail_4=",,"+detail_4
##                detail.append(detail_4)
##            else:
##                detail.append(detail_4)
##            #updated.write(detail)
        elif "<nextHop>" in line:
            detail_5 = line[:-1]
            detail.append(detail_5)
            #updated.write(detail)
        updated.write(",".join(detail))
    rf2.close()
    rf1.close()
    os.remove("updated"+edge_filename)
updated.close()
        
    
    
    
        
