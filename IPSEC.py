import os

edge_ids=["edge-769","edge-875","edge-138","edge-538","edge-613","edge-921","edge-894","edge-688","edge-727","edge-947","edge-854","edge-890","edge-918","edge-917","edge-860","edge-929","edge-925","edge-576","edge-650","edge-824"]

#edge_ids = ['edge-85-2']

updated = open('IPSEC.csv','w+')

for i in range(len(edge_ids)):
    edge_filename = "IPSEC"+edge_ids[i]+".json"
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
        if "<enabled>" in line:
            #print("whoooo "+edge_ids[i])
            detail_1 = "\n"+edge_ids[i]+","+line[:-1]+","
            detail.append(detail_1)
        elif "<name>" in line:
            detail_2 = line[:-1]+","
            detail.append(detail_2)
        elif "<localIp>" in line:
            detail_3 = line[:-1]+","
            detail.append(detail_3)            
        elif "<peerIp>" in line:
            detail_4 = line[:-1]+","
            detail.append(detail_4)
        elif "<ipsecSessionType>" in line:
            detail_5 = line[:-1]+","
            detail.append(detail_5)
        elif "<encryptionAlgorithm>" in line:
            detail_6 = line[:-1]+","
            detail.append(detail_6)
        elif "<mtu>" in line:
            detail_7 = line[:-1]+","
            detail.append(detail_7)
        elif "<enablePfs>" in line:
            detail_8 = line[:-1]+","
            detail.append(detail_8)
        elif "<dhGroup>" in line:
            detail_9 = line[:-1]+","
            detail.append(detail_9)
        elif "<localSubnets>" in line:
            detail_10 = "localSubnets,"
            detail.append(detail_10)
        elif "<peerSubnets>" in line:
            detail_11 = "peerSubnets,"
            detail.append(detail_11)
        elif "<subnet>" in line:
            detail_12 = line[:-1]+","
            detail.append(detail_12)
##        elif "<originalPort>" in line:
##            detail_13 = line[:-1]+","
##            detail.append(detail_13)
##        elif "<translatedPort>" in line:
##            detail_14 = line[:-1]+","
##            detail.append(detail_14)
##        elif "<snatMatchDestinationPort>" in line:
##            detail_15 =line[:-1]
##            detail.append(detail_15)
##        elif "<dnatMatchSourceAddress>" in line:
##            detail_16 =line[:-1]
##            detail.append(detail_16)
##        elif "<dnatMatchSourcePort>" in line:
##            detail_17 =line[:-1]
##            detail.append(detail_17)


        updated.write(",".join(detail))
    rf2.close()
    rf1.close()
    os.remove("updated"+edge_filename)
updated.close()
